"""
File: game_of_nimm.py
---------------------
Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.
"""

def main():
    print("The Ancient Game of Nimm")

    stones = 20
    current_player = 1

    while (stones > 0):
      next_player = current_player == 1 and 2 or 1
      print(f"There are {stones} stones left.")

      query = int(input(f"Player {current_player} would you like to remove 1 or 2 stones? "))

      while (query != 1 and query != 2):
        query = int(input(f"Player {current_player} please enter 1 or 2: "))

      stones -= query
      current_player = next_player

      if (stones <= 0):
         print(f"Player {next_player} wins!")

__name__ == '__main__' and main()