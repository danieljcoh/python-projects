

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate():
    while True:
        num1 = input("Enter a number: ")
        if not num1.isdigit():
            print("Please enter a number! \n")
            continue
        num2 = input("Enter a second number: ")
        if not num2.isdigit():
            print("Please enter a number! \n")
            continue
        break

    x = int(num1)
    y = int(num2)


    operation = input("Which operation do you want to do? (+, -, *, /): ")
    if operation == "+":
        print(add(x, y))
    elif operation == "-":
        print(subtract(x, y))
    elif operation == "*":
        print(multiply(x, y))
    elif operation == "/":
        print(divide(x, y))
    else:
        print("I don't recognize that command!")


calculate()


