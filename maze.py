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

places_where_x_can_be = {
       0:[],
       1:[], 
       2:[],
       3:[],
       4:[],
       5:[],
       6:[],
       7:[],
       8:[],
       9:[],
       10:[],
       11:[],
       12:[],
       13:[],
       14:[],
       15:[],
       16:[],
       17:[],
       18:[],
       19:[],
       20:[],
       21:[],
       22:[],
       23:[],
       24:[], 
       25:[],
       26:[],
       27:[],
       28:[],
       29:[]
       }


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
                            
def print_line(no_hor, start_hor, end_hor, no_vert, vert_pos):
       pass
def print_spaces(index):
       for i in range(index):
              print(" ", end = '') 
def print_underscores(index):
       for i in range(index):
              print("_", end = '')
def print_horizontal_path(start, end, branches_up, branches_down):
       pass
def print_vert_paths(length, number, roof, floor): 
       #use roof or floor = -1 to indicate lack thereof
       pass
def print_vert_paths_after_first_line():#put in module
       print("|", end = '')
       print_spaces(17)
       print("|", end = '')
       print_spaces(5)
       print("|", end = '')
       print_spaces(30)
       print("|", end = '')
       print_spaces(4)
       print("|", end = '')
       print_spaces(13)
       print("|")
def connecting_first_two_branches(roof=False, passthrough=False): #Creates passage between two 
       #vertical branches of first path (roof and floor)
       #Use argument true if roof
       print("|", end = '')
       if not passthrough:
              print_spaces(17)
       else: print_underscores(17)
       print("|", end = '')
       
       print_spaces(5)

       if not roof:
              print(" ", end = '')
       if roof:
              print("|", end = '')
       print_underscores(30)
       if roof:
              print("|", end = '')
       print_spaces(4)

       if not roof:
              print(" ", end = '')
       print("|", end = '')
       if not passthrough:
              print_spaces(13)
       else: print_underscores(13)
       print("|")
def three_vert_diverge_from_passthrough(roof):
       print("|", end = '')
       print_underscores(6)
       print_spaces(5) #new branch diverging from this horizontal passthrough
       print_underscores(6)
       print_spaces(7) #Continuing original vertical branch from Original horizantal entry
       print_underscores(40) #blocks off second vertical branch from original horizontal entry
       print_spaces(6) #new vertical branch diverging
       print_underscores(3)
       print("|")
       
def print_maze():
       print("\n")
       for i in range(74): #prints upper wall of maze 
              print("_", end = '')
       print()
       #first road
       print("x", end = '')
       print_spaces(73)
       print("|")
       print_underscores(18)
       print_spaces(7) #path diverges (one branch)
       print_underscores(30)
       print_spaces(5) #path diverges (one branch)
       print_underscores(14)
       print("|")
       #end of line
       for i in range(2):
              print_vert_paths_after_first_line() #two branches of original path continue
       #end of line x2
       connecting_first_two_branches(True)
       #end of line
       print("|", end = '')
       print_spaces(17)
       print("|", end = '')
       print_spaces(41) #two branches of original path connected
       print("|", end = '')
       print_spaces(13)
       print("|")
       #end of line
       connecting_first_two_branches()
       #end of line
       for i in range(2):
              print_vert_paths_after_first_line()
       #end of line x2
       connecting_first_two_branches(True, True)
       #end of line
       print("|", end = '')
       print_spaces(73)
       print("|")
       #end of line
       print("|", end = '')
       print_underscores(6)
       print_spaces(5) #new branch diverging from this horizontal passthrough
       print_underscores(6)
       print_spaces(7) #Continuing original vertical branch from Original horizantal entry
       print_underscores(40) #blocks off second vertical branch from original horizontal entry
       print_spaces(6) #new vertical branch diverging
       print_underscores(3)
       print("|")
       #end of line
       for i in range(4):
              print("|", end = '')
              print_spaces(6)
              print("|", end = '')
              print_spaces(4)
              print("|", end = '')
              print_spaces(5)
              print("|", end = '')
              print_spaces(5) 
              print("|", end = '')
              print_spaces(40) 
              print("|", end = '')
              print_spaces(4) 
              print("|", end = '')
              print_spaces(3)
              print("|")
       #end of line x4
       print("|", end = '')
       print_spaces(6)
       print("|", end = '')
       print_spaces(4)
       print("|", end = '')
       print_underscores(5)
       print("|", end = '')
       print_spaces(5) 
       print("|", end = '')
       print_underscores(40) 
       print("|", end = '')
       print_spaces(4) 
       print("|", end = '')
       print_spaces(3)
       print("|")
       #end of line      
       print("|", end = '')
       print_spaces(6)
       print("|", end = '')
       print_spaces(62)
       print("|", end = '')
       print_spaces(3)
       print("|")
       #end of line
       print("|", end = '')
       print_spaces(6)
       print("|", end = '')
       print_underscores(28)
       print_spaces(8)
       print_underscores(26)
       print("|", end = '')
       print_spaces(3)
       print("|")
       #end of line
       for i in range(2):
              print("|", end = '')
              print_spaces(35)
              print("|", end = '')
              print_spaces(6)
              print("|", end = '')
              print_spaces(30)
              print("|")
       #end of line x2
       print("|", end = '')
       print_underscores(35)
       print("|", end = '')
       print_spaces(6)
       print("|", end = '')
       print_underscores(30)
       print("|")
       #end of line
       print("|", end = '')
       print_spaces(73)
       print("|")
       #end of line
       print("|", end = '')
       print_underscores(10)
       print_spaces(7)
       print_underscores(74-18)
       print("|")
       #end of line
       print("|", end = '')
       print_spaces(10)
       print("|", end = '')
       print_spaces(5)
       print("|", end = '')
       print_spaces(74-18)
       print("|")
       #end of line
       print("|", end = '')
       print_underscores(10)
       print("|", end = '')
       print_spaces(5)
       print("|", end = '')
       print_underscores(74-18)
       print("|")
       #end of line 
       print("|", end = '')
       print_spaces(73)
       print("|")
       #end of line (last line ahead!)
       print("|", end = '')
       print_underscores(52)
       print_spaces(5)
       print_underscores(16)
       print("|")
print_maze()