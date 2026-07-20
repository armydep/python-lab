"""TaskForge v0.1 — REPL driver (run with: python -m taskforge).

Commands: add <title>, done <id>, ls, ls <tag>, stats, quit.
Parse with str.split; dispatch via a dict of functions (Phase 2 pattern) —
no if/elif chain over command names. All printing lives HERE, not in core.
"""

from taskforge import core  # noqa: F401  (remove noqa once used)


def main():
    raise NotImplementedError  # TODO: REPL loop


if __name__ == "__main__":
    main()
