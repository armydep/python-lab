"""Tests for Phase 4 (the package parts that are testable).

Skills practiced:
- Reading a pytest suite as the spec for the shapes package
"""

import math

import pytest

from shapes import area as unified_area
from shapes import circle, rectangle


def test_circle():
    assert circle.area(1) == pytest.approx(math.pi)
    assert circle.perimeter(2) == pytest.approx(4 * math.pi)


def test_rectangle():
    assert rectangle.area(2, 3) == 6
    assert rectangle.perimeter(2, 3) == 10


def test_unified_area_dispatch():
    assert unified_area("circle", radius=1) == pytest.approx(math.pi)
    assert unified_area("rectangle", width=2, height=3) == 6


def test_unified_area_unknown_shape():
    with pytest.raises(ValueError):
        unified_area("triangle", base=1, height=1)
