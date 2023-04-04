# import module
import os
from calculator import calc

# 1. Add Calculator Functions
# Add 
def add(n1, n2):
    return n1 + n2

# Subtrack
def subtract(n1, n2):
    return n1 - n2

# Multiply 
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# 2. Create a dictionary named operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(calc.logo)
    
    # input number 1
    num1 = float(input("What is the first number?: "))

    # print operations to console
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        # input operation symbol to cosole
        operation_symbol = input("Pick an operation: ")

        # input number 2
        num2 = float(input("What is the next number?: "))

        # print first result 
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        # ask for continue or stop
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system('clear')
            calculator()           # 만약 continue가 False인 경우 내가 만든 함수를 다시 재사용 (a.k.a 재귀)
            
calculator()