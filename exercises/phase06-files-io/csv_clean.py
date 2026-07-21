"""Exercise 6.4 — clean a messy CSV.

clean_csv(src, dst) reads src with csv.DictReader, writes a cleaned file to
dst with csv.DictWriter (remember newline="" and encoding="utf-8"), and
returns a list of skipped line numbers.

Cleaning rules: strip whitespace from every field; skip blank lines; skip
rows missing any column value (record their line number).

Skills practiced:
- csv.DictReader / DictWriter
- The newline='' requirement
- Skipping and reporting bad rows
"""

import csv


def clean_csv(src, dst):
    """Clean a CSV file and return line numbers of incomplete rows."""
    skipped = []
    with open(src, newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        fields = [name.strip() for name in reader.fieldnames or []]
        reader.fieldnames = fields

        with open(dst, "w", newline="", encoding="utf-8") as destination:
            writer = csv.DictWriter(destination, fieldnames=fields)
            if fields:
                writer.writeheader()
            for row in reader:
                cleaned = {field: (row[field] or "").strip() for field in fields}
                if not fields or any(not value for value in cleaned.values()):
                    skipped.append(reader.line_num)
                    continue
                writer.writerow(cleaned)
    return skipped
