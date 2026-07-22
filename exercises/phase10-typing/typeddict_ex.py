"""Exercise 10.5 — TypedDict for dict-shaped data.

TaskRow describes your CSV/JSON row: id (int), title (str), done (bool),
tags (list[str]). row_to_summary(row: TaskRow) -> str builds a one-line
summary. Introduce a wrong-key typo on purpose (row["titel"]), run
mypy, paste the error in a comment, fix it.

Skills practiced:
- TypedDict for dict-shaped data
- Catching wrong-key typos with the checker
"""

from typing import TypedDict


class TaskRow(TypedDict):
    id: int
    title: str
    done: bool
    tags: list[str]


def row_to_summary(row: TaskRow) -> str:
    status = "done" if row["done"] else "todo"
    tags = ", ".join(row["tags"])
    # Using row["titel"] produced:
    # error: TypedDict "TaskRow" has no key "titel"  [typeddict-item]
    # note: Did you mean "title"?
    return f'#{row["id"]} [{status}] {row["title"]} (tags: {tags})'
