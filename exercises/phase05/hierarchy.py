"""Exercise 5.3 — designing an exception hierarchy.

BankError(Exception) is the base. InsufficientFunds carries `shortfall`;
AccountNotFound carries `account_id` (as attributes, with useful str()).

withdraw(accounts, account_id, amount) — accounts is a dict id -> balance:
  - unknown id -> AccountNotFound
  - amount > balance -> InsufficientFunds(shortfall=amount - balance)
  - otherwise mutate the balance and return the new balance

Write a demo caller (under __main__) handling each error differently and
printing the carried data.
"""


class BankError(Exception):
    pass


class InsufficientFunds(BankError):
    pass  # TODO: __init__ storing .shortfall + a useful message


class AccountNotFound(BankError):
    pass  # TODO: __init__ storing .account_id + a useful message


def withdraw(accounts, account_id, amount):
    raise NotImplementedError


if __name__ == "__main__":
    pass  # demo caller
