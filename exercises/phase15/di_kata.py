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
"""


class ReminderService:
    def __init__(self, clock, repo, notifier):
        raise NotImplementedError

    def remind(self):
        raise NotImplementedError
