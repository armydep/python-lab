"""Exercise 7.5 — composition vs inheritance.

Engine has start() -> "engine started"; GPS has locate() -> "(lat, lon)".
Car HAS an engine and a gps (composition) and DELEGATES:
car.start() -> "engine started", car.locate() -> "(lat, lon)".

Then, in comments (or a second class), sketch the inheritance version
Car(Engine) and write three concrete ways it's worse. See roadmap Phase 7.
"""


class Engine:
    def start(self):
        return "engine started"


class GPS:
    def locate(self):
        return "(lat, lon)"


class Car:
    def __init__(self):
        raise NotImplementedError


# Why Car(Engine) is worse:
# 1.
# 2.
# 3.
