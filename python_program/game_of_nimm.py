"""
File: game_of_nimm.py
---------------------
Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.
"""

def main():
    print("The Ancient Game of Nimm")

    stones = 20

    while (stones > 0):
      print(f"There are {stones} stones left.")

      query = int(input("Would you like to remove 1 or 2 stones? "))

      while (query != 1 and query != 2):
        query = int(input("Please enter 1 or 2: "))

      stones -= query
      if (stones <= 0):
         print("Game over")

__name__ == '__main__' and main()