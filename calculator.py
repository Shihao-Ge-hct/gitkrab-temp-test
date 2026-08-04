"""A simple command-line calculator for GitKrab diff testing."""


def print_separator():
    print("=" * 50)


def print_title():
    print_separator()
    print("Simple Python Calculator")
    print_separator()


def show_menu():
    print()
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Remainder")
    print("7. Average")
    print("8. Maximum")
    print("9. Minimum")
    print("10. Show history")
    print("0. Exit")
    print()


def read_number(message):
    while True:
        value = input(message).strip()

        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please try again.")


def read_positive_integer(message):
    while True:
        value = input(message).strip()

        try:
            number = int(value)

            if number > 0:
                return number

            print("The number must be greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def format_number(number):
    if number == int(number):
        return str(int(number))

    return str(round(number, 6))


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        return None

    return first / second


def power(first, second):
    return first ** second


def remainder(first, second):
    if second == 0:
        return None

    return first % second


def maximum(first, second):
    if first >= second:
        return first

    return second


def minimum(first, second):
    if first <= second:
        return first

    return second


def calculate_average():
    count = read_positive_integer("How many numbers? ")
    numbers = []

    for index in range(count):
        message = "Enter number " + str(index + 1) + ": "
        number = read_number(message)
        numbers.append(number)

    total = 0

    for number in numbers:
        total = total + number

    result = total / len(numbers)
    text_numbers = []

    for number in numbers:
        text_numbers.append(format_number(number))

    expression = "Average of " + ", ".join(text_numbers)

    return expression, result


def calculate_two_numbers(choice):
    first = read_number("Enter the first number: ")
    second = read_number("Enter the second number: ")

    if choice == "1":
        result = add(first, second)
        symbol = "+"
    elif choice == "2":
        result = subtract(first, second)
        symbol = "-"
    elif choice == "3":
        result = multiply(first, second)
        symbol = "*"
    elif choice == "4":
        result = divide(first, second)
        symbol = "/"

        if result is None:
            print("Error: cannot divide by zero.")
            return None, None
    elif choice == "5":
        result = power(first, second)
        symbol = "**"
    elif choice == "6":
        result = remainder(first, second)
        symbol = "%"

        if result is None:
            print("Error: cannot calculate remainder with zero.")
            return None, None
    elif choice == "8":
        result = maximum(first, second)
        symbol = "maximum of"
    elif choice == "9":
        result = minimum(first, second)
        symbol = "minimum of"
    else:
        print("Unknown operation.")
        return None, None

    first_text = format_number(first)
    second_text = format_number(second)

    if choice == "8" or choice == "9":
        expression = symbol + " " + first_text + " and " + second_text
    else:
        expression = first_text + " " + symbol + " " + second_text

    return expression, result


def show_result(expression, result):
    print()
    print("Calculation:")
    print(expression + " = " + format_number(result))
    print()


def show_history(history):
    print()
    print_separator()
    print("Calculation History")
    print_separator()

    if len(history) == 0:
        print("No calculations have been completed.")
        return

    number = 1

    for item in history:
        print(str(number) + ". " + item)
        number = number + 1


def main():
    history = []

    print_title()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print()
            print("Thank you for using the calculator.")
            break

        if choice == "10":
            show_history(history)
            continue

        if choice == "7":
            expression, result = calculate_average()
        elif choice in ["1", "2", "3", "4", "5", "6", "8", "9"]:
            expression, result = calculate_two_numbers(choice)
        else:
            print("Invalid choice. Please select a menu number.")
            continue

        if expression is not None and result is not None:
            show_result(expression, result)
            history_item = expression + " = " + format_number(result)
            history.append(history_item)


if __name__ == "__main__":
    main()