
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

def possible_directions(column, row):
    ''' Check the position of the player and print out the valid direction that the player can go. '''
  
    if column == 1 and row == 1 :
        valid_directions = NORTH
        print("You can travel: (N)orth.")
    elif column == 1 and row == 2:
        valid_directions = NORTH + EAST + SOUTH
        print("You can travel: (N)orth or (E)ast or (S)outh.")
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
        valid_directions = NORTH
    return valid_directions

def position(direction, column, row):
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
    else:
        print("Not a valid direction!")
    return(column, row)

def victory(column, row):
    ''' The player has won the game '''
    if column == 3 and row == 1:
        victory_ = True
        print("Victory!")
        return victory_
    
column = 1
row = 1

victory_ = False
while victory_ != True:
    valid_directions = possible_directions(column, row)
    user_input = input("Direction: ")
    column, row = position(user_input, column, row)
    victory(column, row)
    if (column == 3) and (row == 1):
        victory_ = True
    

