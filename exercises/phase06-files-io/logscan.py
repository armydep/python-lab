"""Exercise 6.3 — stream a log file.

Line format: "TIMESTAMP LEVEL message..." e.g.
"2026-07-20T10:00:00 ERROR db connection lost".

count_levels(path) -> dict level -> count
last_errors(path, n=5) -> list of the last n ERROR lines (stripped)

Constraint: stream line by line — never hold the whole file in memory
(no .read(), no .readlines(); for last_errors use collections.deque(maxlen=n)).
Generate your own 200-line fake log to try it (see make_fake_log below).

Skills practiced:
- Streaming a file line by line
- collections.deque(maxlen=...)
- Constant-memory processing
"""


def count_levels(path):
    """Return a dict of log levels and their counts."""
    count_dict = {}
    with open(path, encoding="utf-8") as file:
        for line in file:
            parts = line.split(maxsplit=2)
            if len(parts) >= 2:
                level = parts[1]
                count_dict[level] = count_dict.get(level, 0) + 1
    return count_dict


def last_errors(path, n=5):
    """Return a list of the last n ERROR lines (stripped)."""
    from collections import deque

    error_lines = deque(maxlen=n)
    with open(path, encoding="utf-8") as file:
        for line in file:
            parts = line.split(maxsplit=2)
            if len(parts) >= 2 and parts[1] == "ERROR":
                error_lines.append(line.strip())
    return list(error_lines)


def make_fake_log(path, lines=200):
    """Optional helper: write a synthetic log for manual experiments."""
    import random
    from datetime import datetime, timedelta

    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    start_time = datetime.now() - timedelta(days=1)
    with open(path, "w", encoding="utf-8") as file:
        for _ in range(lines):
            timestamp = start_time + timedelta(seconds=random.randint(0, 86400))
            level = random.choice(levels)
            message = f"Sample log message at {timestamp.isoformat()}"
            file.write(f"{timestamp.isoformat()} {level} {message}\n")
