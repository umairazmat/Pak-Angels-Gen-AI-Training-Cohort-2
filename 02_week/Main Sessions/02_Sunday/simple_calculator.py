# Define functions for each operation
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
operation = input("Enter choice(1/2/3/4): ")

# Validate the operation input
if operation in ["1", "2", "3", "4"]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == "2":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "4":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")
