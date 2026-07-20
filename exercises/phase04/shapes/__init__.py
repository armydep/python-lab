"""Exercise 4.1 — the shapes package.

Expose a unified area(shape_name, **dims) here that dispatches to the
submodules: area("circle", radius=2), area("rectangle", width=2, height=3).
Unknown shape -> ValueError. Then use the package from an outside script
with three different import styles (record them in use_shapes.py).
"""


def area(shape_name, **dims):
    raise NotImplementedError
