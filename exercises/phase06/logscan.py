"""Exercise 6.3 — stream a log file.

Line format: "TIMESTAMP LEVEL message..." e.g.
"2026-07-20T10:00:00 ERROR db connection lost".

count_levels(path) -> dict level -> count
last_errors(path, n=5) -> list of the last n ERROR lines (stripped)

Constraint: stream line by line — never hold the whole file in memory
(no .read(), no .readlines(); for last_errors use collections.deque(maxlen=n)).
Generate your own 200-line fake log to try it (see make_fake_log below).
"""


def count_levels(path):
    raise NotImplementedError


def last_errors(path, n=5):
    raise NotImplementedError


def make_fake_log(path, lines=200):
    """Optional helper: write a synthetic log for manual experiments."""
    raise NotImplementedError
