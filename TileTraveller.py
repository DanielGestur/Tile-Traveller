
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

# def first_location():
#     location = (1,1)
#     return location

def possible_directions(col, row):
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def direction():
    direction_input = input("Directions: ")
    return direction_input

def position():
    pass

def victory():
    pass

while not victory():
    location = (1,1)