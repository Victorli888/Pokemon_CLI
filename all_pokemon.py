import Actions

class Pokemon:
    # init needed  variables for Poke dex
    def __init__(self, name, region, poke_type, level):
        self.name = name
        self.region = region
        self.poke_type = poke_type
        self.level = level



    # Use variables and print string to describe pokemon
    def pokedex(self):
        Actions.tap()
        print(f"This Pokemon is called {self.name} and it is a {self.poke_type} type from the {self.region} region.")
        Actions.tap()
        print(f"This particular {self.name} is level {self.level}")


#  Pokedex data
quilava = Pokemon("Quilava", "Kanto", "Fire", 5)
chikorita = Pokemon("Chikorita", "Kanto", "Grass", 5)
totodile = Pokemon("Totodile", "Kanto", "Water", 5)

quilava.pokedex()
chikorita.pokedex()
totodile.pokedex()