"""Exercise 15.2 — three shapes of the strategy pattern.

format_report(tasks, fmt) renders [{"title": ..., "done": ...}, ...] as:
  fmt="plain" -> "[x] title" / "[ ] title" lines joined by \\n
  fmt="csv"   -> "title,done" header + rows
  fmt="count" -> "3 tasks (1 done)"
Unknown fmt -> ValueError.

Implement it THREE ways in this file: (1) if/elif chain, (2) class-based
strategy objects, (3) FORMATTERS dict-of-functions registry — expose the
registry version as format_report (it's the one under test). Then the
two-sentence verdict in a comment: when does each shape earn its keep?

Skills practiced:
- The strategy pattern three ways (if/elif, classes, dict registry)
- Choosing the simplest form that earns its keep
"""

from abc import ABC, abstractmethod
from collections.abc import Callable, Sequence
from typing import TypedDict


class Task(TypedDict):
    title: str
    done: bool


def format_report_if_elif(tasks: Sequence[Task], fmt: str) -> str:
    """Format tasks by selecting a strategy with an if/elif chain."""
    if fmt == "plain":
        lines = [
            f"[{'x' if task['done'] else ' '}] {task['title']}"
            for task in tasks
        ]
        return "\n".join(lines)

    if fmt == "csv":
        rows = ["title,done"]
        rows.extend(
            f"{task['title']},{task['done']}" for task in tasks
        )
        return "\n".join(rows)

    if fmt == "count":
        done_count = sum(task["done"] for task in tasks)
        return f"{len(tasks)} tasks ({done_count} done)"

    raise ValueError(f"unknown report format: {fmt!r}")


class ReportFormatter(ABC):
    """Interface implemented by class-based report strategies."""

    @abstractmethod
    def format(self, tasks: Sequence[Task]) -> str:
        """Return a formatted report."""


class PlainFormatter(ReportFormatter):
    def format(self, tasks: Sequence[Task]) -> str:
        lines = [
            f"[{'x' if task['done'] else ' '}] {task['title']}"
            for task in tasks
        ]
        return "\n".join(lines)


class CsvFormatter(ReportFormatter):
    def format(self, tasks: Sequence[Task]) -> str:
        rows = ["title,done"]
        rows.extend(
            f"{task['title']},{task['done']}" for task in tasks
        )
        return "\n".join(rows)


class CountFormatter(ReportFormatter):
    def format(self, tasks: Sequence[Task]) -> str:
        done_count = sum(task["done"] for task in tasks)
        return f"{len(tasks)} tasks ({done_count} done)"


CLASS_FORMATTERS: dict[str, ReportFormatter] = {
    "plain": PlainFormatter(),
    "csv": CsvFormatter(),
    "count": CountFormatter(),
}


def format_report_with_classes(tasks: Sequence[Task], fmt: str) -> str:
    """Format tasks using a selected class-based strategy object."""
    try:
        formatter = CLASS_FORMATTERS[fmt]
    except KeyError as error:
        raise ValueError(f"unknown report format: {fmt!r}") from error
    return formatter.format(tasks)


def format_plain(tasks: Sequence[Task]) -> str:
    """Format one task per human-readable line."""
    return "\n".join(
        f"[{'x' if task['done'] else ' '}] {task['title']}"
        for task in tasks
    )


def format_csv(tasks: Sequence[Task]) -> str:
    """Format tasks as simple comma-separated rows."""
    rows = ["title,done"]
    rows.extend(f"{task['title']},{task['done']}" for task in tasks)
    return "\n".join(rows)


def format_count(tasks: Sequence[Task]) -> str:
    """Format only the total and completed task counts."""
    done_count = sum(task["done"] for task in tasks)
    return f"{len(tasks)} tasks ({done_count} done)"


Formatter = Callable[[Sequence[Task]], str]

FORMATTERS: dict[str, Formatter] = {
    "plain": format_plain,
    "csv": format_csv,
    "count": format_count,
}


def format_report(tasks: Sequence[Task], fmt: str) -> str:
    """Format tasks using the function registered for ``fmt``."""
    try:
        formatter = FORMATTERS[fmt]
    except KeyError as error:
        raise ValueError(f"unknown report format: {fmt!r}") from error
    return formatter(tasks)


# Verdict: an if/elif chain earns its keep for a tiny, stable set of choices,
# while classes are worthwhile when strategies carry state or share richer
# behavior. For stateless functions that should be easy to extend, the
# registry is the simplest open design: add a function and one mapping entry.
