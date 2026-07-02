"""Exercise 03: classes.

Based on Microsoft More Python for Beginners lesson "03 - Classes".

Assignment
----------
Implement a `Presenter` class:

- `__init__(self, name)` stores the presenter's name.
- `name` is a property. The setter stores the value title-cased
  (e.g. "chris" becomes "Chris"). The getter returns the stored value.
- `greet(self)` returns the string "Hello, {name}".

Run:

    python3 -m unittest tests.test_03_classes
"""


class Presenter:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value.title()

    def greet(self) -> str:
        return f"Hello, {self._name}"
