"""TaskForge's public package interface."""

from taskforge.core import (
    add_task,
    complete_task,
    find_by_tag,
    pending_sorted_by_priority,
    remove_task,
    rename_tag,
    stats,
)


__version__ = "0.1.0"

__all__ = [
    "__version__",
    "add_task",
    "complete_task",
    "find_by_tag",
    "pending_sorted_by_priority",
    "remove_task",
    "rename_tag",
    "stats",
]
