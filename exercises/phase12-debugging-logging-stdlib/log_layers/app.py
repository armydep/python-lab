"""Exercise 12.2 — application-side logging (run: python app.py [-v]).

The ONLY place logging gets configured: basicConfig with a format showing
time, level, logger name, message; level WARNING by default, DEBUG with
-v. Call worker.do_work; catch its error with logger.exception and compare
the output with logger.error — paste both in comments.

Skills practiced:
- Configuring logging once at the entry point
- logger.exception and verbosity flags
"""

import argparse
import logging

import worker


logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Demonstrate layered logging")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="show debug and informational log messages",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    worker.do_work(4)
    try:
        worker.do_work(0)
    except ZeroDivisionError:
        logger.exception("Worker calculation failed")

        # logger.error("Worker calculation failed") prints only:
        # ERROR __main__ Worker calculation failed
        # logger.exception("Worker calculation failed") prints that message
        # plus the complete traceback for the active exception.


if __name__ == "__main__":
    main()
