from calculatorart import logo
import os
def clear():
    os.system('clear')

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  if n1 > n2:
    return n1 - n2
  else:
    return n2 - n1

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  keep_calculating = True
  for key in operations:
     print(key)
  while keep_calculating:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calc_function = operations[operation_symbol]
    answer = calc_function(n1 = num1, n2 = num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ") == 'y':
      num1 = answer
    else:
      keep_calculating = False
      clear()
      calculator()

calculator()


