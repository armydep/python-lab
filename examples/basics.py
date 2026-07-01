"""Small examples of common Python basics."""


def main() -> None:
    numbers = [1, 2, 3, 4, 5]

    print("Numbers:", numbers)
    print("First number:", numbers[0])
    print("Total:", sum(numbers))
    print("Squares:", [number * number for number in numbers])

    age = 20
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

    for number in numbers:
        print(f"{number} doubled is {number * 2}")


if __name__ == "__main__":
    main()

