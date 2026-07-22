"""Exercise 12.6 — regex with groups (plus knowing when NOT to).

Log line shape:
  '127.0.0.1 - - [20/Jul/2026:10:00:00] "GET /api/tasks HTTP/1.1" 200'

parse_request(line) -> (ip, method, path, status:int) using ONE compiled
regex with groups; return None for non-matching lines.

Then in a comment: show one extraction task from this same line where
plain str.split beats the regex, and say why.

Skills practiced:
- re with capture groups
- Knowing when str.split beats a regex
"""

import re


REQUEST_PATTERN = re.compile(
    r"^(?P<ip>\S+)\s+-\s+-\s+"
    r"\[[^]]+\]\s+"
    r'"(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+HTTP/\d+(?:\.\d+)?"\s+'
    r"(?P<status>\d{3})$"
)


def parse_request(line: str) -> tuple[str, str, str, int] | None:
    match = REQUEST_PATTERN.fullmatch(line)
    if match is None:
        return None
    return (
        match.group("ip"),
        match.group("method"),
        match.group("path"),
        int(match.group("status")),
    )


# To extract only the IP, `line.split(maxsplit=1)[0]` beats a regex: the IP is
# already the first whitespace-delimited field, so splitting is shorter and
# communicates that simple structure directly.
