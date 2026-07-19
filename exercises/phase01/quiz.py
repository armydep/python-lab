"""Phase 1 larger assignment — Terminal Quiz Game.

A multiple-choice quiz that runs in the terminal.

Requirements:
  - Questions live in a list of tuples at the top of this file, e.g.
    ("What does // do?", ["true division", "floor division", "modulo",
    "power"], "b") — at least 8 questions, about Phase 1 material (write
    them yourself; writing questions IS studying).
  - Shuffle question order (random.shuffle).
  - Accept answers a–d; re-prompt on anything else without counting it wrong.
  - Track the score; at the end show a percentage and a letter grade using
    `match` or an elif chain.
  - `--reverse` mode (check sys.argv for now): show the ANSWER text, the user
    picks which QUESTION it belongs to. This must reuse the same question
    data — restructure, don't copy-paste.

Completion check (from the roadmap): survives hostile input — letters where
numbers are expected, empty input, EOF if you're feeling thorough.

Note: in Phase 6 you will move the questions into a JSON file — keep the
data separate from the logic with that in mind.
"""

import random
import sys

QUESTIONS = [
    # ("question text", ["option a", "option b", "option c", "option d"], "a"),
]

# TODO
