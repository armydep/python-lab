"""Exercise 15.3 — dependency injection kata.

ReminderService needs a clock (has .now()), a repo (has .list_pending()),
and a notifier (has .send(message)). remind() sends one message per
pending task older than 1 day.

Build it TWICE:
1. BAD version (in comments or a scratch branch): reaches for globals /
   module-level singletons — then try to test it and feel the pain.
2. GOOD version here: constructor injection; the composition root wires
   real objects; tests wire fakes with zero patching.
The diff between the two test files is the argument — keep both.

Skills practiced:
- Dependency injection via the constructor
- The composition root
- Testing with injected fakes
"""

from collections.abc import Iterable
from datetime import datetime, timedelta, timezone
from typing import Protocol, TypedDict


class Task(TypedDict):
    title: str
    created_at: datetime


class ClockProtocol(Protocol):
    def now(self) -> datetime: ...


class RepoProtocol(Protocol):
    def list_pending(self) -> list[Task]: ...


class NotifierProtocol(Protocol):
    def send(self, message: str) -> None: ...


class Clock:
    def now(self) -> datetime:
        """Return the current timezone-aware UTC time."""
        return datetime.now(timezone.utc)


class Repo:
    """In-memory repository of pending tasks."""

    def __init__(self, pending: Iterable[Task] = ()) -> None:
        self._pending = list(pending)

    def list_pending(self) -> list[Task]:
        """Return a copy so callers cannot mutate repository state."""
        return list(self._pending)


class Notifier:
    """Simple notifier that records sent messages."""

    def __init__(self) -> None:
        self.sent: list[str] = []

    def send(self, message: str) -> None:
        self.sent.append(message)


class ReminderService:
    """Send reminders for pending tasks older than one day."""

    def __init__(
        self,
        clock: ClockProtocol,
        repo: RepoProtocol,
        notifier: NotifierProtocol,
    ) -> None:
        self._clock = clock
        self._repo = repo
        self._notifier = notifier

    def remind(self) -> None:
        cutoff = self._clock.now() - timedelta(days=1)

        for task in self._repo.list_pending():
            if task["created_at"] < cutoff:
                self._notifier.send(
                    f"Reminder: {task['title']} is still pending"
                )


# BAD VERSION: dependencies are hidden module-level singletons. Testing this
# version requires patching globals and restoring them after every test.
global_clock = Clock()
global_repo = Repo()
global_notifier = Notifier()


class GlobalReminderService:
    """Deliberately coupled version used for comparison."""

    def remind(self) -> None:
        cutoff = global_clock.now() - timedelta(days=1)
        for task in global_repo.list_pending():
            if task["created_at"] < cutoff:
                global_notifier.send(
                    f"Reminder: {task['title']} is still pending"
                )


def build_reminder_service(
    pending: Iterable[Task] = (),
) -> ReminderService:
    """Composition root: create and wire the concrete dependencies."""
    clock = Clock()
    repo = Repo(pending)
    notifier = Notifier()
    return ReminderService(clock, repo, notifier)
