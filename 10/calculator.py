from art import logo
from os import system, name

def clear():
  if name == "nt":
    _ = system('cls')
  else:
    _ = system('clear')

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
            print(symbol)
    
    should_continue = True

    while should_continue:

        chosen_operation = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        result = 0

        calculate = operations[chosen_operation]

        result = calculate(num1, num2)

        clear()
            
        print(f"{num1} {chosen_operation} {num2} = {result}")

        answer = input(f"Type 'y' to continue calculating with {result}, type 'n' to exit, or type 's' to start a new calulator: ")

        if answer == 'n':
            clear()
            should_continue = False
        elif answer == 's':
            clear()
            calculator()
        else:
            num1 = result

calculator()