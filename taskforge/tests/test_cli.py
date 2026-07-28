"""Tests for TaskForge CLI command dispatch."""

from pathlib import Path

import pytest

import taskforge
from taskforge.cli import COMMANDS, import_command, main, version_command
from taskforge.errors import StorageError
from taskforge.storage import load_tasks, save_tasks


def test_version_command_prints_package_version(capsys) -> None:
    should_continue = version_command([], [])

    assert should_continue is True
    assert capsys.readouterr().out == f"{taskforge.__version__}\n"


def test_version_command_rejects_arguments() -> None:
    with pytest.raises(ValueError, match="usage: version"):
        version_command([], ["unexpected"])


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

    main(tmp_path / "tasks.json")

    output = capsys.readouterr().out
    assert "Duplicate task: 'Existing task'" in output


def test_repl_does_not_swallow_unexpected_errors(
    monkeypatch,
) -> None:
    def broken_command(_tasks, _arguments):
        raise RuntimeError("programming bug")

    monkeypatch.setitem(COMMANDS, "broken", broken_command)
    monkeypatch.setattr("builtins.input", lambda _prompt: "broken")

    with pytest.raises(RuntimeError, match="programming bug"):
        main(Path("unused.json"))


def test_repl_loads_existing_tasks_at_startup(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    storage_path = tmp_path / "tasks.json"
    save_tasks(
        storage_path,
        [
            {
                "id": 10,
                "title": "Persisted task",
                "done": False,
                "tags": {"disk"},
                "priority": 4,
            }
        ],
    )
    commands = iter(["ls", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    main(storage_path)

    assert "Persisted task" in capsys.readouterr().out


def test_successful_mutation_saves_once(monkeypatch) -> None:
    calls = []
    commands = iter(["add Saved task", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))
    monkeypatch.setattr("taskforge.cli.load_tasks", lambda _path: [])
    monkeypatch.setattr(
        "taskforge.cli.save_tasks",
        lambda path, tasks: calls.append((path, [task.copy() for task in tasks])),
    )

    main(Path("store.json"))

    assert len(calls) == 1
    assert calls[0][1][0]["title"] == "Saved task"


def test_failed_mutation_does_not_save(monkeypatch) -> None:
    calls = []
    commands = iter(["add Existing", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))
    monkeypatch.setattr(
        "taskforge.cli.load_tasks",
        lambda _path: [
            {
                "id": 1,
                "title": "Existing",
                "done": False,
                "tags": set(),
                "priority": 1,
            }
        ],
    )
    monkeypatch.setattr("taskforge.cli.save_tasks", lambda _path, _tasks: calls.append(True))

    main(Path("store.json"))

    assert calls == []


def test_read_only_command_does_not_save(monkeypatch) -> None:
    calls = []
    commands = iter(["ls", "stats", "version", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))
    monkeypatch.setattr("taskforge.cli.load_tasks", lambda _path: [])
    monkeypatch.setattr("taskforge.cli.save_tasks", lambda _path, _tasks: calls.append(True))

    main(Path("store.json"))

    assert calls == []


def test_storage_error_is_reported_and_repl_remains_alive(monkeypatch, capsys) -> None:
    commands = iter(["add Unsaved task", "quit"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))
    monkeypatch.setattr("taskforge.cli.load_tasks", lambda _path: [])

    def fail_save(path, _tasks):
        raise StorageError(path, "disk full")

    monkeypatch.setattr("taskforge.cli.save_tasks", fail_save)

    main(Path("store.json"))

    output = capsys.readouterr().out
    assert "Storage error for store.json: disk full" in output


def test_csv_export_import_round_trips_all_task_fields(
    tmp_path: Path,
    monkeypatch,
) -> None:
    storage_path = tmp_path / "tasks.json"
    csv_path = tmp_path / "tasks.csv"
    tasks = [
        {
            "id": 1,
            "title": "Ship CSV",
            "done": True,
            "tags": {"csv", "io"},
            "priority": 5,
        }
    ]
    save_tasks(storage_path, tasks)
    commands = iter(
        [
            f"export csv {csv_path}",
            f"import csv {csv_path}",
            "quit",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    main(storage_path)

    assert load_tasks(storage_path) == tasks


def test_bad_csv_rows_are_skipped_and_reported(
    tmp_path: Path,
    capsys,
) -> None:
    csv_path = tmp_path / "bad.csv"
    csv_path.write_text(
        "id,title,done,priority,tags\n"
        "1,Good,false,2,\"[\"\"ok\"\"]\"\n"
        "not-an-int,Bad,false,1,[]\n"
        "2,Also good,true,3,\"[\"\"x\"\", \"\"y\"\"]\"\n",
        encoding="utf-8",
    )
    tasks = []

    import_command(tasks, ["csv", str(csv_path)])

    output = capsys.readouterr().out
    assert "Skipped malformed CSV row on line 3" in output
    assert [task["title"] for task in tasks] == ["Good", "Also good"]
    assert tasks[0]["tags"] == {"ok"}
    assert tasks[1]["tags"] == {"x", "y"}
