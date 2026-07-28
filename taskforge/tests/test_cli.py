"""Tests for TaskForge CLI command dispatch."""

from pathlib import Path

import pytest

import taskforge
from taskforge.cli import COMMANDS, import_command, main, version_command
from taskforge.errors import StorageError
from taskforge.models import Priority, Task
from taskforge.repository import JsonRepository, MemoryRepository


def test_version_command_prints_package_version(capsys) -> None:
    should_continue = version_command(MemoryRepository(), [])

    assert should_continue is True
    assert capsys.readouterr().out == f"{taskforge.__version__}\n"


def test_version_command_rejects_arguments() -> None:
    with pytest.raises(ValueError, match="usage: version"):
        version_command(MemoryRepository(), ["unexpected"])


def test_version_command_is_registered() -> None:
    assert COMMANDS["version"] is version_command


def test_repl_reports_domain_error_and_continues(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    commands = iter(
        [
            "add Existing task",
            "add Existing task",
            "quit",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    main(JsonRepository(tmp_path / "tasks.json"))

    output = capsys.readouterr().out
    assert "Duplicate task: 'Existing task'" in output


def test_repl_does_not_swallow_unexpected_errors(
    monkeypatch,
) -> None:
    def broken_command(_repo, _arguments):
        raise RuntimeError("programming bug")

    monkeypatch.setitem(COMMANDS, "broken", broken_command)
    monkeypatch.setattr("builtins.input", lambda _prompt: "broken")

    with pytest.raises(RuntimeError, match="programming bug"):
        main(MemoryRepository())


def test_repl_loads_existing_tasks_at_startup(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    storage_path = tmp_path / "tasks.json"
    repo = JsonRepository(storage_path)
    repo.add(
        Task(
            id=10,
            title="Persisted task",
            done=False,
            tags={"disk"},
            priority=Priority.HIGH,
        )
    )
    repo.save()
    commands = iter(["ls", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    main(JsonRepository(storage_path))

    assert "Persisted task" in capsys.readouterr().out


def test_successful_mutation_saves_once(monkeypatch) -> None:
    calls = []
    repo = MemoryRepository()
    commands = iter(["add Saved task", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))
    monkeypatch.setattr(repo, "save", lambda: calls.append(repo.list()))

    main(repo)

    assert len(calls) == 1
    assert calls[0][0].title == "Saved task"


def test_failed_mutation_does_not_save(monkeypatch) -> None:
    calls = []
    repo = MemoryRepository()
    repo.add(Task(id=1, title="Existing", priority=Priority.LOW))
    commands = iter(["add Existing", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))
    monkeypatch.setattr(repo, "save", lambda: calls.append(True))

    main(repo)

    assert calls == []


def test_read_only_command_does_not_save(monkeypatch) -> None:
    calls = []
    repo = MemoryRepository()
    commands = iter(["ls", "stats", "version", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))
    monkeypatch.setattr(repo, "save", lambda: calls.append(True))

    main(repo)

    assert calls == []


def test_storage_error_is_reported_and_repl_remains_alive(monkeypatch, capsys) -> None:
    repo = MemoryRepository()
    commands = iter(["add Unsaved task", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    def fail_save():
        raise StorageError(Path("store.json"), "disk full")

    monkeypatch.setattr(repo, "save", fail_save)

    main(repo)

    output = capsys.readouterr().out
    assert "Storage error for store.json: disk full" in output


def test_csv_export_import_round_trips_all_task_fields(
    tmp_path: Path,
    monkeypatch,
) -> None:
    storage_path = tmp_path / "tasks.json"
    csv_path = tmp_path / "tasks.csv"
    task = Task(
        id=1,
        title="Ship CSV",
        done=True,
        tags={"csv", "io"},
        priority=Priority.HIGH,
    )
    repo = JsonRepository(storage_path)
    repo.add(task)
    repo.save()
    commands = iter(
        [
            f"export csv {csv_path}",
            f"import csv {csv_path}",
            "quit",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    main(JsonRepository(storage_path))

    assert JsonRepository(storage_path).list() == [task]


def test_bad_csv_rows_are_skipped_and_reported(
    tmp_path: Path,
    capsys,
) -> None:
    csv_path = tmp_path / "bad.csv"
    csv_path.write_text(
        "id,title,done,priority,tags,created_at\n"
        "1,Good,false,2,\"[\"\"ok\"\"]\",2026-07-28T12:00:00+00:00\n"
        "not-an-int,Bad,false,1,[],2026-07-28T12:00:00+00:00\n"
        "2,Also good,true,3,\"[\"\"x\"\", \"\"y\"\"]\",2026-07-28T12:00:00+00:00\n",
        encoding="utf-8",
    )
    repo = MemoryRepository()

    import_command(repo, ["csv", str(csv_path)])

    output = capsys.readouterr().out
    tasks = repo.list()
    assert "Skipped malformed CSV row on line 3" in output
    assert [task.title for task in tasks] == ["Good", "Also good"]
    assert tasks[0].tags == {"ok"}
    assert tasks[1].tags == {"x", "y"}
