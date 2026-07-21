"""Exercise 4.1 — the shapes package.

Expose a unified area(shape_name, **dims) here that dispatches to the
submodules: area("circle", radius=2), area("rectangle", width=2, height=3).
Unknown shape -> ValueError. Then use the package from an outside script
with three different import styles (record them in use_shapes.py).

Skills practiced:
- Defining a package's public API in __init__.py
- Dispatching across submodules
- **kwargs
"""

from . import circle, rectangle


_AREA_FUNCTIONS = {
    "circle": circle.area,
    "rectangle": rectangle.area,
}


def area(shape_name, **dims):
    """Return the area of a named shape using the supplied dimensions."""
    try:
        area_function = _AREA_FUNCTIONS[shape_name]
    except KeyError:
        raise ValueError(f"unknown shape: {shape_name}") from None
    return area_function(**dims)


__all__ = ["area", "circle", "rectangle"]
