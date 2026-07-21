"""Exercise 7.5 — composition vs inheritance.

Engine has start() -> "engine started"; GPS has locate() -> "(lat, lon)".
Car HAS an engine and a gps (composition) and DELEGATES:
car.start() -> "engine started", car.locate() -> "(lat, lon)".

Then, in comments (or a second class), sketch the inheritance version
Car(Engine) and write three concrete ways it's worse. See roadmap Phase 7.

Skills practiced:
- Composition and delegation
- Composition vs inheritance trade-offs
"""


class Engine:
    def start(self):
        return "engine started"


class GPS:
    def locate(self):
        return "(lat, lon)"


class Car:
    def __init__(self):
        self.engine = Engine()
        self.gps = GPS()

    def start(self):
        return self.engine.start()

    def locate(self):
        return self.gps.locate()


# Why Car(Engine) is worse:
# 1. A car has an engine; it is not substitutable for an engine everywhere.
# 2. It exposes all public Engine behavior even when Car should hide/control it.
# 3. Replacing Engine with another implementation requires changing inheritance,
#    while composition only requires supplying a different engine object.
