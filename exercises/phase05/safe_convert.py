"""Exercise 5.1 — narrow exception handling.

to_int(s, default=None): convert or return default — catching ONLY
ValueError and TypeError. A list argument hits the right path; broader
exceptions (KeyboardInterrupt!) must not be swallowed.
"""


def to_int(s, default=None):
    raise NotImplementedError
