#main
from maze import *
from controls import *
row_pos = 1
column_pos = 0
print_maze()
print("You are X!")
print("Can you get out of the maze?")
print("Use 'w', 'a', 's' and 'd' keys to move up, "+
      "left, down and right respectively!")
uin = input()
valid_inputs = ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D']
while row_pos != 28 and (not (column_pos in range(62, 67))):
    while not uin in valid_inputs:
        print("That is an invalid input, try again.")
        uin = input()
    valid = check_validity(uin, row_pos, column_pos)
    while not valid:
        print("You can't move in that direction, try again.")
        uin = input()
    execute_user_command(uin)
    for row in range(len(sample_maze)):
        for column in range(len(sample_maze[1])):
            if row == row_pos and column == column_pos:
                print("X", end = '')
            else: print(sample_maze[row][column], end = '')
        print()
    uin = input()
print("Congratulations! you did it!")