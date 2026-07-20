"""Tests for Phase 15 (the function-shaped parts)."""

from pathlib import Path

import pytest

from strategy import format_report
from di_kata import ReminderService
from config_env import Config

TASKS = [
    {"title": "ship", "done": True},
    {"title": "test", "done": False},
    {"title": "docs", "done": False},
]


def test_format_plain():
    out = format_report(TASKS, "plain")
    assert "[x] ship" in out and "[ ] test" in out


def test_format_count():
    assert format_report(TASKS, "count") == "3 tasks (1 done)"


def test_format_unknown():
    with pytest.raises(ValueError):
        format_report(TASKS, "xml")


class FakeClock:
    def __init__(self, now):
        self._now = now

    def now(self):
        return self._now


class FakeRepo:
    def __init__(self, pending):
        self._pending = pending

    def list_pending(self):
        return list(self._pending)


class RecordingNotifier:
    def __init__(self):
        self.sent = []

    def send(self, message):
        self.sent.append(message)


def test_reminder_service_with_fakes():
    from datetime import datetime, timedelta, timezone

    now = datetime(2026, 7, 20, tzinfo=timezone.utc)
    old = {"title": "stale", "created_at": now - timedelta(days=3)}
    fresh = {"title": "new", "created_at": now - timedelta(hours=2)}
    notifier = RecordingNotifier()
    service = ReminderService(FakeClock(now), FakeRepo([old, fresh]), notifier)
    service.remind()
    assert len(notifier.sent) == 1
    assert "stale" in notifier.sent[0]


def test_config_from_env_full():
    cfg = Config.from_env(
        {
            "TASKFORGE_DATA_DIR": "/tmp/tf",
            "TASKFORGE_LOG_LEVEL": "DEBUG",
            "TASKFORGE_MAX_RESULTS": "50",
        }
    )
    assert cfg.data_dir == Path("/tmp/tf")
    assert cfg.log_level == "DEBUG"
    assert cfg.max_results == 50


def test_config_defaults():
    cfg = Config.from_env({"TASKFORGE_DATA_DIR": "/tmp/tf"})
    assert cfg.log_level == "WARNING"
    assert cfg.max_results == 20


def test_config_missing_required():
    with pytest.raises(ValueError, match="TASKFORGE_DATA_DIR"):
        Config.from_env({})


def test_config_invalid_value():
    with pytest.raises(ValueError, match="TASKFORGE_MAX_RESULTS"):
        Config.from_env(
            {"TASKFORGE_DATA_DIR": "/tmp/tf", "TASKFORGE_MAX_RESULTS": "-3"}
        )
