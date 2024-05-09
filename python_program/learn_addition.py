"""
File: learn_addition.py
-----------------------
Basic console game to teach user addition
"""

import random

def main():
    print("Welcome to learn addition")
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    print(f"What is {num1} + {num2}?")
    sum = int(input("Your answer: "))

    if (sum == num1 + num2):
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {num1 + num2}")
    
    
__name__ == '__main__' and main()