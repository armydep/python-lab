"""Exercise 7.1 — immutable Money.

A frozen dataclass: amount (Decimal), currency (str).
- Money + Money works only within one currency; across -> ValueError.
- Comparison (<, <=, ...) also within one currency only.
- Nice __repr__, e.g. Money(Decimal('9.99'), 'EUR').
- Being frozen, it's hashable — usable as a dict key.

Skills practiced:
- frozen dataclasses
- Operator dunders (__add__, __lt__)
- Immutability and hashability; Decimal
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __add__(self, other):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError
