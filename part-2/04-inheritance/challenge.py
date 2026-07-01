"""Exercise 04: inheritance.

Based on Microsoft More Python for Beginners lesson "04 - Inheritance".

Assignment
----------
Implement two classes:

- `Person` with `__init__(self, name)` and `greet(self)` returning
  "Hello, {name}".
- `Student(Person)` with `__init__(self, name, school)` that calls the
  parent constructor, plus `school_song(self)` returning "Ode to {school}".

Then implement `describe(entity)`, a function that returns
`{"is_person": ..., "is_student": ..., "is_student_subclass": ...}` using
`isinstance`/`issubclass` against `Person`/`Student`.

Run:

    python3 -m unittest tests.test_04_inheritance
"""


class Person:
    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def greet(self) -> str:
        raise NotImplementedError


class Student(Person):
    def __init__(self, name: str, school: str) -> None:
        raise NotImplementedError

    def school_song(self) -> str:
        raise NotImplementedError


def describe(entity: object) -> dict[str, bool]:
    raise NotImplementedError
