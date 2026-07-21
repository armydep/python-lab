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

FORMATTERS = {
    # "plain": ...,
}


def format_report(tasks, fmt):
    raise NotImplementedError
