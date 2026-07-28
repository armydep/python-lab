"""TaskForge REPL and command-line interface.

Commands: add <title>, done <id>, ls, ls <tag>, stats, export, import,
version, quit.
Parse with str.split; dispatch via a dict of functions (Phase 2 pattern) —
no if/elif chain over command names. All printing lives HERE.
"""

from collections.abc import Callable
from pathlib import Path

import taskforge
from taskforge import csv_adapter
from taskforge.errors import TaskForgeError
from taskforge.models import Task
from taskforge.repository import JsonRepository, MemoryRepository, TaskRepository


DEFAULT_DATA_PATH = Path.home() / ".taskforge" / "tasks.json"


def add_command(repo: TaskRepository, arguments: list[str]) -> bool:
    if not arguments:
        raise ValueError("usage: add <title>")
    task = repo.add(Task(id=None, title=" ".join(arguments)))
    print(f"Added task {task.id}: {task.title}")
    return True


def done_command(repo: TaskRepository, arguments: list[str]) -> bool:
    if len(arguments) != 1:
        raise ValueError("usage: done <id>")
    try:
        task_id = int(arguments[0])
    except ValueError as error:
        raise ValueError("task ID must be an integer") from error
    repo.get(task_id).complete()
    print(f"Completed task {task_id}")
    return True


def print_task(task: Task) -> None:
    marker = "x" if task.done else " "
    tags = ", ".join(sorted(task.tags)) or "-"
    print(
        f"{task.id:>3} [{marker}] {task.title} "
        f"(priority={int(task.priority)}, tags={tags})"
    )


def list_command(repo: TaskRepository, arguments: list[str]) -> bool:
    if len(arguments) > 1:
        raise ValueError("usage: ls [tag]")
    tasks = repo.list()
    selected = (
        [task for task in tasks if arguments[0] in task.tags]
        if arguments
        else tasks
    )
    if not selected:
        print("No tasks")
        return True
    for task in selected:
        print_task(task)
    return True


def stats_command(repo: TaskRepository, arguments: list[str]) -> bool:
    if arguments:
        raise ValueError("usage: stats")
    tasks = repo.list()
    tag_counts: dict[str, int] = {}
    for task in tasks:
        for tag in task.tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    done_count = sum(1 for task in tasks if task.done)
    done_ratio = done_count / len(tasks) if tasks else 0.0

    print(f"Tasks: {len(tasks)}")
    print(f"Done: {done_ratio:.0%}")
    if tag_counts:
        print(
            "Tags: "
            + ", ".join(
                f"{tag}={count}"
                for tag, count in sorted(tag_counts.items())
            )
        )
    else:
        print("Tags: none")
    return True


def export_command(repo: TaskRepository, arguments: list[str]) -> bool:
    if len(arguments) != 2 or arguments[0] != "csv":
        raise ValueError("usage: export csv <path>")
    tasks = repo.list()
    csv_adapter.export_tasks(Path(arguments[1]), tasks)
    print(f"Exported {len(tasks)} task(s) to {arguments[1]}")
    return True


def import_command(repo: TaskRepository, arguments: list[str]) -> bool:
    if len(arguments) != 2 or arguments[0] != "csv":
        raise ValueError("usage: import csv <path>")
    imported_tasks, malformed_lines = csv_adapter.import_tasks(Path(arguments[1]))
    repo.replace_all(imported_tasks)
    for line_number in malformed_lines:
        print(f"Skipped malformed CSV row on line {line_number}")
    print(f"Imported {len(imported_tasks)} task(s) from {arguments[1]}")
    return True


def quit_command(_repo: TaskRepository, arguments: list[str]) -> bool:
    if arguments:
        raise ValueError("usage: quit")
    return False


def version_command(_repo: TaskRepository, arguments: list[str]) -> bool:
    if arguments:
        raise ValueError("usage: version")
    print(taskforge.__version__)
    return True


CommandHandler = Callable[[TaskRepository, list[str]], bool]

COMMANDS: dict[str, CommandHandler] = {
    "add": add_command,
    "done": done_command,
    "export": export_command,
    "import": import_command,
    "ls": list_command,
    "stats": stats_command,
    "quit": quit_command,
    "version": version_command,
}

MUTATING_COMMANDS = {"add", "done", "import"}


def main(repository: TaskRepository | None = None) -> None:
    if repository is None:
        try:
            repository = JsonRepository(DEFAULT_DATA_PATH)
        except TaskForgeError as error:
            print(f"Error: {error}")
            repository = MemoryRepository()

    print(
        "TaskForge v0.3a — commands: add, done, ls, stats, "
        "export, import, version, quit"
    )

    while True:
        try:
            raw_command = input("taskforge> ")
        except (EOFError, KeyboardInterrupt):
            print()
            return

        parts = raw_command.split()
        if not parts:
            continue

        command, *arguments = parts
        handler = COMMANDS.get(command)
        if handler is None:
            print(f"Error: unknown command {command!r}")
            continue

        try:
            should_continue = handler(repository, arguments)
            if command in MUTATING_COMMANDS:
                repository.save()
        except TaskForgeError as error:
            print(f"Error: {error}")
            continue
        except ValueError as error:
            print(f"Error: {error}")
            continue

        if not should_continue:
            return


if __name__ == "__main__":
    main()
