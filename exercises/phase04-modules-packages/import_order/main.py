"""Import mod_a and mod_b in different orders, then import each AGAIN.
Record in comments: what printed, what didn't, and the sys.modules
explanation.

Skills practiced:
- sys.modules caching
- How import order affects side effects
"""

import mod_a
import mod_b

# Import the same modules again, this time in the opposite order.
import mod_b
import mod_a

# Observations:
# Output:
# importing mod_a
# importing mod_b
#
# The first two imports print in the order in which they execute. The second
# pair prints nothing: after loading a module, Python stores its module object
# in sys.modules. A later import finds and reuses that cached object instead of
# executing the module's top-level code again. Changing the later import order
# therefore has no visible effect.
