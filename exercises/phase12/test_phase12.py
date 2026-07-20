"""Tests for Phase 12 (the function-shaped parts)."""

from datetime import datetime, timedelta, timezone

from dates import older_than, by_week, humanize_age
from counter_refactor import word_frequencies, invert_roles, level_counts
from regex_extract import parse_request

NOW = datetime(2026, 7, 20, 12, 0, tzinfo=timezone.utc)


def ts(days_ago):
    return NOW - timedelta(days=days_ago)


def test_older_than():
    stamps = [ts(1), ts(8), ts(30)]
    assert older_than(stamps, days=7, now=NOW) == [ts(8), ts(30)]


def test_by_week():
    groups = by_week([ts(0), ts(1), ts(7)])
    assert len(groups) == 2  # this week and last week
    for key, members in groups.items():
        assert isinstance(key, tuple) and len(key) == 2
        assert members


def test_humanize_age():
    assert humanize_age(ts(0), NOW) == "today"
    assert humanize_age(ts(1), NOW) == "1 day ago"
    assert humanize_age(ts(5), NOW) == "5 days ago"


def test_word_frequencies():
    assert word_frequencies(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_invert_roles():
    result = invert_roles({"alice": "admin", "bob": "user", "carol": "admin"})
    assert dict(result) == {"admin": ["alice", "carol"], "user": ["bob"]}


def test_level_counts():
    lines = [
        "2026-07-20T10:00:00 INFO ok",
        "2026-07-20T10:00:01 ERROR bad",
        "2026-07-20T10:00:02 ERROR worse",
    ]
    assert level_counts(lines) == {"INFO": 1, "ERROR": 2}


def test_parse_request():
    line = '127.0.0.1 - - [20/Jul/2026:10:00:00] "GET /api/tasks HTTP/1.1" 200'
    assert parse_request(line) == ("127.0.0.1", "GET", "/api/tasks", 200)
    assert parse_request("garbage line") is None
