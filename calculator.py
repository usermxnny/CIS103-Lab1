print("CIS 103 - Calculator Lab")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice: ")

    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == '1':
        result = num1 + num2
        print(result) # addition
    elif choice == '2':
        result = num1 - num2
        print(result) # subtraction
    elif choice == '3':
        result = num1 * num2
        print(result) #multiplication
    elif choice == '4':
        result = num1 / num2
        print(result) #division
    else:
        print() #invalid

else:
    print(f"{operator} is not a valid operator")