"""
File: first_person_karel.py
---------------------------
Imagine you are a robot, wandering about a nice rectangular world, not a worry in the world, just moving and turning left whenever you'd like. All you can do is moving and turning left. Number of columns and rows in the "world" stored as constants, and you start in row 1 column 1 facing East. User is prompted for an action ("move" or "turn left").
"""

N_COLS = 3
N_ROWS = 3

def main():
    cur_row = 1
    cur_col = 1
    cur_dir = "East"
    print(f"Welcome to first person Karel! You're at row {cur_row}, column {cur_col}, facing {cur_dir} (facing column 3)")
    user_input = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    while user_input != "":
        if user_input == "move":
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
            pass
        else:
            print("Wrong command. Try 'move' or 'turn left'")

        user_input = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    
    print(f"You've ended up at row {cur_row} and column {cur_col} facing {cur_dir}.")


if __name__ == '__main__':
    main()