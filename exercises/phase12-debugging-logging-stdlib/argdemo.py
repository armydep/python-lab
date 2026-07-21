"""Exercise 12.3 — argparse subcommands (script; test via --help).

Rebuild the Phase 2 textstats driver as a CLI:
  argdemo.py words <file>
  argdemo.py chars <file> --ignore-case/--no-ignore-case
  argdemo.py longest <file> -n 5
Typed arguments (type=Path, type=int), helpful help texts, and a
-v/--verbose count flag. `python argdemo.py --help` must read like a real
tool.

Skills practiced:
- argparse subcommands and typed arguments
- Writing a helpful --help
"""

# TODO
