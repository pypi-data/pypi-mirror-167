import os
from functools import lru_cache
from typing import Any, Dict, List, Optional, cast

import xdg
from autoimport import fix_code
from isort import code
from isort.settings import Config
from maison.config import ProjectConfig
from pylsp import hookimpl
from pylsp.workspace import Document


@lru_cache(100)
def read_autoimport_config() -> Dict[str, str]:

    config_files: List[str] = []

    global_config_path = xdg.xdg_config_home() / "autoimport" / "config.toml"
    if global_config_path.is_file():
        config_files.append(str(global_config_path))

    config_files.append("pyproject.toml")

    return cast(
        Dict[str, str],
        ProjectConfig(
            project_name="autoimport", source_files=config_files, merge_configs=True
        ).to_dict(),
    )


def autoimport_isort(
    document: Document, override: Optional[str] = None
) -> Optional[List[Dict[str, Any]]]:
    source = override or document.source

    # Auto import
    after = fix_code(source, config=read_autoimport_config())

    # isort
    after = code(
        after,
        config=Config(settings_path=os.path.dirname(os.path.abspath(document.path))),
    )

    if source == after:
        return None
    return [
        {
            "range": {
                "start": {
                    "line": 0,
                    "character": 0,
                },
                "end": {
                    "line": len(document.lines),
                    "character": 0,
                },
            },
            "newText": after,
        }
    ]


@hookimpl(hookwrapper=True)  # type: ignore
def pylsp_format_document(document: Document):  # type: ignore
    outcome = yield
    results = outcome.get_result()
    if results:
        newResults = autoimport_isort(document, results[0]["newText"])
    else:
        newResults = autoimport_isort(document)

    if newResults:
        outcome.force_result(newResults)


@hookimpl(hookwrapper=True)  # type: ignore
def pylsp_format_range(document: Document, range: Dict[str, str]):  # type: ignore
    outcome = yield
    results = outcome.get_result()
    if results:
        newResults = autoimport_isort(document, results[0]["newText"])
    else:
        newResults = autoimport_isort(document)

    if newResults:
        outcome.force_result(newResults)
