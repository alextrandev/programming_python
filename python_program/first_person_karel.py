"""
File: first_person_karel.py
---------------------------
Imagine you are a robot, wandering about a nice rectangular world, not a worry in the world, just moving and turning left whenever you'd like. All you can do is moving and turning left. Number of columns and rows in the "world" stored as constants, and you start in row 1 column 1 facing East. User is prompted for an action ("move" or "turn left").
"""

# define world size
N_COLS = 3
N_ROWS = 3

def main():
  # define current row, collumn and direction. Direction can be East, West, North, South
  cur_row = 1
  cur_col = 1
  cur_dir = "East"

  # welcome message
  print(f"Welcome to first person Karel! You're at row {cur_row}, column {cur_col}, facing {cur_dir} (facing column 3)")

  # first input prompt
  user_input = input("What would you like to do? You can move and turn left. Press enter to finish. ")

  # loop the game until user input empty string.
  # acceptable input are move and turn_left
  while user_input != "":
    if user_input == "move":
      # change position based on current direction
      # e.g: if face north and move, the current row should increase by 1
      # the if statement is to check if the Karel is at the edge of the world
      match cur_dir:
        case "East" if cur_col < N_COLS:
          cur_col += 1
          print(f"You moved one step forward and now you're at row {cur_row} column {cur_col}.")
        case "West" if cur_col > 1:
          cur_col -= 1
          print(f"You moved one step forward and now you're at row {cur_row} column {cur_col}.")
        case "North" if cur_row < N_ROWS:
          cur_row += 1
          print(f"You moved one step forward and now you're at row {cur_row} column {cur_col}.")
        case "South" if cur_row > 1:
          cur_row -= 1
          print(f"You moved one step forward and now you're at row {cur_row} column {cur_col}.")
        case _:
          print("You can't move forward!")
    elif user_input == "turn left":
      # just a simple direction change
      match cur_dir:
        case "East":
          cur_dir = "North"
        case "West":
          cur_dir = "South"
        case "North":
          cur_dir = "West"
        case "South":
          cur_dir = "East"
      print(f"You turned left and are now facing {cur_dir}.")
    # this else is for wrong input
    else:
      print("Wrong command. Try 'move' or 'turn left'")

    # continue prompt user until they input empty string
    user_input = input("What would you like to do? You can move and turn left. Press enter to finish. ")

  # print final location before terminate
  print(f"You've ended up at row {cur_row} and column {cur_col} facing {cur_dir}.")

__name__ == '__main__' and main()