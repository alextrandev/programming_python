"""
File: input.py
--------------
Prompt user to choose an action, take inputs and return something.
Current actions: Sum and multiply of 2 numbers, dice roll, greeting
"""

import random

def main():
  prompt = ""
  while (prompt != "exit"):
    prompt = input("Type sum, multiply, hello, dice or FtoC. Type exit to end the program: ")
    match prompt:
      case "sum":
        sum()
      case "multiply":
        multiply()
      case "hello":
        hello()
      case "dice":
        dice()
      case "FtoC":
        f_to_c()
      case "exit":
        print("Goodbye!")
      case _:
        print("Wrong command, try again!")

def sum():
  print("Calculate the sum of 2 numbers")
  num1 = input("Enter first number: ")
  num1 = int(num1)
  num2 = input("Enter second number: ")
  num2 = int(num2)
  total = num1 + num2
  print(f"Result: {num1} + {num2} = {total}")

def hello():
  name = input("What is your name? ")
  print(f"Hello {name}!")

def multiply():
  print("Calculate the multiply of 2 numbers")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  total = num1 * num2
  print(f"Result: {num1} x {num2} = {total}")

def dice():
  dice = int(input("What is the number of sides on your dice? "))
  roll = random.randint(1, dice)
  print(f"Your roll is {roll}")

def f_to_c():
    f_temp = float(input("Enter temperature in Fahrenheit: "))
    c_temp = (f_temp - 32) * 5.0/9.0
    print(f"Temperature: {f_temp}F = {c_temp}C")

# call the main funtion
__name__ == '__main__' and main()