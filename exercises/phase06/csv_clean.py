"""Exercise 6.4 — clean a messy CSV.

clean_csv(src, dst) reads src with csv.DictReader, writes a cleaned file to
dst with csv.DictWriter (remember newline="" and encoding="utf-8"), and
returns a list of skipped line numbers.

Cleaning rules: strip whitespace from every field; skip blank lines; skip
rows missing any column value (record their line number).
"""


def clean_csv(src, dst):
    raise NotImplementedError
