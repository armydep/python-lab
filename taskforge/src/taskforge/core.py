"""Legacy dict-based TaskForge core operations.

A task is a dict: {"id": int, "title": str, "done": bool,
"tags": set[str], "priority": int}. Ids come from an incrementing counter.

As of Phase 7, the primary domain model is ``taskforge.models.Task`` and the
primary collection boundary is ``taskforge.repository.TaskRepository``. This
module remains public as a compatibility API for earlier roadmap phases and
their tests.

Design rule (from the roadmap): no function both mutates its input AND
returns a value — pick one per function and say which in its docstring.
"""

from collections.abc import Iterable
from itertools import count
from typing import Any

from taskforge.errors import InvalidTask, DuplicateTask, TaskNotFound

Task = dict[str, Any]
_task_ids = count(start=1)


def _find_task_by_id(tasks: list[Task], task_id: int) -> Task | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def _find_task_by_title(tasks: list[Task], task_title: str) -> Task | None:
    for task in tasks:
        if task["title"] == task_title:
            return task
    return None


def sync_next_task_id(tasks: list[Task]) -> None:
    """Advance the ID counter beyond existing tasks; return nothing."""
    global _task_ids
    next_id = max((task["id"] for task in tasks), default=0) + 1
    _task_ids = count(start=next_id)


def add_task(tasks: list[Task], title: str, *, tags: Iterable[str] | None = None, priority: int = 1,) -> None:
    """Append a new incomplete task with a unique ID; return nothing."""
    if not title.strip():
        raise InvalidTask("title cannot be empty")
    if priority < 0:
        raise InvalidTask("priority cannot be negative")
    if _find_task_by_title(tasks, title) is not None:
        raise DuplicateTask(title)
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
    task = _find_task_by_id(tasks, task_id)
    if task is None:
        raise TaskNotFound(task_id)
    task["done"] = True


def remove_task(tasks: list[Task], task_id: int) -> None:
    """Remove the task with ``task_id`` in place; return nothing."""
    task = _find_task_by_id(tasks, task_id)
    if task is None:
        raise TaskNotFound(task_id)
    tasks.remove(task)


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
