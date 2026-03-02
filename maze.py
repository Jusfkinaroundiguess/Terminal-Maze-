sample_maze = [
       "_________________________________________________________________________",
       "                                                                         |",
       "_________________       ______________________________     ______________|",
       "|                |     |                              |    |             |",
       "|                |     |                              |    |             |",
       "|                |     |______________________________|    |             |",
       "|                |                                         |             |",
       "|                |      ______________________________     |             |",
       "|                |     |                              |    |             |",
       "|                |     |                              |    |             |",
       "_________________|     |______________________________|    |_____________|",
       "|                                                                        |",
       "|______     _____       ________________________________________      ___|",
       "|      |   |     |     |                                        |    |   |",
       "|      |   |     |     |                                        |    |   |",
       "|      |   |     |     |                                        |    |   |", 
       "|      |   |     |     |                                        |    |   |",
       "|      |   |_____|     |________________________________________|    |   |",
       "|      |                                                             |   |",
       "|      |____________________________        _________________________|   |", 
       "|                                   |      |                             |",
       "|                                   |      |                             |",
       "|___________________________________|      |_____________________________|",
       "|                                                                        |",
       "|__________       _______________________________________________________|",
       "|          |     |                                                       |",
       "|          |     |                                                       |",
       "|__________|     |_______________________________________________________|",
       "|                                                                        |",
       "|___________________________________________________     ________________|"
       ]

places_where_x_can_be = {}
for i in range(30):
       places_where_x_can_be[i] = []
for index in range(len(sample_maze)):
       if "|" in sample_maze[index][1:73]:
              flag = False 
              for i in range(1,73):
                     if sample_maze[index][i] == '|':
                            flag = not flag
                     if flag and sample_maze[index][i] == ' ':
                            places_where_x_can_be[index].append(i)
                                   
       else:
              for i in range(1, 73):
                     if sample_maze[index][i] == ' ':
                            places_where_x_can_be[index].append(i)
print(places_where_x_can_be)
                                   
def print_maze():
       initial_row_pos_of_x = 1
       initial_column_pos_of_x = 0 
       print("\n")
       for row in range(len(sample_maze)):
              for column in range(len(sample_maze[row])):
                     if row == initial_row_pos_of_x and column == initial_column_pos_of_x:
                            print("x", end = '')
                     else: print(sample_maze[row][column], end = '')
              print()
              
print_maze()
