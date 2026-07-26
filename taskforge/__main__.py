"""TaskForge v0.1 — REPL driver (run with: python -m taskforge).

Commands: add <title>, done <id>, ls, ls <tag>, stats, quit.
Parse with str.split; dispatch via a dict of functions (Phase 2 pattern) —
no if/elif chain over command names. All printing lives HERE, not in core.
"""

from collections.abc import Callable

from taskforge import core


def add_command(tasks: list[core.Task], arguments: list[str]) -> bool:
    if not arguments:
        raise ValueError("usage: add <title>")
    core.add_task(tasks, " ".join(arguments))
    print(f"Added task {tasks[-1]['id']}: {tasks[-1]['title']}")
    return True


def done_command(tasks: list[core.Task], arguments: list[str]) -> bool:
    if len(arguments) != 1:
        raise ValueError("usage: done <id>")
    try:
        task_id = int(arguments[0])
    except ValueError as error:
        raise ValueError("task ID must be an integer") from error
    core.complete_task(tasks, task_id)
    print(f"Completed task {task_id}")
    return True


def print_task(task: core.Task) -> None:
    marker = "x" if task["done"] else " "
    tags = ", ".join(sorted(task["tags"])) or "-"
    print(
        f"{task['id']:>3} [{marker}] {task['title']} "
        f"(priority={task['priority']}, tags={tags})"
    )


def list_command(tasks: list[core.Task], arguments: list[str]) -> bool:
    if len(arguments) > 1:
        raise ValueError("usage: ls [tag]")
    selected = core.find_by_tag(tasks, arguments[0]) if arguments else tasks
    if not selected:
        print("No tasks")
        return True
    for task in selected:
        print_task(task)
    return True


def stats_command(tasks: list[core.Task], arguments: list[str]) -> bool:
    if arguments:
        raise ValueError("usage: stats")
    summary = core.stats(tasks)
    tag_counts = summary["tag_counts"]
    print(f"Tasks: {len(tasks)}")
    print(f"Done: {summary['done_ratio']:.0%}")
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


def quit_command(_tasks: list[core.Task], arguments: list[str]) -> bool:
    if arguments:
        raise ValueError("usage: quit")
    return False


CommandHandler = Callable[[list[core.Task], list[str]], bool]

COMMANDS: dict[str, CommandHandler] = {
    "add": add_command,
    "done": done_command,
    "ls": list_command,
    "stats": stats_command,
    "quit": quit_command,
}


def main() -> None:
    tasks: list[core.Task] = []
    print("TaskForge v0.1 — commands: add, done, ls, stats, quit")

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
            should_continue = handler(tasks, arguments)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        if not should_continue:
            return


if __name__ == "__main__":
    main()
