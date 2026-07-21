"""Exercise 7.2 — a 2D Vector with operator dunders.

Support: v + w, v - w, v * 3 AND 3 * v (__rmul__), abs(v) (magnitude),
v == w, readable __repr__. Predict-then-run: what happens for v * "x"?
Return NotImplemented (not raise!) for foreign types and note why in a
comment.

Skills practiced:
- Operator overloading including __rmul__
- __eq__ and __abs__
- Returning NotImplemented for foreign types
"""


class Vector:
    def __init__(self, x, y):
        raise NotImplementedError
