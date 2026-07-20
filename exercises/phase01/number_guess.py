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

LOWER_BOUND = 1
UPPER_BOUND = 100


def pick_secret_number() -> int:
    """Return the random number the player is trying to guess."""
    # TODO: use random.randint with the configured bounds.
    random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    return random_number


def read_guess() -> int | str | None:
    """Read and validate one guess from input().

    Return:
      - an int for a valid in-range guess
      - "quit" if the player wants to exit
      - None for invalid input so the caller can re-prompt
    """
    # TODO: read input().
    # TODO: handle "quit".
    # TODO: reject non-numeric input without crashing.
    # TODO: reject out-of-range guesses.
    pass


def play_game() -> None:
    """Run one number guessing game."""
    # TODO: pick the secret number.
    # TODO: repeatedly read guesses until the player wins or quits.
    # TODO: count only valid numeric guesses as attempts.
    # TODO: print higher/lower/success/quit messages.
    pass


def main() -> None:
    """Run the exercise."""
    play_game()


if __name__ == "__main__":
    main()
