"""Tests for Phase 5. Skipped until you implement each exercise.

Skills practiced:
- Reading a pytest suite as the spec for phase 5 error handling
"""

import pytest

from safe_convert import to_int
from retry import RetryError, call_with_retry
import hierarchy


def test_to_int():
    assert to_int("42") == 42
    assert to_int("nope") is None
    assert to_int("nope", default=0) == 0
    assert to_int([1, 2]) is None  # TypeError path


def test_to_int_does_not_swallow_everything():
    class Evil(str):
        def __int__(self):
            raise KeyboardInterrupt

    # hack: int(Evil()) raises KeyboardInterrupt — must NOT be caught
    with pytest.raises(KeyboardInterrupt):
        to_int(Evil("boom"))


def make_flaky(fail_times, exc=OSError):
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] <= fail_times:
            raise exc(f"failure {calls['n']}")
        return "ok"

    flaky.calls = calls
    return flaky


def test_retry_succeeds_after_failures():
    flaky = make_flaky(2)
    assert call_with_retry(flaky, attempts=3) == "ok"
    assert flaky.calls["n"] == 3


def test_retry_exhausts_and_chains_cause():
    flaky = make_flaky(5)
    with pytest.raises(RetryError) as exc_info:
        call_with_retry(flaky, attempts=3)
    assert flaky.calls["n"] == 3
    assert isinstance(exc_info.value.__cause__, OSError)


def test_retry_does_not_retry_other_errors():
    flaky = make_flaky(5, exc=ValueError)
    with pytest.raises(ValueError):
        call_with_retry(flaky, attempts=3)
    assert flaky.calls["n"] == 1


def test_withdraw_ok():
    accounts = {"acc1": 100}
    assert hierarchy.withdraw(accounts, "acc1", 30) == 70
    assert accounts["acc1"] == 70


def test_withdraw_unknown_account():
    with pytest.raises(hierarchy.AccountNotFound) as exc_info:
        hierarchy.withdraw({"acc1": 100}, "ghost", 10)
    assert exc_info.value.account_id == "ghost"
    assert isinstance(exc_info.value, hierarchy.BankError)


def test_withdraw_insufficient():
    with pytest.raises(hierarchy.InsufficientFunds) as exc_info:
        hierarchy.withdraw({"acc1": 100}, "acc1", 130)
    assert exc_info.value.shortfall == 30
    assert isinstance(exc_info.value, hierarchy.BankError)
