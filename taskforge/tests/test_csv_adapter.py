"""Tests for TaskForge CSV import/export adapter."""

import csv
from datetime import UTC, datetime
from pathlib import Path

import pytest

from taskforge import csv_adapter
from taskforge.errors import StorageError
from taskforge.models import Priority, Task


def sample_task() -> Task:
    return Task(
        id=1,
        title="Ship CSV adapter",
        done=True,
        tags={"csv", "adapter"},
        priority=Priority.HIGH,
        created_at=datetime(2026, 7, 28, 12, 0, tzinfo=UTC),
    )


def test_export_writes_documented_stable_header(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"

    csv_adapter.export_tasks(path, [sample_task()])

    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        assert next(reader) == csv_adapter.FIELDNAMES


def test_export_writes_task_object_fields(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"

    csv_adapter.export_tasks(path, [sample_task()])

    with path.open(newline="", encoding="utf-8") as file:
        row = next(csv.DictReader(file))

    assert row == {
        "id": "1",
        "title": "Ship CSV adapter",
        "done": "true",
        "priority": "3",
        "tags": '["adapter", "csv"]',
        "created_at": "2026-07-28T12:00:00+00:00",
    }


def test_export_import_round_trips_task_without_data_loss(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"
    task = sample_task()

    csv_adapter.export_tasks(path, [task])
    imported_tasks, malformed_lines = csv_adapter.import_tasks(path)

    assert malformed_lines == []
    assert imported_tasks == [task]


def test_import_returns_task_instances(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"
    csv_adapter.export_tasks(path, [sample_task()])

    imported_tasks, _malformed_lines = csv_adapter.import_tasks(path)

    assert isinstance(imported_tasks[0], Task)


def test_import_skips_malformed_rows_and_keeps_valid_rows(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"
    path.write_text(
        "id,title,done,priority,tags,created_at\n"
        "1,Good,false,2,\"[\"\"ok\"\"]\",2026-07-28T12:00:00+00:00\n"
        "2,Bad done,maybe,2,\"[\"\"bad\"\"]\",2026-07-28T12:00:00+00:00\n"
        "3,Bad tags,false,2,\"{\"\"not\"\":\"\"a list\"\"}\",2026-07-28T12:00:00+00:00\n"
        "4,Bad priority,false,99,\"[\"\"bad\"\"]\",2026-07-28T12:00:00+00:00\n"
        "5,Bad date,false,2,\"[\"\"bad\"\"]\",not-a-date\n"
        "6,Also good,true,1,\"[\"\"x\"\", \"\"y\"\"]\",2026-07-28T12:00:00+00:00\n",
        encoding="utf-8",
    )

    imported_tasks, malformed_lines = csv_adapter.import_tasks(path)

    assert malformed_lines == [3, 4, 5, 6]
    assert [task.title for task in imported_tasks] == ["Good", "Also good"]
    assert imported_tasks[0].tags == {"ok"}
    assert imported_tasks[1].tags == {"x", "y"}


def test_import_rejects_unexpected_header_with_storage_error(tmp_path: Path) -> None:
    path = tmp_path / "tasks.csv"
    path.write_text("id,title\n1,Incomplete\n", encoding="utf-8")

    with pytest.raises(StorageError, match="CSV header"):
        csv_adapter.import_tasks(path)
