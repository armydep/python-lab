"""Exercise 7.3 — properties with validation.

Temperature stores KELVIN internally. celsius and fahrenheit are
properties (both get and set). EVERY path — constructor and both setters —
rejects values below absolute zero (0 K) with ValueError. No duplicated
validation logic: one guard, used everywhere.

Temperature(kelvin=300).celsius ≈ 26.85; setting t.celsius = 100 updates
t.kelvin to 373.15 (kelvin must stay readable as t.kelvin).

Skills practiced:
- @property getters and setters
- Centralised validation
- Internal representation vs public API
"""


class Temperature:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    @property
    def kelvin(self):
        """Return the temperature in kelvin."""
        return self._kelvin

    @kelvin.setter
    def kelvin(self, value):
        if value < 0:
            raise ValueError("temperature cannot be below absolute zero")
        self._kelvin = value

    @property
    def celsius(self):
        """Return the temperature in degrees Celsius."""
        return self.kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self.kelvin = value + 273.15

    @property
    def fahrenheit(self):
        """Return the temperature in degrees Fahrenheit."""
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.kelvin = (value - 32) * 5 / 9 + 273.15

    def __repr__(self):
        return f"Temperature(kelvin={self.kelvin!r})"
