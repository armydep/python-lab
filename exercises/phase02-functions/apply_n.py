"""Exercise 2.6 — functions as values.

apply_n(func, value, times) applies func repeatedly: apply_n(double, 3, 2)
-> 12. Also write apply_n_recursive with the same behavior (base case:
times == 0 returns value). Try both with lambda x: x * 2 and str.upper.

Skills practiced:
- Passing functions as arguments
- Iterative vs recursive implementations
- Base case and recursion
"""


def apply_n(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def apply_n_recursive(func, value, times):
    if times == 0:
        return value

    val = apply_n_recursive(func, value, times - 1)
    return func(val)
