"""Repository interfaces for TaskForge tasks."""

from __future__ import annotations

import json
import os
import tempfile
from abc import ABC, abstractmethod
from pathlib import Path

from taskforge.errors import DuplicateTask, StorageError, TaskNotFound
from taskforge.models import Task


class TaskRepository(ABC):
    """Abstract persistence boundary for TaskForge tasks."""

    @abstractmethod
    def add(self, task: Task) -> Task:
        """Add ``task`` to the repository and return the stored task."""
        raise NotImplementedError

    @abstractmethod
    def get(self, task_id: int) -> Task:
        """Return the task with ``task_id``."""
        raise NotImplementedError

    @abstractmethod
    def remove(self, task_id: int) -> None:
        """Remove the task with ``task_id``."""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Task]:
        """Return all stored tasks."""
        raise NotImplementedError

    @abstractmethod
    def save(self) -> None:
        """Persist repository state if this repository is durable."""
        raise NotImplementedError

    @abstractmethod
    def replace_all(self, tasks: list[Task]) -> None:
        """Replace all stored tasks and resync repository state."""
        raise NotImplementedError


class MemoryRepository(TaskRepository):
    """In-memory TaskRepository implementation."""

    def __init__(self, tasks: list[Task] | None = None) -> None:
        self._tasks: list[Task] = list(tasks or [])
        self._sync_next_id()

    def add(self, task: Task) -> Task:
        """Add ``task`` to the repository and return the stored task."""
        self._ensure_unique_title(task.title)
        if task.id is None:
            task.id = self._next_id
            self._next_id += 1
        else:
            self._next_id = max(self._next_id, task.id + 1)
        self._tasks.append(task)
        return task

    def get(self, task_id: int) -> Task:
        """Return the task with ``task_id``."""
        task = self._find_by_id(task_id)
        if task is None:
            raise TaskNotFound(task_id)
        return task

    def remove(self, task_id: int) -> None:
        """Remove the task with ``task_id``."""
        task = self.get(task_id)
        self._tasks.remove(task)

    def list(self) -> list[Task]:
        """Return all stored tasks."""
        return list(self._tasks)

    def save(self) -> None:
        """Do nothing for in-memory repositories."""
        return None

    def replace_all(self, tasks: list[Task]) -> None:
        """Replace all stored tasks and resync the next ID."""
        seen_titles: set[str] = set()
        for task in tasks:
            if task.title in seen_titles:
                raise DuplicateTask(task.title)
            seen_titles.add(task.title)
        self._tasks = list(tasks)
        self._sync_next_id()

    def _find_by_id(self, task_id: int) -> Task | None:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def _ensure_unique_title(self, title: str) -> None:
        if any(task.title == title for task in self._tasks):
            raise DuplicateTask(title)

    def _sync_next_id(self) -> None:
        self._next_id = max(
            (task.id for task in self._tasks if task.id is not None),
            default=0,
        ) + 1


class JsonRepository(MemoryRepository):
    """JSON-backed TaskRepository implementation."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        super().__init__(self._load())

    def save(self) -> None:
        """Persist repository state to JSON."""
        jsonable_tasks = [task.to_dict() for task in self._tasks]
        text = json.dumps(jsonable_tasks, indent=2, sort_keys=True)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._atomic_write(text)

    def _load(self) -> list[Task]:
        try:
            with self.path.open(encoding="utf-8") as file:
                raw_tasks = json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as error:
            raise StorageError(self.path, "invalid JSON") from error
        except OSError as error:
            raise StorageError(self.path, str(error)) from error

        return [Task.from_dict(raw_task) for raw_task in raw_tasks]

    def _atomic_write(self, text: str) -> None:
        temp_name: str | None = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.path.parent,
                delete=False,
            ) as temp_file:
                temp_name = temp_file.name
                temp_file.write(text)
                temp_file.flush()
                os.fsync(temp_file.fileno())
            os.replace(temp_name, self.path)
        except Exception:
            if temp_name is not None:
                try:
                    os.remove(temp_name)
                except FileNotFoundError:
                    pass
            raise
