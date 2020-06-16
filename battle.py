import Actions
class wild_poke(object):

    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        print(f"A wild {pokemon_name} appeared...")

pidgey = wild_poke("Pidgey")  # del this
rattata = wild_poke("Rattata")  # del this

"""
Hard code for Cyndiquil as player picked pokemon.
"""
class Trainer_battle():
    def __init__(self, trainer_name, pokemon):
        self.trainer_name = trainer_name
        self.pokemon = pokemon
        print(f"Trainer {trainer_name} wants to battle...")
        Actions.tap()
        print(f"Trainer {trainer_name} sent out {pokemon}")
        Actions.tap()

    def battle(self):
        print("What will you do? [A] Fight [B] Items [C] Pokeball [D] Flee ")
        ans = input("Type answer here: ")
        if ans == "A":
            pass  # fight()
        elif ans == "B":
            pass  # items()
        elif ans == "D":
            pass  # pokeball()
        elif ans == "D":
            pass  # flee()











# intro for a battle works, I think I should make a switch case or a dictionary
# that pulls these names to make it seem like it randomly appears when wandering through a bush





