"""Tests for TaskForge CLI command dispatch."""

import pytest

import taskforge
from taskforge.cli import COMMANDS, version_command


def test_version_command_prints_package_version(capsys) -> None:
    should_continue = version_command([], [])

    assert should_continue is True
    assert capsys.readouterr().out == f"{taskforge.__version__}\n"


def test_version_command_rejects_arguments() -> None:
    with pytest.raises(ValueError, match="usage: version"):
        version_command([], ["unexpected"])


def test_version_command_is_registered() -> None:
    assert COMMANDS["version"] is version_command
