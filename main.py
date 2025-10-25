# A simple calculator program in Python

def calculator():
    print("Welcome to the Python Calculator!")
    print("Operations: +, -, *, /")

    while True:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Invalid operator. Try again.")
            continue

        print(f"The result is: {result}")

        # Ask if the user wants to continue
        choice = input("Do you want to calculate again? (yes/no): ").lower()
        if choice != 'yes':
            print("Goodbye!")
            break

# Run the calculator
calculator()
