"""
File: guess_my_number.py
------------------------
A simple guessing game using while loop
"""

import random

def main():
  print("I am thinking of a number between 1-100")

  number = random.randint(1, 100)
  guess = int(input("What's your guess? "))

  while (guess != number):
    if (guess > number):
      print("Your guess is too high")
    elif (guess < number):
      print("Your guess is too low")
    guess = int(input("Try again. What's your guess? "))

  print (f"You're right! The number is {number}")
  
__name__ == '__main__' and main()