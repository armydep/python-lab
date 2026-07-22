"""Exercise 12.2 — library-side logging.

This module is the 'library': logger = logging.getLogger(__name__), NEVER
basicConfig here. Give do_work() a few logger.debug/info/warning calls and
one operation that raises; catch it in app.py.

Skills practiced:
- Library-side logging with getLogger(__name__)
- Never configuring logging inside a library
"""

import logging

logger = logging.getLogger(__name__)


def do_work(n: int) -> float:
    """Divide 100 by *n*, logging progress without configuring handlers."""
    logger.debug("Starting work with n=%d", n)

    if n == 0:
        logger.warning("n is zero; the calculation will fail")

    logger.info("Calculating 100 divided by %d", n)
    result = 100 / n
    logger.info("Work completed successfully")
    logger.debug("Calculation result: %f", result)
    return result
