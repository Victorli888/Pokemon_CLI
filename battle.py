import Actions
import poke_characters
import inventory

invalid = "\nThat is not a valid section please try again."
"""
Implementation for wild pokemon battles saved for v1.1.
"""


class WildPokemon(object):

    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name

    def intro(self):
        print(f"A wild {self.pokemon_name} appeared...")


"""
pokemon1 = player's pokemon
pokemon2 = NPC's pokemon
"""


class TrainerBattle:
    def __init__(self, trainer_name, pokemon1, pokemon2):
        self.trainer_name = trainer_name
        self.pokemon2 = pokemon2
        self.pokemon1 = pokemon1

    def intro(self):
        print(f"Trainer {self.trainer_name} wants to battle...")
        Actions.tap()
        print(f"Trainer {self.trainer_name} sent out {self.pokemon2.name}")
        Actions.tap()

    def fight(self):
        print(f"{self.pokemon1.name} wants to fight!")
        Actions.tap()
        ans = input("Please select a move:")
        print(f"{self.pokemon1.mv1}\n{self.pokemon1.mv2}")

    def items(self):
        print("Which item would you like to use?")
        print("[A] Potions x [{}] ".format(inventory.items["potion"]))
        print("[B] Super Potion x [{}]".format(inventory.items["super potion"]))
        print("[C] Cancel, Go back")
        ans = input("Choice:  ")
        if ans == "A":
            inventory.items["potion"] -= 1
            print("Potion used to regain 20HP")
        elif ans == "B":
            inventory.items["super potion"] -= 1
            print("Super Potion used 50 HP was regained")
        elif ans == "C":
            print("In development")
        else:
            self.items()

        ans = input()

    def pokeball(self):
        pass

    def battle(self):
        print("What will you do? \n[A] Fight \n[B] Items \n[C] Pokeball \n[D] Flee ")
        ans = input("\nType answer here: ")
        if ans == "A":
            self.fight()
        elif ans == "B":
            self.items()
        elif ans == "C":
            self.pokeball()
        elif ans == "D":
            print("You can't flee from a trainer battle!")
            self.battle()
        else:
            print(invalid)
            self.battle()


totodile1 = poke_characters.totodile_l5
cyndiquil1 = poke_characters.cyndiquil_l5

first_battle = TrainerBattle("Rival Gary", cyndiquil1, totodile1)
first_battle.intro()
first_battle.battle()
first_battle.items()
