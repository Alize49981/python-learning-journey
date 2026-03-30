def calculator():
    print("Simple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator")

    except ValueError:
        print("Error: Please enter valid numbers")

calculator()
while True:
    calculator()
    
    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break