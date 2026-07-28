"""JSON persistence adapter for TaskForge tasks."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any

from taskforge.errors import StorageError


def _task_to_jsonable(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": task["id"],
        "title": task["title"],
        "done": task["done"],
        "tags": sorted(task["tags"]),
        "priority": task["priority"],
    }


def _task_from_jsonable(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": task["id"],
        "title": task["title"],
        "done": task["done"],
        "tags": set(task["tags"]),
        "priority": task["priority"],
    }


def load_tasks(path: Path) -> list[dict[str, Any]]:
    """Load tasks from ``path``; a missing file means no saved tasks."""
    path = Path(path)
    try:
        with path.open(encoding="utf-8") as file:
            raw_tasks = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        raise StorageError(path, "invalid JSON") from error
    except OSError as error:
        raise StorageError(path, str(error)) from error

    return [_task_from_jsonable(task) for task in raw_tasks]


def save_tasks(path: Path, tasks: list[dict[str, Any]]) -> None:
    """Save tasks to ``path`` using an atomic temp-file replacement."""
    path = Path(path)
    jsonable_tasks = [_task_to_jsonable(task) for task in tasks]
    text = json.dumps(jsonable_tasks, indent=2, sort_keys=True)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            delete=False,
        ) as temp_file:
            temp_name = temp_file.name
            temp_file.write(text)
            temp_file.flush()
            os.fsync(temp_file.fileno())
        os.replace(temp_name, path)
    except Exception:
        if temp_name is not None:
            try:
                os.remove(temp_name)
            except FileNotFoundError:
                pass
        raise
