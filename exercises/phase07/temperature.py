"""Exercise 7.3 — properties with validation.

Temperature stores KELVIN internally. celsius and fahrenheit are
properties (both get and set). EVERY path — constructor and both setters —
rejects values below absolute zero (0 K) with ValueError. No duplicated
validation logic: one guard, used everywhere.

Temperature(kelvin=300).celsius ≈ 26.85; setting t.celsius = 100 updates
t.kelvin to 373.15 (kelvin must stay readable as t.kelvin).
"""


class Temperature:
    def __init__(self, kelvin):
        raise NotImplementedError
