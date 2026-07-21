"""Exercise 4.4 — dual-use module.

A module with a main() guarded by `if __name__ == "__main__":`.
Prove it runs as a script (python cli_module.py prints something) AND
imports cleanly (importing it from the REPL prints nothing). Record both
observations in comments.

Phase 4's larger assignment is the TaskForge restructure into a src/
layout with pyproject.toml — see roadmap Phase 4; it happens in the
taskforge/ directory, not here.

Skills practiced:
- The if __name__ == '__main__' guard
- Script execution vs clean importability
"""


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
