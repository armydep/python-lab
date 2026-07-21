"""Tests for Phase 7. Skipped until you implement each exercise.

Skills practiced:
- Reading a pytest suite as the spec for phase 7 classes
"""

import dataclasses
from decimal import Decimal

import pytest

from money import Money
from vector import Vector
from temperature import Temperature
import shapes_abc


def test_money_add_same_currency():
    total = Money(Decimal("1.50"), "EUR") + Money(Decimal("2.50"), "EUR")
    assert total == Money(Decimal("4.00"), "EUR")


def test_money_add_cross_currency_raises():
    with pytest.raises(ValueError):
        Money(Decimal("1"), "EUR") + Money(Decimal("1"), "USD")


def test_money_comparison():
    assert Money(Decimal("1"), "EUR") < Money(Decimal("2"), "EUR")
    with pytest.raises(ValueError):
        Money(Decimal("1"), "EUR") < Money(Decimal("2"), "USD")


def test_money_is_frozen_and_hashable():
    m = Money(Decimal("1"), "EUR")
    with pytest.raises(dataclasses.FrozenInstanceError):
        m.amount = Decimal("2")
    prices = {m: "coffee"}
    assert prices[Money(Decimal("1"), "EUR")] == "coffee"


def test_vector_arithmetic():
    v, w = Vector(1, 2), Vector(3, 4)
    assert v + w == Vector(4, 6)
    assert w - v == Vector(2, 2)
    assert v * 3 == Vector(3, 6)
    assert 3 * v == Vector(3, 6)
    assert abs(Vector(3, 4)) == 5.0


def test_vector_foreign_type():
    with pytest.raises(TypeError):
        Vector(1, 2) * "x"


def test_temperature_conversions():
    t = Temperature(kelvin=300)
    assert t.celsius == pytest.approx(26.85)
    t.celsius = 100
    assert t.kelvin == pytest.approx(373.15)
    t.fahrenheit = 32
    assert t.celsius == pytest.approx(0.0)


def test_temperature_rejects_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(kelvin=-1)
    t = Temperature(kelvin=300)
    with pytest.raises(ValueError):
        t.celsius = -300
    with pytest.raises(ValueError):
        t.fahrenheit = -500


def test_shapes():
    shapes = [shapes_abc.Circle(1), shapes_abc.Rect(2, 3)]
    assert shapes_abc.total_area(shapes) == pytest.approx(3.14159265 + 6, rel=1e-6)


def test_shape_is_abstract():
    with pytest.raises(TypeError):
        shapes_abc.Shape()


def test_protocol_without_inheritance():
    class Napkin:  # satisfies Squarish structurally
        side = 0.3

    assert "0.3" in shapes_abc.describe_square(Napkin())


def test_car_delegates():
    from composition import Car, Engine

    car = Car()
    assert car.start() == "engine started"
    assert car.locate() == "(lat, lon)"
    assert not isinstance(car, Engine)  # composition, not inheritance
