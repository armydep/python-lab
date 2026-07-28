"""Manual hostile-input checks for TaskForge's public API."""

from collections.abc import Callable

import taskforge


def run_case(
    number: int,
    description: str,
    operation: Callable[[], None],
) -> None:
    """Run one operation and print its expected domain error."""
    print(f"CASE {number}: {description}")
    try:
        operation()
    except taskforge.TaskForgeError as error:
        print(f"{type(error).__name__}: {error}")
    else:
        raise AssertionError(
            f"hostile case unexpectedly succeeded: {description}"
        )


def main() -> None:
    tasks = []
    taskforge.add_task(tasks, "Existing task")

    run_case(
        1,
        "empty title",
        lambda: taskforge.add_task(tasks, ""),
    )
    run_case(
        2,
        "negative priority",
        lambda: taskforge.add_task(
            tasks,
            "Invalid priority",
            priority=-1,
        ),
    )
    run_case(
        3,
        "whitespace-only title",
        lambda: taskforge.add_task(tasks, "   "),
    )
    run_case(
        4,
        "tab-and-newline title",
        lambda: taskforge.add_task(tasks, "\t\n"),
    )
    run_case(
        5,
        "very negative priority",
        lambda: taskforge.add_task(
            tasks,
            "Another invalid priority",
            priority=-100,
        ),
    )
    run_case(
        6,
        "duplicate title",
        lambda: taskforge.add_task(tasks, "Existing task"),
    )
    run_case(
        7,
        "repeated duplicate title",
        lambda: taskforge.add_task(tasks, "Existing task"),
    )
    run_case(
        8,
        "complete unknown ID",
        lambda: taskforge.complete_task(tasks, 999_999),
    )
    run_case(
        9,
        "remove unknown ID",
        lambda: taskforge.remove_task(tasks, 999_999),
    )
    run_case(
        10,
        "complete negative ID",
        lambda: taskforge.complete_task(tasks, -1),
    )

    if len(tasks) != 1 or tasks[0]["title"] != "Existing task":
        raise AssertionError("hostile cases corrupted task state")

    taskforge.add_task(tasks, "Valid after failures")
    if tasks[-1]["title"] != "Valid after failures":
        raise AssertionError("valid operation failed after hostile cases")
    print("VALID AFTER FAILURES: OK")


if __name__ == "__main__":
    main()
