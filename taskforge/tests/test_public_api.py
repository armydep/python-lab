"""Tests for TaskForge's intentionally public package interface."""

import taskforge
from taskforge import core


EXPECTED_PUBLIC_NAMES = {
    "__version__",
    "add_task",
    "complete_task",
    "find_by_tag",
    "pending_sorted_by_priority",
    "remove_task",
    "rename_tag",
    "stats",
}


def test_public_api_is_explicit() -> None:
    assert set(taskforge.__all__) == EXPECTED_PUBLIC_NAMES


def test_public_operations_reexport_core_functions() -> None:
    for name in EXPECTED_PUBLIC_NAMES - {"__version__"}:
        assert getattr(taskforge, name) is getattr(core, name)


def test_public_api_can_add_a_task() -> None:
    tasks = []

    result = taskforge.add_task(
        tasks,
        "Test public API",
        tags={"package"},
        priority=2,
    )

    assert result is None
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test public API"
    assert tasks[0]["tags"] == {"package"}
    assert tasks[0]["priority"] == 2
    assert tasks[0]["done"] is False


def test_version_is_public() -> None:
    assert taskforge.__version__ == "0.1.0"
