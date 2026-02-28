#main
from maze import sample_maze,print_maze, places_where_x_can_be
import controls as ctr
row_pos = 1
column_pos = 0
print_maze()
print("You are X!")
print("Can you get out of the maze?")
print("Use 'w', 'a', 's' and 'd' keys to move up, "+
      "left, down and right respectively!")
uin = input()
vert_commands = ['w', 'W', 's', 'S']
hor_commands = ['a', 'd','A', 'D']
valid_inputs = ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D']
while not(row_pos == 29 and (column_pos in places_where_x_can_be[29])):
    while not uin in valid_inputs:
        print("That is an invalid input, try again.")
        uin = input()
    valid = ctr.check_validity(uin, row_pos, column_pos)
    while not valid:
        print("You can't move in that direction, try again.")
        uin = input()
        valid = ctr.check_validity(uin, row_pos, column_pos)
    if uin in vert_commands:
        row_pos = ctr.execute_user_command(uin, row_pos, column_pos)
    else: column_pos = ctr.execute_user_command(uin, row_pos, column_pos)
    for row in range(len(sample_maze)):
        for column in range(len(sample_maze[row])):
            if row == row_pos and column == column_pos:
                print("X", end = '')
            else: print(sample_maze[row][column], end = '')
        print()
    uin = input()
print("Congratulations! you did it!")