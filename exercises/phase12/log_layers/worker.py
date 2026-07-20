"""Exercise 12.2 — library-side logging.

This module is the 'library': logger = logging.getLogger(__name__), NEVER
basicConfig here. Give do_work() a few logger.debug/info/warning calls and
one operation that raises; catch it in app.py.
"""

import logging

logger = logging.getLogger(__name__)


def do_work(n):
    raise NotImplementedError
