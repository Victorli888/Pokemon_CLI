class wild_poke(object):

    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        print(f"A wild {pokemon_name} appeared...")

pidgey = wild_poke("Pidgey")  # del this
rattata = wild_poke("Rattata")  # del this


class Trainer_battle():
    def __init__(self, trainer_name):
        self.trainer_name = trainer_name
        print(f"Trainer {trainer_name} wants to battle...")



# intro for a battle works, I think I should make a switch case or a dictioanry
# that pulls these names to make it seem like it randomly appears when wandering through a bush





