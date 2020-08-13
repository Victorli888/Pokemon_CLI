import Actions


"""
mv1 = moveset 1 (attack move, power up move , etc)
pokemon_l5 = pokemon name and its level
** NOTE move sets are currently a string value as a place holder. The plan is to create a method that will have an
effect in game when called on this will be under

speed will be implemented in v1.1 to determine who goes first in a battle.

DEVELOPER NOTES: 
Remove Move_set from Pokemon Class and apply them to a new move list script [ DON't CREATE A FACTORY INSIDE A FACTORY
keep "Tackle", "Smokescreen" etc as string values for battle.py and only apply the methods when needed.

story.py is when the actual instances of a pokemon hp and stats save it into a hash map.

poke_characters.py will use this classes to generate the pokedex
"""


class Pokemon:
    def __init__(self, name, hp, og_hp, attack, og_atk, defence, og_def, speed):
        self.name = name
        self.hp = hp
        self.og_hp = og_hp
        self.attack = attack
        self.og_atk = og_atk
        self.defence = defence
        self.og_def = og_def
        self.speed = speed

    def reset_stats(self):
        self.hp = self.og_hp
        self.attack = self.og_atk
        self.defence = self.og_def

    def tackle(self):
        print(f"{self.name} Used Tackle...")
        Actions.tap()
        # Check for Hit/Miss
        hit = Actions.chance(90)

        # Check for Critical
        crit = Actions.chance(20)

        # Check stats and reference damage accordingly
        if hit is True:
            print("It was a successful hit!")
            damage = round(self.attack * .12)
            if crit is True:
                print("It was a Critical Hit!")
                damage = round(damage * 1.5)
                print(f"inflicted {damage} points of damage")
                return damage
            print(f"inflicted {damage} points of damage")
            return damage
        else:
            print("Attack was a miss...")
            return 0

    def scratch(self):
        print(f"{self.name} Used Scratch...")
        Actions.tap()
        # Check for Hit/Miss
        hit = Actions.chance(95)

        # Check stats and reference damage accordingly
        if hit is True:
            print("It was a successful hit!")
            damage = round(self.attack * .12)
            print(f"inflicted {damage} points of damage")
            return damage
        else:
            print("Attack was a miss...")
            return 0

    def smokescreen(self):
        print(f'{self.name} used Smokescreen...')
        Actions.tap()
        # Check for Hit or Miss
        hit = Actions.chance(90)

        # Apply Status Effect
        if hit is True:
            print("It was a successful hit!")
            print("Opponent defence was lowered")
            def_down = .20
            return def_down
        else:
            print("Attack was a miss...")
            return 0

    def leer(self):
        print(f"{self.name} used Leer...")
        Actions.tap()
        # Check for Hit or Miss
        hit = Actions.chance(90)

        # Apply Status Effect
        if hit is True:
            print("It was a successful hit!")
            print("Opponent defence was lowered")
            def_down = .20
            return def_down
        else:
            print("Attack was a miss...")
            return 0

    def growl(self):
        print(f"{self.name} used Growl...")
        Actions.tap()
        # Check for Hit or Miss
        hit = Actions.chance(90)

        # Apply Status Effect
        if hit is True:
            print("It was a successful hit!")
            print("Opponent attack was lowered")
            atk_down = .20
            return atk_down
        else:
            print("Attack was a miss...")
            return 0


cyndiquil_l5 = Pokemon("Cyndiquil", 40, 40, 52, 52, 43, 43, 65)
chikorita_l5 = Pokemon("Chikorita", 45, 45, 49, 49, 65, 65, 45)
totodile_l5 = Pokemon("Totodile", 50, 50, 65, 65, 64, 64, 43)
totodile_rival = Pokemon("Totodile", 50, 50, 65, 65, 64, 64, 43)

scratch = Pokemon.scratch
tackle = Pokemon.tackle
smokescreen = Pokemon.smokescreen
leer = Pokemon.leer
growl = Pokemon.growl


cy_l5 = {"move1": tackle, "move2": smokescreen}
