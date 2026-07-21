"""Exercise 7.2 — a 2D Vector with operator dunders.

Support: v + w, v - w, v * 3 AND 3 * v (__rmul__), abs(v) (magnitude),
v == w, readable __repr__. Predict-then-run: what happens for v * "x"?
Return NotImplemented (not raise!) for foreign types and note why in a
comment.

Skills practiced:
- Operator overloading including __rmul__
- __eq__ and __abs__
- Returning NotImplemented for foreign types
"""

import math
from numbers import Real


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, Real):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self * scalar

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"


# Returning NotImplemented gives the other operand a chance to handle the
# operation. If neither operand supports it, Python raises a useful TypeError;
# for example, Vector(1, 2) * "x" is unsupported rather than producing a
# misleading vector of repeated strings.
