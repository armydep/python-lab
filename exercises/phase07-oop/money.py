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
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("cannot add money in different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("cannot compare money in different currencies")
        return self.amount < other.amount

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"
