"""Exercise 12.6 — regex with groups (plus knowing when NOT to).

Log line shape:
  '127.0.0.1 - - [20/Jul/2026:10:00:00] "GET /api/tasks HTTP/1.1" 200'

parse_request(line) -> (ip, method, path, status:int) using ONE compiled
regex with groups; return None for non-matching lines.

Then in a comment: show one extraction task from this same line where
plain str.split beats the regex, and say why.
"""

import re


def parse_request(line):
    raise NotImplementedError
