"""
File: learn_addition.py
-----------------------
Basic console game to teach user addition
"""

import random


def main():
    print("Welcome to learn addition")

    streak = 0
    while (streak < 3):
      num1 = random.randint(10, 99)
      num2 = random.randint(10, 99)
      print(f"What is {num1} + {num2}?")
      sum = int(input("Your answer: "))

      if (sum == num1 + num2):
          streak += 1
          print("Correct!")
          print(f"You've gotten {streak} correct in a row")
      else:
          streak = 0
          print("Incorrect.")
          print(f"The expected answer is {num1 + num2}")

    print("Congratulations! You mastered addition.")
      

    
    
__name__ == '__main__' and main()