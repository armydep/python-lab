"""Tests for TaskForge Phase 7 repositories."""

import json
import os
from datetime import UTC, datetime
from pathlib import Path

import pytest

from taskforge.errors import DuplicateTask, StorageError, TaskNotFound
from taskforge.models import Priority, Task
from taskforge.repository import JsonRepository, MemoryRepository, TaskRepository


def make_task(title: str, task_id: int | None = None) -> Task:
    return Task(
        id=task_id,
        title=title,
        tags={"repo"},
        priority=Priority.MEDIUM,
        created_at=datetime(2026, 7, 28, 12, 0, tzinfo=UTC),
    )


def test_memory_repository_is_task_repository() -> None:
    assert isinstance(MemoryRepository(), TaskRepository)


def test_memory_repository_add_assigns_ids() -> None:
    repo = MemoryRepository()

    first = repo.add(make_task("First"))
    second = repo.add(make_task("Second"))

    assert first.id == 1
    assert second.id == 2
    assert repo.list() == [first, second]


def test_memory_repository_respects_existing_task_ids() -> None:
    repo = MemoryRepository()

    existing = repo.add(make_task("Existing", task_id=10))
    new = repo.add(make_task("New"))

    assert existing.id == 10
    assert new.id == 11


def test_memory_repository_rejects_duplicate_titles() -> None:
    repo = MemoryRepository()
    repo.add(make_task("Duplicate"))

    with pytest.raises(DuplicateTask, match="Duplicate"):
        repo.add(make_task("Duplicate"))


@pytest.mark.parametrize("operation", ["get", "remove"])
def test_memory_repository_unknown_id_raises_task_not_found(operation: str) -> None:
    repo = MemoryRepository()

    with pytest.raises(TaskNotFound, match="999"):
        getattr(repo, operation)(999)


def test_memory_repository_remove_deletes_task() -> None:
    repo = MemoryRepository()
    task = repo.add(make_task("Remove me"))

    repo.remove(task.id)

    assert repo.list() == []


def test_memory_repository_replace_all_resets_tasks_and_next_id() -> None:
    repo = MemoryRepository()
    repo.add(make_task("Old"))

    repo.replace_all([make_task("Imported", task_id=20)])
    added = repo.add(make_task("Next"))

    assert [task.title for task in repo.list()] == ["Imported", "Next"]
    assert added.id == 21


def test_memory_repository_replace_all_rejects_duplicate_titles() -> None:
    repo = MemoryRepository()

    with pytest.raises(DuplicateTask, match="Same"):
        repo.replace_all([make_task("Same", 1), make_task("Same", 2)])


def test_json_repository_missing_file_starts_empty(tmp_path: Path) -> None:
    repo = JsonRepository(tmp_path / "missing.json")

    assert repo.list() == []


def test_json_repository_save_and_reload_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "tasks.json"
    repo = JsonRepository(path)
    task = repo.add(make_task("Persist me"))

    repo.save()
    reloaded = JsonRepository(path)

    assert reloaded.list() == [task]


def test_json_repository_save_creates_parent_directories(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "taskforge" / "tasks.json"
    repo = JsonRepository(path)
    repo.add(make_task("Nested"))

    repo.save()

    assert path.exists()


def test_json_repository_stores_json_safe_task_data(tmp_path: Path) -> None:
    path = tmp_path / "tasks.json"
    repo = JsonRepository(path)
    repo.add(make_task("JSON"))

    repo.save()
    raw_tasks = json.loads(path.read_text(encoding="utf-8"))

    assert raw_tasks == [
        {
            "id": 1,
            "title": "JSON",
            "done": False,
            "tags": ["repo"],
            "priority": 2,
            "created_at": "2026-07-28T12:00:00+00:00",
        }
    ]


def test_json_repository_loads_phase6_task_data_without_created_at(
    tmp_path: Path,
) -> None:
    path = tmp_path / "tasks.json"
    path.write_text(
        json.dumps(
            [
                {
                    "id": 4,
                    "title": "Old format",
                    "done": True,
                    "tags": ["phase6"],
                    "priority": 3,
                }
            ]
        ),
        encoding="utf-8",
    )

    repo = JsonRepository(path)
    task = repo.get(4)

    assert task.title == "Old format"
    assert task.done is True
    assert task.tags == {"phase6"}
    assert task.priority is Priority.HIGH


def test_json_repository_corrupt_json_raises_chained_storage_error(
    tmp_path: Path,
) -> None:
    path = tmp_path / "tasks.json"
    path.write_text("{not valid json", encoding="utf-8")

    with pytest.raises(StorageError) as error:
        JsonRepository(path)

    assert isinstance(error.value.__cause__, json.JSONDecodeError)
    assert str(path) in str(error.value)


def test_json_repository_failed_save_preserves_existing_file(
    tmp_path: Path,
    monkeypatch,
) -> None:
    path = tmp_path / "tasks.json"
    repo = JsonRepository(path)
    repo.add(make_task("Original"))
    repo.save()
    original_contents = path.read_bytes()
    repo.add(make_task("New"))

    def broken_replace(_src, _dst):
        raise OSError("disk on fire")

    monkeypatch.setattr(os, "replace", broken_replace)

    with pytest.raises(OSError):
        repo.save()

    assert path.read_bytes() == original_contents
