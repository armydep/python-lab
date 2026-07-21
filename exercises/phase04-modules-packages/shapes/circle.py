"""Circle geometry. Use math.pi.

Skills practiced:
- Module-level functions
- Using math.pi
"""

import math


def area(radius):
    """Return the area of a circle with the given radius."""
    return math.pi * radius ** 2


def perimeter(radius):
    """Return the circumference of a circle with the given radius."""
    return 2 * math.pi * radius
