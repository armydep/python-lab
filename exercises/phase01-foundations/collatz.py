"""Exercise 1.4 — Collatz sequence.

Given a starting number n, print the Collatz sequence and its length.

Rules: if n is even -> n // 2; if odd -> 3*n + 1. Loop until n == 1.

Requirements:
  - Read n from input(); guard against n < 1 and non-numeric input
    (message + exit or re-prompt — your choice, state it in a comment).
  - Print the sequence on one line, e.g. `6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4
    -> 2 -> 1`, then `length: 9`.

Stretch: find which starting number below 1000 produces the longest sequence.

Skills practiced:
- while loops with integer arithmetic (// and %)
- Building a sequence step by step
- Guarding against invalid input
"""

def collatz_sequence(start: int) -> list[int]:
    """Return the Collatz sequence beginning at `start` and ending at 1."""
    # TODO: build and return the sequence
    ans : list[int] = []
    for digit in range(start, 1, -1):
        if digit % 2 == 0:
            ans.append(digit // 2)
        if digit % 2 != 1:
            ans.append(3 * digit + 1)
    return ans


def read_starting_number() -> int | None:
    """Read and validate a starting number from input().

    Choice for invalid input: print a message and exit by returning None.
    """
    # TODO: read input(), reject non-numeric values, and reject numbers < 1.
    pass


def main() -> None:
    """Run the Collatz exercise."""
    # TODO: read the starting number.
    # TODO: generate the sequence.
    # TODO: print values joined with " -> ".
    # TODO: print the sequence length.
    pass


if __name__ == "__main__":
    main()
