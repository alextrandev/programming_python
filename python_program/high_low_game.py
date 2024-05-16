"""
File: high_low_game.py
----------------------
The high low game goes as follows:
- Two numbers are generated from 1 to 100 (inclusive on both ends): one for player and one for an opponent computer.
- Player make a guess, saying their number is either higher than or lower than the computer's number.
- If their guess matches the truth, they get a point!
These steps make up one round of the game. The game is over after all rounds have been played.

Step 1: Generate the random numbers, print it out to test logic on later steps
Step 2: Get user choice
Step 3: Write the game logic
"""

import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    player_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)
    print(f"Your number is {player_num}")
    print(f"Computer's number is {computer_num}")

    choice = input("Do you think your number is higher or lower than the computer's?: ")

    if (choice == "lower" and player_num < computer_num 
        or choice == "higher" and player_num > computer_num):
        print(f"You were right! The computer's number was {computer_num}") 
    elif (choice == "lower" or choice == "higher"):
        print(f"Aww, that's incorrect. The computer's number was {computer_num}")
    else:
        print(f"Wrong input. Please type 'higher' or 'lower'")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()