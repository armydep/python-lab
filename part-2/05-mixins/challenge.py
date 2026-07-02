"""Exercise 05: mixins.

Based on Microsoft More Python for Beginners lesson "05 - Mixins".

Assignment
----------
Implement three classes using multiple inheritance:

- `Loggable` with `__init__(self)` setting `self.title = ""` and
  `log(self)` returning "Log message from {title}".
- `Connection` with `__init__(self)` setting `self.server = ""` and
  `connect(self)` returning "Connecting to database on {server}".
- `SqlDatabase(Connection, Loggable)` whose `__init__(self)` calls
  `super().__init__()`, then sets `self.title` to "Sql Connection Demo"
  and `self.server` to "Some_Server".

Then implement `run_framework(item)`: a function returning a list of
strings, calling `item.connect()` first if `item` is a `Connection`, then
`item.log()` if `item` is `Loggable` (skipping whichever doesn't apply).

Run:

    python3 -m unittest tests.test_05_mixins
"""


class Loggable:
    def __init__(self) -> None:
        self.title = ""

    def log(self) -> str:
        return f"Log message from {self.title}"


class Connection:
    def __init__(self) -> None:
        self.server = ""

    def connect(self) -> str:
        return f"Connecting to database on {self.server}"


class SqlDatabase(Connection, Loggable):
    def __init__(self) -> None:
        super().__init__()
        self.title = "Sql Connection Demo"
        self.server = "Some_Server"


def run_framework(item: object) -> list[str]:
    results = []
    if isinstance(item, Connection):
        results.append(item.connect())
    if isinstance(item, Loggable):
        results.append(item.log())
    return results
