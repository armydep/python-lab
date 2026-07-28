"""Object-oriented domain models for TaskForge."""

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from taskforge.errors import InvalidTask


class Priority(enum.IntEnum):
    """Supported task priority levels."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Task:
    """A TaskForge task with validation, behavior, and serialization helpers."""

    id: int | None
    title: str
    done: bool = False
    tags: set[str] = field(default_factory=set)
    priority: Priority = Priority.MEDIUM
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        """Validate and normalize task fields after dataclass initialization."""
        if not self.title.strip():
            raise InvalidTask("title cannot be empty")

        try:
            self.priority = Priority(self.priority)
        except ValueError as error:
            raise InvalidTask(f"invalid priority: {self.priority!r}") from error

        self.tags = set(self.tags)

    def complete(self) -> None:
        """Mark this task as completed."""
        self.done = True

    def matches(self, query: str) -> bool:
        """Return whether ``query`` matches this task's title or tags."""
        normalized_query = query.strip().lower()
        if not normalized_query:
            return False

        if normalized_query in self.title.lower():
            return True

        return any(normalized_query == tag.lower() for tag in self.tags)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-safe dictionary representation of this task."""
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done,
            "tags": sorted(self.tags),
            "priority": int(self.priority),
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Task:
        """Restore a task from data produced by ``to_dict``."""
        try:
            created_at = datetime.fromisoformat(data["created_at"])
        except KeyError:
            created_at = datetime.now(UTC)
        except ValueError as error:
            raise InvalidTask("invalid created_at") from error

        return cls(
            id=data["id"],
            title=data["title"],
            done=data.get("done", False),
            tags=set(data.get("tags", [])),
            priority=data.get("priority", Priority.MEDIUM),
            created_at=created_at,
        )
