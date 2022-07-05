# Written 7/5/2022
# Day 10 Project of 100 Days of Code

# Program calculator that takes integers to perform simple calculations.
import calculator_art

print(calculator_art.logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {"+": add, "-": sub, "*": mult, "/": div}

def calculator():
    num1 = float(input("What is the first number?: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))
        calc = operations[operation_symbol]
        answer = calc(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type \'y\' to continue calculation with {answer}, or type \'n\' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()