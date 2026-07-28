"""Tests for TaskForge Phase 7 domain models."""

from datetime import UTC, datetime

import pytest

from taskforge.errors import InvalidTask
from taskforge.models import Priority, Task


def test_task_rejects_blank_title() -> None:
    with pytest.raises(InvalidTask, match="title cannot be empty"):
        Task(id=None, title="  ")


def test_task_preserves_original_title_whitespace() -> None:
    task = Task(id=None, title="  Padded title  ")

    assert task.title == "  Padded title  "


def test_task_tags_use_independent_default_sets() -> None:
    first = Task(id=None, title="First")
    second = Task(id=None, title="Second")

    first.tags.add("urgent")

    assert second.tags == set()


def test_task_normalizes_valid_priority_values() -> None:
    task = Task(id=None, title="Priority", priority=3)

    assert task.priority is Priority.HIGH


def test_task_rejects_invalid_priority() -> None:
    with pytest.raises(InvalidTask, match="invalid priority"):
        Task(id=None, title="Priority", priority=99)


def test_task_complete_marks_done() -> None:
    task = Task(id=1, title="Finish model")

    task.complete()

    assert task.done is True


def test_task_matches_title_substring_case_insensitively() -> None:
    task = Task(id=1, title="Ship API", tags={"work"})

    assert task.matches("api") is True
    assert task.matches("SHIP") is True


def test_task_matches_tag_case_insensitively() -> None:
    task = Task(id=1, title="Ship API", tags={"Backend"})

    assert task.matches("backend") is True


def test_task_does_not_match_blank_query() -> None:
    task = Task(id=1, title="Ship API", tags={"backend"})

    assert task.matches("   ") is False


def test_task_to_dict_returns_json_safe_data() -> None:
    created_at = datetime(2026, 7, 28, 12, 0, tzinfo=UTC)
    task = Task(
        id=1,
        title="Serialize",
        done=True,
        tags={"z", "a"},
        priority=Priority.HIGH,
        created_at=created_at,
    )

    assert task.to_dict() == {
        "id": 1,
        "title": "Serialize",
        "done": True,
        "tags": ["a", "z"],
        "priority": 3,
        "created_at": "2026-07-28T12:00:00+00:00",
    }


def test_task_from_dict_restores_task() -> None:
    data = {
        "id": 7,
        "title": "Restore",
        "done": False,
        "tags": ["json", "model"],
        "priority": 1,
        "created_at": "2026-07-28T12:00:00+00:00",
    }

    task = Task.from_dict(data)

    assert task == Task(
        id=7,
        title="Restore",
        done=False,
        tags={"json", "model"},
        priority=Priority.LOW,
        created_at=datetime(2026, 7, 28, 12, 0, tzinfo=UTC),
    )


def test_task_to_dict_from_dict_round_trip() -> None:
    original = Task(
        id=3,
        title="Round trip",
        done=True,
        tags={"phase7", "oop"},
        priority=Priority.MEDIUM,
        created_at=datetime(2026, 7, 28, 12, 0, tzinfo=UTC),
    )

    assert Task.from_dict(original.to_dict()) == original
