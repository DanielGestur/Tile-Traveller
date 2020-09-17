
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

def first_location():
    location = (1,1)
    return location

def possible_directions():
    if position() == (1,1) or (2,1) or (3,1) or (1,2) or (3,2):
        if direction() == "n" or "N":
            print("(N)orth")
    elif position() == (1,2) or (2,2) or (3,2) or (1,3) or (3,3):
        if direction() == "s" or "S":
            print("(S)outh")
    elif position() == (1,3) or (3,2) or (1,2):
        if direction() == "e" or "E":
            print("(E)ast")
    elif position() == (3,3) or (2,3) or (2,2):
        if direction() == "w" or "W":
            print("(W)est")
    return possible_directions

def direction():
    direction_input = input("Directions: ")
    return direction_input

def position():
    pass

def victory():
    pass