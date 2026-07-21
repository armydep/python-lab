"""Exercise 7.4 — ABC vs Protocol.

Shape(ABC) with abstract area(); Circle(radius) and Rect(width, height)
implement it; total_area(shapes) sums a mixed list.

Then: Squarish is a typing.Protocol requiring a `side` attribute (float);
describe_square(sq: Squarish) returns f"square-ish with side {sq.side}".
Write a class satisfying Squarish WITHOUT inheriting from anything — that's
the point.

Skills practiced:
- Abstract base classes (abc.ABC, @abstractmethod)
- typing.Protocol structural typing
- Polymorphism over a mixed list
"""

from abc import ABC, abstractmethod
from typing import Protocol


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


class Rect(Shape):
    def __init__(self, width, height):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


def total_area(shapes):
    raise NotImplementedError


class Squarish(Protocol):
    side: float


def describe_square(sq):
    raise NotImplementedError
