
# Markmið að komast á reit 3,1
# Gera fall fyrir reiti

    # 1,1 - Bara hægt að fara Norður
    # 1,2 - Hægt að fara Norður, Austur og Suður
    # 1,3 - Hægt að fara Suður og Austur
    # 2,1 - Bara hægt að fara Norður
    # 2,2 - Hægt að fara Vestur og Suður
    # 2,3 - Hægt að fara Vestur og Austur
    # 3,1 - Bara hægt að fara Norður
    # 3,2 - Hægt að fara Norður og Suður
    # 3,3 - Hægt að fara Vestur og Suður

# í upphafi þarf að prenta út í hvaða átt er hægt að fara "You can travel: (N)orth".
# Ef hreyfing er ekki möguleg á að prentast út "Not a valid direction!" og biðja um nýja átt
# Þegar komið er á reit 3,1 prentast út "Victory!" og forrit klárast.
# Input frá leikmanni getur verið bæði hástafur eða lágstafur
# https://github.com/DanielGestur/Tile-Traveller/blob/master/TileTraveller.py

NORTH = "n" or "N"
EAST = "e" or "E"
SOUTH = "s" or "S"
WEST = "w" or "W"
# Column + row make one tile, our first tile is (1,1)
# COLUMN = 1
# ROW = 1


def possible_directions(column, row):
    ''' Check the position of the player and print out the valid direction that the player can go. '''
  
    
    if column == 1 and row == 1 :
        valid_directions = NORTH
        print("You can travel: (N)orth.")
    elif column == 1 and row == 2:
        valid_directions = NORTH + EAST + SOUTH
        print("You can travel: (N)orht or (E)ast or (S)outh.")
    elif column == 1 and row == 3:
        valid_directions = EAST + SOUTH
        print("You can travel: (E)ast or (S)outh.")
    elif column == 2 and row == 1: 
        valid_directions = NORTH
        print("You can travel: (N)orth.")
    elif column == 2 and row == 2: 
        valid_directions = SOUTH + WEST
        print("You can travel: (S)outh or (W)est.")
    elif column == 2 and row == 3: 
        valid_directions = EAST + WEST
        print("You can travel: (E)ast or (W)est.")      
    elif column == 3 and row == 2: 
        valid_directions = NORTH + SOUTH
        print("You can travel: (N)orth or (S)outh.")
    elif column == 3 and row == 3: 
        valid_directions = SOUTH + WEST
        print("You can travel: (S)outh or (W)est.")
    elif column == 3 and row == 1: 
        valid_directions = EAST + WEST
        victory = True
        return victory
    return valid_directions

<<<<<<< HEAD
def position(direction, column, row):
=======
def position(user_input, column, row,valid_directions):
>>>>>>> f37cea6189d169e6044213cef332b549019609ec
    ''' Changes the player position after play is chosen '''

    if user_input in valid_directions:  
     if user_input == NORTH:
        row += 1
     elif user_input == EAST:
        column += 1
     elif user_input == WEST:
        column -= 1
     elif user_input == SOUTH:
        row -= 1
<<<<<<< HEAD
    else:
        print("Not a valid direction!")
    return(column, row)

def victory(column, row):
    ''' The player has won the game '''
    if column == 3 and row == 1:
        print("Victory!")
=======
     return column ,row    
      
    if user_input != valid_directions:
        print("Not a valid direction!") 
        if row > 3 or row < 1: 
            if row > 3: 
              row -= 1 
            if row < 1: 
              row += 1   
            return column ,row
        else: 
         return column ,row
        if column > 3 or column < 1: 
            if column > 3:
              column -= 1 
            if column < 1: 
              column += 1    
            return column ,row
        else: 
         return column ,row
       
>>>>>>> f37cea6189d169e6044213cef332b549019609ec

def victory(victory):
    if column == 3 and row == 1:
        victory = True
        print("Victory!")
    else:
        victory = False    
    return victory      
column = 1
row = 1
<<<<<<< HEAD

while victory != True:
    valid_directions = possible_directions(column, row)
    user_input = input("Direction: ")
    #print(valid_directions)
    column, row =position(user_input, column, row)
    
if victory == True:
    victory(column, row)
=======

# valid_directions = NORTH
# possible_directions(column, row)


while victory(victory) != True:
    print(column,row)
    valid_directions = possible_directions(column, row)
    user_input = input("Direction: ")
    column ,row= position(user_input, column, row,valid_directions)
        


>>>>>>> f37cea6189d169e6044213cef332b549019609ec
