from maze import places_where_x_can_be
#Controls
#if the follow functions when executed by user lead
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
    #this function makes sure x cannot run into a wall
    #or go to an invalid position
    if uin == 'w':
        test_row = move_x_up(row_pos)
    elif uin == 's':
        test_row = move_x_down(row_pos)
    else: test_row = row_pos
    if uin == 'a':
        test_column = move_x_left(column_pos)
    elif uin == 'd':
        test_column = move_x_right(column_pos)
    else: test_column = column_pos
    return test_column in places_where_x_can_be[test_row] 
def execute_user_command(uin, row_pos, column_pos):
    if uin == 'w':
        return move_x_up(row_pos)
    if uin == 's':
        return move_x_down(row_pos)
    if uin == 'a':
        return move_x_left(column_pos)
    if uin == 'd':
        return move_x_right(column_pos)