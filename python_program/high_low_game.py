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
Step 4: Play multiple rounds
Step 5: Score system
Step 6: Safeguard user input
Step 6: Customed message based on score
"""

import random

NUM_ROUNDS = 5

def main():
    print("+-------------------------------------------+")
    print("|       Welcome to the High-Low Game!       |")
    print("+-------------------------------------------+")
    score = 0

    # game start. for loop to prompt player to play multiple rounds
    for i in range(NUM_ROUNDS):
      player_num = random.randint(1, 100)
      computer_num = random.randint(1, 100)

      print(f"Round {i + 1}")
      print(f"Your number is {player_num}")

      choice = input("Your number is higher or lower?: ")

      while (choice != "lower" and choice != "higher"): # loop to ask for a correct input
          choice = input("Please enter either higher or lower: ")

      print("") # end of prompt phase new line

      if (choice == "lower" and player_num < computer_num 
          or choice == "higher" and player_num > computer_num):
          score += 1
          print(f"Correct! The computer's number was {computer_num}") 
      else:
          score -= 1
          print(f"Aww, incorrect. The computer's number was {computer_num}")
      
      print(f"Your score is now {score}") # notify score after each round
      print(f"---------------------------------------------") # end of round decoration line

    # end game prints start
    print("+-------------------------------------------+")
    if (score == 5):
        print("|        Wow! You played perfectly!         |")
    elif (score >= 1):
        print("|     Good job, you played really well!     |")
    else:
        print("|          Better luck next time!           |")
    print("+-------------------------------------------+")

if __name__ == "__main__":
    main()