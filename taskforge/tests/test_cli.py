"""Tests for TaskForge CLI command dispatch."""

import pytest

import taskforge
from taskforge.cli import COMMANDS, main, version_command


def test_version_command_prints_package_version(capsys) -> None:
    should_continue = version_command([], [])

    assert should_continue is True
    assert capsys.readouterr().out == f"{taskforge.__version__}\n"


def test_version_command_rejects_arguments() -> None:
    with pytest.raises(ValueError, match="usage: version"):
        version_command([], ["unexpected"])


def test_version_command_is_registered() -> None:
    assert COMMANDS["version"] is version_command


def test_repl_reports_domain_error_and_continues(monkeypatch, capsys) -> None:
    commands = iter(
        [
            "add Existing task",
            "add Existing task",
            "quit",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: next(commands))

    main()

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
        main()
