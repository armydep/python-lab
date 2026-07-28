"""CSV interchange adapter for TaskForge tasks.

Stable Phase 7 CSV format:

```
id,title,done,priority,tags,created_at
```

Field encoding:

- ``id``: integer task ID.
- ``title``: task title text.
- ``done``: lowercase ``true`` or ``false``.
- ``priority``: integer ``Priority`` value.
- ``tags``: JSON-encoded sorted list of strings inside one CSV cell.
- ``created_at``: ISO 8601 datetime string.

CSV is an import/export interchange format. It is not TaskForge's canonical
store; the canonical durable store is JSON through ``JsonRepository``.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path

from taskforge.errors import InvalidTask, StorageError
from taskforge.models import Task


FIELDNAMES = ["id", "title", "done", "priority", "tags", "created_at"]


def _format_task(task: Task) -> dict[str, str]:
    return {
        "id": str(task.id),
        "title": task.title,
        "done": "true" if task.done else "false",
        "priority": str(int(task.priority)),
        "tags": json.dumps(sorted(task.tags)),
        "created_at": task.created_at.isoformat(),
    }


def export_tasks(path: Path, tasks: list[Task]) -> None:
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


def _parse_task(row: dict[str, str | None]) -> Task:
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

    return Task(
        id=int(row["id"] or ""),
        title=row["title"] or "",
        done=done_text == "true",
        tags=set(tags),
        priority=int(row["priority"] or ""),
        created_at=datetime.fromisoformat(row["created_at"] or ""),
    )


def import_tasks(path: Path) -> tuple[list[Task], list[int]]:
    """Read tasks from CSV, returning valid tasks and malformed line numbers."""
    path = Path(path)
    tasks: list[Task] = []
    malformed_lines: list[int] = []

    try:
        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != FIELDNAMES:
                raise StorageError(path, f"CSV header must be {FIELDNAMES}")
            for line_number, row in enumerate(reader, start=2):
                try:
                    tasks.append(_parse_task(row))
                except (InvalidTask, ValueError, TypeError, json.JSONDecodeError):
                    malformed_lines.append(line_number)
    except OSError as error:
        raise StorageError(path, str(error)) from error

    return tasks, malformed_lines
