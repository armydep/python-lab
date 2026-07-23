"""Exercise 14.3 — the profiling loop (script; the narrative IS the
deliverable).

1. Write a deliberately slow pipeline over synthetic data: nested-loop
   dedupe, a file re-read INSIDE the loop, a sort inside the loop.
2. python -m cProfile -s cumulative profile_me.py — paste the top rows as
   a comment.
3. Fix ONLY the #1 item. Re-profile, paste again. Repeat until
   diminishing returns. Keep every snapshot: the sequence of profiles +
   fixes is what you're practicing, not the final speed.

Skills practiced:
- cProfile
- Fixing the top hot spot, then re-profiling
"""

from pathlib import Path
from random import Random
from tempfile import TemporaryDirectory
from time import perf_counter


NUMBER_OF_RECORDS = 5_000
NUMBER_OF_POSSIBLE_IDS = 2_500
RANDOM_SEED = 42


def make_synthetic_records() -> list[int]:
    """Create repeatable input containing many duplicate IDs."""
    rng = Random(RANDOM_SEED)
    return [
        rng.randrange(NUMBER_OF_POSSIBLE_IDS)
        for _ in range(NUMBER_OF_RECORDS)
    ]


def is_duplicate(record_id: int, processed: list[tuple[int, str]]) -> bool:
    """Deliberately scan all processed records for a matching ID."""
    for existing_id, _ in processed:
        if existing_id == record_id:
            return True
    return False


def slow_pipeline(
    records: list[int], settings_path: Path
) -> list[tuple[int, str]]:
    """Process records with three intentional performance problems."""
    processed: list[tuple[int, str]] = []

    for record_id in records:
        # Intentionally inefficient #1: linear search makes deduplication
        # quadratic as the processed collection grows.
        if is_duplicate(record_id, processed):
            continue

        # Intentionally inefficient #2: unchanged settings are read from
        # disk once for every unique record.
        category = settings_path.read_text(encoding="utf-8").strip()
        processed.append((record_id, category))

        # Intentionally inefficient #3: the entire growing result is sorted
        # after every insertion instead of once at the end.
        processed.sort(key=lambda item: item[0])

    return processed


def main() -> None:
    records = make_synthetic_records()

    # A temporary file keeps the exercise self-contained while still making
    # the pipeline perform real repeated file I/O.
    with TemporaryDirectory() as temporary_directory:
        settings_path = Path(temporary_directory) / "settings.txt"
        settings_path.write_text("synthetic", encoding="utf-8")

        start = perf_counter()
        processed = slow_pipeline(records, settings_path)
        elapsed = perf_counter() - start

    print(f"Input records: {len(records):,}")
    print(f"Unique records: {len(processed):,}")
    print(f"Elapsed: {elapsed:.3f} seconds")


# Baseline profile — Python 3.14:
#
# $ python -m cProfile -s cumulative profile_me.py
#
# 2,453,152 function calls (2,452,895 primitive calls) in 1.024 seconds
#
# ncalls  tottime  cumtime  function
#      1    0.011    0.980  slow_pipeline
#   2177    0.451    0.700  list.sort
# 2370753   0.249    0.249  sort key lambda
#   5000    0.180    0.180  is_duplicate
#   2177    0.006    0.087  Path.read_text
#   2178    0.002    0.055  Path.open
#   2178    0.047    0.052  _io.open
#
# Sorted by cumulative time, repeated sorting is the first actionable hot
# spot: list.sort and its key function consume about 0.700 of the pipeline's
# 0.980 seconds. Part 3 should fix only that item before profiling again.
if __name__ == "__main__":
    main()
