"""CSV interchange adapter for TaskForge tasks."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from taskforge.errors import StorageError


FIELDNAMES = ["id", "title", "done", "priority", "tags"]


def _format_task(task: dict[str, Any]) -> dict[str, str]:
    return {
        "id": str(task["id"]),
        "title": task["title"],
        "done": "true" if task["done"] else "false",
        "priority": str(task["priority"]),
        "tags": json.dumps(sorted(task["tags"])),
    }


def export_tasks(path: Path, tasks: list[dict[str, Any]]) -> None:
    """Write tasks as stable UTF-8 CSV."""
    path = Path(path)
    try:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for task in tasks:
                writer.writerow(_format_task(task))
    except OSError as error:
        raise StorageError(path, str(error)) from error


def _parse_task(row: dict[str, str | None]) -> dict[str, Any]:
    if set(row) != set(FIELDNAMES):
        raise ValueError("unexpected columns")
    if any(row[field] in (None, "") for field in FIELDNAMES):
        raise ValueError("missing field")

    done_text = row["done"]
    if done_text not in {"true", "false"}:
        raise ValueError("done must be true or false")

    tags = json.loads(row["tags"] or "[]")
    if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
        raise ValueError("tags must be a JSON list of strings")

    return {
        "id": int(row["id"] or ""),
        "title": row["title"] or "",
        "done": done_text == "true",
        "tags": set(tags),
        "priority": int(row["priority"] or ""),
    }


def import_tasks(path: Path) -> tuple[list[dict[str, Any]], list[int]]:
    """Read tasks from CSV, returning valid tasks and malformed line numbers."""
    path = Path(path)
    tasks: list[dict[str, Any]] = []
    malformed_lines: list[int] = []

    try:
        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != FIELDNAMES:
                raise StorageError(path, f"CSV header must be {FIELDNAMES}")
            for line_number, row in enumerate(reader, start=2):
                try:
                    tasks.append(_parse_task(row))
                except (ValueError, TypeError, json.JSONDecodeError):
                    malformed_lines.append(line_number)
    except OSError as error:
        raise StorageError(path, str(error)) from error

    return tasks, malformed_lines
