
from maze import *
#Controls
#If the follow functions when executed by user lead
#cont'd>> x to be in an invalid position then an 
#cont'd>> "invalid action" message will be delivered
#cont'd>> to the user and they will be forced to do 
#cont'd>> something else until a valid action is 
#cont'd>> executed
def move_x_up(y_pos):
    y_pos -=1
    return y_pos
def move_x_down(y_pos):
    y_pos += 1
    return y_pos
def move_x_right(x_pos):
    x_pos += 1
    return x_pos
def move_x_left(x_pos):
    x_pos -= 1 
    return x_pos
def check_validity(uin, row_pos, column_pos):
    if uin == 'w' or uin == 'W':
        test_row = move_x_up(row_pos)
    elif uin == 's' or uin == 'S':
        test_row = move_x_down(row_pos)
    else: test_row = row_pos
    if uin == 'a' or uin == 'A':
        test_column = move_x_left(column_pos)
    elif uin == 'd' or uin == 'D':
        test_column = move_x_right(column_pos)
    else: test_column = column_pos
    return test_column in places_where_x_can_be[test_row] 
def execute_user_command(uin, row_pos, column_pos):
    if uin == 'w' or uin == 'W':
        return move_x_up(row_pos)
    if uin == 's' or uin == 'S':
        return move_x_down(row_pos)
    if uin == 'a' or uin == 'A':
        return move_x_left(column_pos)
    if uin == 'd' or uin == 'D':
        return move_x_right(column_pos)