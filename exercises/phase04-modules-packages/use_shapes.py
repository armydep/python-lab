"""Exercise 4.1b — use the shapes package with three import styles:

1. import shapes
2. from shapes import circle
3. from shapes.rectangle import area as rect_area

Print one result per style. Note in comments what names each style brings
into scope.

Skills practiced:
- Import styles: import x, from x import y, and aliasing
- Which names each import style brings into scope
"""

# ``import shapes`` adds only the package name ``shapes`` here.
import shapes

# This adds the submodule name ``circle`` here.
from shapes import circle

# This adds only the alias ``rect_area`` here.
from shapes.rectangle import area as rect_area


print(shapes.area("circle", radius=2))
print(circle.perimeter(2))
print(rect_area(2, 3))
