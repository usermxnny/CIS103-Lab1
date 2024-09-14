# CIS 103: Introduction to Programming
# Lab 2: "Building a Simple Calculator"
# Instructor: Md Ali
# Date: 09/14/2024

# This program adds, subtracts, multiplies, divides, and squares numbers using operators that combine two numbers.

# This function adds two numbers using the "+" operator
def add(x, y):
    return x + y

# This function subtracts two number using the "-" operator
def subtract(x, y):
    return x - y

# This function multiplies two numbers using the "*" operator
def multiply(x, y):
    return x * y

# This function divides two numbers using the "/" operator
def divide(x, y):
        return x / y

# This function squares two numbers using the "**" operator
def sqrt(x, y):
    return x ** y

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")

while True:
    # This takes input from the user
    choice = input("Enter choice(1, 2, 3, 4, 5,): ")

    # This checks if choice is one of five options
    if choice in ('1,' '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. PLease enter a number.")
            continue

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        print(num1, "**", num2, "=", sqrt(num1, num2))

    # This checks if user wants another calculation
    # This breaks the loop if answer is no
    next_calculation = input("Next calculation? (yes/no): ")
    if next_calculation == "no":
        break

else:
    print("Invalid Input")