def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers or an error message for division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def main():
    print("=== CodVeda Simple Calculator ===")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == "4":
        result = divide(num1, num2)
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid choice. Please run the program again and select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
