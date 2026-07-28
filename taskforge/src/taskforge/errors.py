"""Domain exceptions raised by TaskForge's public operations."""


class TaskForgeError(Exception):
    """Base class for expected TaskForge domain errors."""


class TaskNotFound(TaskForgeError):
    """Raised when an operation refers to an unknown task ID."""

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task not found: {task_id}")


class InvalidTask(TaskForgeError):
    """Raised when task data violates a validation rule."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(f"Invalid task: {reason}")


class DuplicateTask(TaskForgeError):
    """Raised when a task title already exists."""

    def __init__(self, title: str) -> None:
        self.title = title
        super().__init__(f"Duplicate task: {title!r}")
