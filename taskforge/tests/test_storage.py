"""Phase 6 contract tests for TaskForge JSON persistence."""

import json

from pathlib import Path

import pytest


storage = pytest.importorskip(
    "taskforge.storage",
    reason="Phase 6 storage module is not implemented yet",
)

from taskforge.errors import StorageError  # noqa: E402


def sample_tasks() -> list[dict]:
    return [
        {
            "id": 1,
            "title": "Ship API",
            "done": False,
            "tags": {"work", "api"},
            "priority": 3,
        },
        {
            "id": 2,
            "title": "Write docs",
            "done": True,
            "tags": set(),
            "priority": 1,
        },
    ]


def test_load_missing_file_returns_empty_list(tmp_path: Path) -> None:
    assert storage.load_tasks(tmp_path / "missing.json") == []


def test_save_and_load_round_trip_tasks(tmp_path: Path) -> None:
    path = tmp_path / "tasks.json"
    tasks = sample_tasks()

    storage.save_tasks(path, tasks)

    assert storage.load_tasks(path) == tasks


def test_json_stores_tags_as_sorted_lists(tmp_path: Path) -> None:
    path = tmp_path / "tasks.json"

    storage.save_tasks(path, sample_tasks())
    raw_tasks = json.loads(path.read_text(encoding="utf-8"))

    assert raw_tasks[0]["tags"] == ["api", "work"]
    assert raw_tasks[1]["tags"] == []


def test_save_creates_parent_directories(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "taskforge" / "tasks.json"

    storage.save_tasks(path, sample_tasks())

    assert path.exists()


def test_corrupt_json_raises_chained_storage_error(
    tmp_path: Path,
) -> None:
    path = tmp_path / "tasks.json"
    path.write_text("{not valid json", encoding="utf-8")

    with pytest.raises(StorageError) as error:
        storage.load_tasks(path)

    assert isinstance(error.value.__cause__, json.JSONDecodeError)
    assert str(path) in str(error.value)


def test_failed_save_preserves_existing_file(tmp_path: Path) -> None:
    path = tmp_path / "tasks.json"
    storage.save_tasks(path, sample_tasks())
    original_contents = path.read_bytes()
    invalid_tasks = sample_tasks()
    invalid_tasks[0]["title"] = object()

    with pytest.raises(TypeError):
        storage.save_tasks(path, invalid_tasks)

    assert path.read_bytes() == original_contents
