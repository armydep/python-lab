"""TaskForge v0.1 — core operations (Phase 3 larger assignment).

A task is a dict: {"id": int, "title": str, "done": bool,
"tags": set[str], "priority": int}. Ids come from an incrementing counter.

Design rule (from the roadmap): no function both mutates its input AND
returns a value — pick one per function and say which in its docstring.

In Phase 4 you will restructure this into an installable src/ package —
keep I/O out of this module (printing belongs in __main__.py).
"""

from collections.abc import Iterable
from itertools import count
from typing import Any


Task = dict[str, Any]
_task_ids = count(start=1)


def add_task(
    tasks: list[Task],
    title: str,
    *,
    tags: Iterable[str] | None = None,
    priority: int = 1,
) -> None:
    """Append a new incomplete task with a unique ID; return nothing."""
    task = {
        "id": next(_task_ids),
        "title": title,
        "done": False,
        "tags": set() if tags is None else set(tags),
        "priority": priority,
    }
    tasks.append(task)


def complete_task(tasks: list[Task], task_id: int) -> None:
    """Mark the task with ``task_id`` as completed in place; return nothing."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return

    raise ValueError(f"task with ID {task_id} does not exist")


def remove_task(tasks: list[Task], task_id: int) -> None:
    """Remove the task with ``task_id`` in place; return nothing."""
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return

    raise ValueError(f"task with ID {task_id} does not exist")


def find_by_tag(tasks: list[Task], tag: str) -> list[Task]:
    """Return a new list of tasks containing ``tag``; do not mutate tasks."""
    return [task for task in tasks if tag in task["tags"]]


def pending_sorted_by_priority(tasks: list[Task]) -> list[Task]:
    """Return pending tasks with highest priority first; do not mutate."""
    pending = [task for task in tasks if not task["done"]]
    return sorted(
        pending,
        key=lambda task: task["priority"],
        reverse=True,
    )


def stats(tasks: list[Task]) -> dict[str, Any]:
    """Return tag counts and the done ratio; do not mutate tasks."""
    tag_counts = {}

    for task in tasks:
        for tag in task["tags"]:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    done_count = sum(1 for task in tasks if task["done"])
    done_ratio = done_count / len(tasks) if tasks else 0.0

    return {
        "tag_counts": tag_counts,
        "done_ratio": done_ratio,
    }


def rename_tag(tasks: list[Task], old: str, new: str) -> None:
    """Replace ``old`` with ``new`` in every matching task; return nothing."""
    for task in tasks:
        if old in task["tags"]:
            task["tags"].remove(old)
            task["tags"].add(new)
