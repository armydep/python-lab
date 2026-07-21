"""Exercise 5.3 — designing an exception hierarchy.

BankError(Exception) is the base. InsufficientFunds carries `shortfall`;
AccountNotFound carries `account_id` (as attributes, with useful str()).

withdraw(accounts, account_id, amount) — accounts is a dict id -> balance:
  - unknown id -> AccountNotFound
  - amount > balance -> InsufficientFunds(shortfall=amount - balance)
  - otherwise mutate the balance and return the new balance

Write a demo caller (under __main__) handling each error differently and
printing the carried data.

Skills practiced:
- Designing an exception class hierarchy
- Carrying data on exception instances
- Handling each subtype differently
"""


class BankError(Exception):
    pass


class InsufficientFunds(BankError):
    def __init__(self, shortfall):
        self.shortfall = shortfall
        super().__init__(f"Insufficient funds: shortfall of {shortfall}")


class AccountNotFound(BankError):
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Account not found: {account_id}")

def withdraw(accounts, account_id, amount):
    if account_id not in accounts:
        raise AccountNotFound(account_id)
    balance = accounts[account_id]
    if amount > balance:
        shortfall = amount - balance
        raise InsufficientFunds(shortfall)
    accounts[account_id] -= amount
    return accounts[account_id]


if __name__ == "__main__":
    demo_accounts = {"acc1": 100}
    for demo_id, demo_amount in [("acc1", 30), ("ghost", 10), ("acc1", 100)]:
        try:
            balance = withdraw(demo_accounts, demo_id, demo_amount)
            print(f"New balance: {balance}")
        except AccountNotFound as error:
            print(f"Unknown account: {error.account_id}")
        except InsufficientFunds as error:
            print(f"Insufficient funds; shortfall: {error.shortfall}")
