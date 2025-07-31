while True:
    # Ask for the first number
    num1 = float(input("Enter the first number: "))

    # Ask for the second number
    num2 = float(input("Enter the second number: "))

    # Ask for the operation
    operation = input("Enter an operation (+, -, *, /, %, **): ")

    # Perform the operation
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero.")
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("Error: Cannot divide by zero.")
    elif operation == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")
    else:
        print("Invalid operation. Please choose +, -, *, /, %, or **")

    # Ask if user wants to play again
    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thanks for using the calculator! Goodbye. 😊")
        break