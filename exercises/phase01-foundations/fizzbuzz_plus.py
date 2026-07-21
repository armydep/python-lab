"""Exercise 1.1 — FizzBuzz Plus.

Part A: Classic FizzBuzz for 1–100.
  - Multiples of 3 -> "Fizz", of 5 -> "Buzz", of both -> "FizzBuzz",
    otherwise the number itself.

Part B: Data-driven variant.
  - The rules live in a dict, e.g. {3: "Fizz", 5: "Buzz"}.
  - Adding a new rule (say 7: "Bazz") must require NO new `if` statement —
    only a new dict entry. Numbers matching several rules concatenate the
    words in ascending-divisor order (e.g. 15 -> "FizzBuzz", 21 -> "FizzBazz").

Check yourself: run Part B with {3: "Fizz", 5: "Buzz", 7: "Bazz"} and verify
105 prints "FizzBuzzBazz".

Skills practiced:
- Control flow with the modulo operator
- Replacing if/elif chains with a data-driven dict of rules
- String building and iteration over a range
"""

def classic_fizzbuzz(start: int = 1, stop: int = 100) -> list[str]:
    """Return classic FizzBuzz values from start through stop, inclusive.

    Rules:
      - multiples of 3 -> "Fizz"
      - multiples of 5 -> "Buzz"
      - multiples of both -> "FizzBuzz"
      - all other numbers -> the number as a string
    """
    answer: list[str] = []
    for number in range(start, stop + 1):
        match number:
            case n if n % 15 == 0:
                answer.append("FizzBuzz")
            case n if n % 3 == 0:
                answer.append("Fizz")
            case n if n % 5 == 0:
                answer.append("Buzz")
            case _:
                answer.append(str(number))

    return answer


def fizzbuzz_plus(
    start: int = 1,
    stop: int = 100,
    rules: dict[int, str] | None = None,
) -> list[str]:
    """Return data-driven FizzBuzz values from start through stop, inclusive.

    `rules` maps divisors to words, for example:
        {3: "Fizz", 5: "Buzz", 7: "Bazz"}

    Numbers matching several rules should concatenate the matching words in
    ascending-divisor order. Numbers matching no rules become the number as a
    string.
    """
    if rules is None:
        rules = {3: "Fizz", 5: "Buzz"}

    answer: list[str] = []
    for number in range(start, stop + 1):
        result = ""
        for divisor in sorted(rules):
            if number % divisor == 0:
                result += rules[divisor]

        if result:
            answer.append(result)
        else:
            answer.append(str(number))

    return answer



def print_lines(lines: list[str]) -> None:
    """Print one output value per line."""
    # TODO: print each item in `lines`.
    pass


def main() -> None:
    """Run both exercise parts."""
    # TODO: call classic_fizzbuzz() for Part A.
    # TODO: call fizzbuzz_plus(rules={3: "Fizz", 5: "Buzz", 7: "Bazz"}) for Part B.
    pass


if __name__ == "__main__":
    main()
