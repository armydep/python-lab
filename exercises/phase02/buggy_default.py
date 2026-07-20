"""Exercise 2.5 — the mutable default argument bug (demo script, no test).

1. Write append_buggy(x, acc=[]) — the classic bug. Call it three times with
   no acc argument and print the (surprising) results.
2. Write append_fixed(x, acc=None) using the None idiom; same three calls.
Keep BOTH versions with comments explaining exactly when the default is
evaluated and why the buggy one shares state.
"""

def append_buggy(x, acc=[]):
    """Append x to acc and return acc.

    Bug: the default [] is created once, when this function is defined.
    Every call that omits acc reuses that same list.
    """
    acc.append(x)
    return acc


def append_fixed(x, acc=None):
    """Append x to acc and return acc.

    Fix: None is used as a sentinel. A new list is created during each call
    that omits acc, so separate calls do not share state.
    """
    if acc is None:
        acc = []

    acc.append(x)
    return acc

if __name__ == "__main__":
    print("buggy:")
    print(append_buggy(1))
    print(append_buggy(2))
    print(append_buggy(3))

    print("fixed:")
    print(append_fixed(1))
    print(append_fixed(2))
    print(append_fixed(3))
