"""Tests for TaskForge core validation rules."""

import pytest

import taskforge


@pytest.mark.parametrize("title", ["", "   ", "\t\n"])
def test_add_task_rejects_blank_title(title: str) -> None:
    tasks = []

    with pytest.raises(
        taskforge.InvalidTask,
        match="title cannot be empty",
    ) as error:
        taskforge.add_task(tasks, title)

    assert error.value.reason == "title cannot be empty"
    assert tasks == []


def test_add_task_rejects_negative_priority() -> None:
    tasks = []

    with pytest.raises(
        taskforge.InvalidTask,
        match="priority cannot be negative",
    ) as error:
        taskforge.add_task(tasks, "Valid title", priority=-1)

    assert error.value.reason == "priority cannot be negative"
    assert tasks == []


def test_add_task_accepts_zero_priority() -> None:
    tasks = []

    taskforge.add_task(tasks, "Zero priority", priority=0)

    assert tasks[0]["priority"] == 0


def test_add_task_rejects_duplicate_title() -> None:
    tasks = []
    taskforge.add_task(tasks, "Existing task")

    with pytest.raises(
        taskforge.DuplicateTask,
        match="Existing task",
    ) as error:
        taskforge.add_task(tasks, "Existing task")

    assert error.value.title == "Existing task"
    assert len(tasks) == 1


@pytest.mark.parametrize(
    "operation",
    [taskforge.complete_task, taskforge.remove_task],
    ids=["complete", "remove"],
)
def test_unknown_task_id_raises_task_not_found(operation) -> None:
    tasks = []
    unknown_id = 999_999

    with pytest.raises(
        taskforge.TaskNotFound,
        match=str(unknown_id),
    ) as error:
        operation(tasks, unknown_id)

    assert error.value.task_id == unknown_id
    assert tasks == []
