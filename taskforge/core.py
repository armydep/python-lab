"""TaskForge v0.1 — core operations (Phase 3 larger assignment).

A task is a dict: {"id": int, "title": str, "done": bool,
"tags": set[str], "priority": int}. Ids come from an incrementing counter.

Design rule (from the roadmap): no function both mutates its input AND
returns a value — pick one per function and say which in its docstring.

In Phase 4 you will restructure this into an installable src/ package —
keep I/O out of this module (printing belongs in __main__.py).
"""


def add_task(tasks, title, *, tags=None, priority=1):
    raise NotImplementedError


def complete_task(tasks, task_id):
    raise NotImplementedError


def remove_task(tasks, task_id):
    raise NotImplementedError


def find_by_tag(tasks, tag):
    raise NotImplementedError


def pending_sorted_by_priority(tasks):
    raise NotImplementedError


def stats(tasks):
    """Counts by tag + done ratio."""
    raise NotImplementedError


def rename_tag(tasks, old, new):
    raise NotImplementedError
