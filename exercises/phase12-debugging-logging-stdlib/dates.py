"""Exercise 12.4 — timezone-aware date handling.

ALL functions take and return timezone-aware datetimes (UTC). `now` is a
parameter everywhere — no datetime.now() inside (that's what makes these
testable; Phase 11 lesson).

older_than(timestamps, days, now) -> those more than `days` days old
by_week(timestamps) -> dict (iso_year, iso_week) -> list of timestamps
humanize_age(ts, now) -> "today" / "1 day ago" / "N days ago"

Skills practiced:
- Timezone-aware UTC datetimes
- timedelta math
- Injecting 'now' for testability
"""

from collections.abc import Iterable
from datetime import datetime, timedelta


def _require_utc(value: datetime) -> None:
    if value.utcoffset() != timedelta(0):
        raise ValueError("datetime must be timezone-aware and in UTC")


def older_than(
    timestamps: Iterable[datetime], days: int, now: datetime
) -> list[datetime]:
    _require_utc(now)
    cutoff = now - timedelta(days=days)
    result = []
    for timestamp in timestamps:
        _require_utc(timestamp)
        if timestamp < cutoff:
            result.append(timestamp)
    return result


def by_week(
    timestamps: Iterable[datetime],
) -> dict[tuple[int, int], list[datetime]]:
    groups: dict[tuple[int, int], list[datetime]] = {}
    for timestamp in timestamps:
        _require_utc(timestamp)
        calendar = timestamp.isocalendar()
        groups.setdefault((calendar.year, calendar.week), []).append(timestamp)
    return groups


def humanize_age(timestamp: datetime, now: datetime) -> str:
    _require_utc(timestamp)
    _require_utc(now)
    days = (now.date() - timestamp.date()).days
    if days == 0:
        return "today"
    if days == 1:
        return "1 day ago"
    return f"{days} days ago"
