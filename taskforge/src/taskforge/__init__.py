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
from taskforge.errors import (
    DuplicateTask,
    InvalidTask,
    StorageError,
    TaskForgeError,
    TaskNotFound,
)
from taskforge.models import Priority, Task
from taskforge.repository import JsonRepository, MemoryRepository, TaskRepository


__version__ = "0.3.0a0"

__all__ = [
    "__version__",
    "add_task",
    "complete_task",
    "DuplicateTask",
    "find_by_tag",
    "InvalidTask",
    "JsonRepository",
    "MemoryRepository",
    "pending_sorted_by_priority",
    "Priority",
    "remove_task",
    "rename_tag",
    "stats",
    "StorageError",
    "Task",
    "TaskForgeError",
    "TaskNotFound",
    "TaskRepository",
]
