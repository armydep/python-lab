"""Exercise 5.4 — predict-then-run (script, no test).

Write functions with `return` in try, in except, and in finally. BEFORE
running, predict each result in comments; then run and record actuals.
Establish: when does finally run? What does a return in finally do to the
in-flight return/exception (and why do style guides forbid it)?

Skills practiced:
- try/except/else/finally execution order
- Why a return inside finally is dangerous
"""

# Predictions before running:
# 1. A return in try waits for finally; the function then returns "try".
# 2. A return in except also waits for finally, then returns "except".
# 3. A return in finally replaces the pending return from try with "finally".
# 4. A return in finally also suppresses a pending exception.


def return_in_try():
    try:
        return "try"
    finally:
        print("finally after try return")


def return_in_except():
    try:
        raise ValueError("problem")
    except ValueError:
        return "except"
    finally:
        print("finally after except return")


def return_in_finally():
    try:
        return "try"
    finally:
        return "finally"


def exception_hidden_by_finally():
    try:
        raise ValueError("this error is lost")
    finally:
        return "finally"


# Actual results matched the predictions. A finally block always runs as the
# try statement exits, including during a return or exception. Returning from
# finally is forbidden by style guides because it silently replaces an earlier
# return and can hide an exception that should have reached the caller.


if __name__ == "__main__":
    print("return_in_try:", return_in_try())
    print("return_in_except:", return_in_except())
    print("return_in_finally:", return_in_finally())
    print("hidden_exception:", exception_hidden_by_finally())
