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
    def area(self) -> float:
        """Return the shape's area."""
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return self.radius * math.pi * self.radius


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def total_area(shapes):
    return sum(shape.area() for shape in shapes)


class Squarish(Protocol):
    """Structural contract for objects with a floating-point side length."""

    side: float


def describe_square(sq: Squarish) -> str:
    """Describe any object that satisfies the Squarish protocol."""
    return f"square-ish with side {sq.side}"
