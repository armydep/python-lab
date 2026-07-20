"""Exercise 12.4 — timezone-aware date handling.

ALL functions take and return timezone-aware datetimes (UTC). `now` is a
parameter everywhere — no datetime.now() inside (that's what makes these
testable; Phase 11 lesson).

older_than(timestamps, days, now) -> those more than `days` days old
by_week(timestamps) -> dict (iso_year, iso_week) -> list of timestamps
humanize_age(ts, now) -> "today" / "1 day ago" / "N days ago"
"""


def older_than(timestamps, days, now):
    raise NotImplementedError


def by_week(timestamps):
    raise NotImplementedError


def humanize_age(ts, now):
    raise NotImplementedError
