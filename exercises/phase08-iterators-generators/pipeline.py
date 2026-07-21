"""Exercise 8.4 — a lazy generator pipeline over a log file.

Line format: "TIMESTAMP LEVEL message..." (as in Phase 6).

read_lines(path)      -> yields stripped non-empty lines
parse(lines)          -> yields dicts {"ts": ..., "level": ..., "message": ...}
only_errors(records)  -> yields records with level == "ERROR"
to_messages(records)  -> yields just the message strings

Every stage is a GENERATOR (lazy) — the test checks none of them returns a
list. Prove laziness to yourself: add a counter to parse and confirm it ran
exactly as many times as lines consumed.

Skills practiced:
- Chained generator pipelines
- Laziness
- Streaming file processing
"""


def read_lines(path):
    with open(path, encoding="utf-8") as log_file:
        for line in log_file:
            stripped = line.strip()
            if stripped:
                yield stripped


def parse(lines):
    for line in lines:
        timestamp, level, message = line.split(maxsplit=2)
        yield {"ts": timestamp, "level": level, "message": message}


def only_errors(records):
    for record in records:
        if record["level"] == "ERROR":
            yield record


def to_messages(records):
    for record in records:
        yield record["message"]
