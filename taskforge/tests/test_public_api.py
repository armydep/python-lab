"""Tests for TaskForge's intentionally public package interface."""

import taskforge
from taskforge import core, errors


PUBLIC_OPERATIONS = {
    "add_task",
    "complete_task",
    "find_by_tag",
    "pending_sorted_by_priority",
    "remove_task",
    "rename_tag",
    "stats",
}
PUBLIC_ERRORS = {
    "DuplicateTask",
    "InvalidTask",
    "StorageError",
    "TaskForgeError",
    "TaskNotFound",
}
EXPECTED_PUBLIC_NAMES = {
    "__version__",
    *PUBLIC_OPERATIONS,
    *PUBLIC_ERRORS,
}


def test_public_api_is_explicit() -> None:
    assert set(taskforge.__all__) == EXPECTED_PUBLIC_NAMES


def test_public_operations_reexport_core_functions() -> None:
    for name in PUBLIC_OPERATIONS:
        assert getattr(taskforge, name) is getattr(core, name)


def test_public_errors_reexport_domain_exceptions() -> None:
    for name in PUBLIC_ERRORS:
        assert getattr(taskforge, name) is getattr(errors, name)


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
    assert taskforge.__version__ == "0.2.0"
