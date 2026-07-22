"""Exercise 12.3 — argparse subcommands (script; test via --help).

Rebuild the Phase 2 textstats driver as a CLI:
  argdemo.py words <file>
  argdemo.py chars <file> --ignore-case/--no-ignore-case
  argdemo.py longest <file> -n 5
Typed arguments (type=Path, type=int), helpful help texts, and a
-v/--verbose count flag. `python argdemo.py --help` must read like a real
tool.

Skills practiced:
- argparse subcommands and typed arguments
- Writing a helpful --help
"""

import argparse
import json
import logging
from collections.abc import Sequence
from pathlib import Path


logger = logging.getLogger(__name__)


def non_negative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be zero or greater")
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate useful statistics for a UTF-8 text file.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="increase logging detail; repeat for debug output",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    words = subparsers.add_parser("words", help="count whitespace-separated words")
    words.add_argument("file", type=Path, help="UTF-8 text file to analyze")

    chars = subparsers.add_parser("chars", help="count non-whitespace characters")
    chars.add_argument("file", type=Path, help="UTF-8 text file to analyze")
    chars.add_argument(
        "--ignore-case",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="combine uppercase and lowercase characters (default: enabled)",
    )

    longest = subparsers.add_parser("longest", help="show the longest words")
    longest.add_argument("file", type=Path, help="UTF-8 text file to analyze")
    longest.add_argument(
        "-n",
        type=non_negative_int,
        default=5,
        metavar="COUNT",
        help="number of words to show (default: 5)",
    )
    return parser


def configure_logging(verbosity: int) -> None:
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG
    logging.basicConfig(level=level, format="%(levelname)s %(message)s")


def character_frequencies(text: str, *, ignore_case: bool) -> dict[str, int]:
    if ignore_case:
        text = text.lower()
    frequencies: dict[str, int] = {}
    for character in text:
        if not character.isspace():
            frequencies[character] = frequencies.get(character, 0) + 1
    return frequencies


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)

    logger.info("Reading %s", args.file)
    try:
        text = args.file.read_text(encoding="utf-8")
    except OSError as error:
        parser.error(f"cannot read {args.file}: {error}")

    logger.debug("Read %d characters", len(text))
    if args.command == "words":
        print(len(text.split()))
    elif args.command == "chars":
        counts = character_frequencies(text, ignore_case=args.ignore_case)
        print(json.dumps(counts, ensure_ascii=False, sort_keys=True))
    elif args.command == "longest":
        longest = sorted(text.split(), key=len, reverse=True)[: args.n]
        print(*longest, sep="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
