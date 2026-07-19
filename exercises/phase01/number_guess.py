"""Exercise 1.3 — Number guessing game.

The computer picks a random number 1–100 (random.randint). The user guesses;
respond "higher" / "lower"; count attempts; congratulate with the attempt
count on success.

Requirements:
  - Non-numeric input must NOT crash the program: detect it (str.isdigit is
    enough for now — exceptions come in Phase 5), print a message, re-prompt.
    It should not count as an attempt.
  - Out-of-range guesses (<1 or >100) get their own message.
  - Typing "quit" exits gracefully, revealing the number.

Check yourself: feed it "abc", "", "0", "101", then real guesses — no crash,
correct attempt count.
"""

import random

# TODO
