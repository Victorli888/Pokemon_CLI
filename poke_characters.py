import Actions

"""
mv1 = moveset 1 (attack move, power up move , etc)
pokemon_l5 = pokemon name and its level
** NOTE move sets are currently a string value as a place holder. The plan is to create a method that will have an
effect in game when called on this will be under
"""


class Pokemon:
    def __init__(self, name, hp, attack, defence, speed, mv1, mv2, mv3, mv4):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.mv1 = mv1
        self.mv2 = mv2
        self.mv3 = mv3
        self.mv4 = mv4
    """
    Chance to Hit: Critical Chance: 20% 
    """
    def tackle(self):
        print(f"{self.name} Used Tackle...")
        Actions.tap()
        # Check for Hit/Miss
        # Check for Critical
        # Check stats and reference damage accordingly

    def scratch(self):
        print(f"{self.name} Used Scratch...")
        Actions.tap()
        # Check for Hit/Miss
        # Check for Critical
        # Check stats and reference damage accordingly

    def smokescreen(self):
        print(f"{self.name} used Smokescreen...")
        Actions.tap()
        # Check for Hit or Miss
        # Apply Status effect

    def leer(self):
        print(f"{self.name} used Leer...")
        Actions.tap()
        # Check for Hit or Miss
        # Apply Status Effect

    def growl(self):
        print(f"{self.name} used Growl...")
        Actions.tap()
        # Check for Hit or Miss
        # Apple Status Effect



cyndiquil_l5 = Pokemon("Cyndiquil", 39, 52, 43, 0, "tackle", "smokescreen", " ", " ")
chikorita_l5 = Pokemon("Chikorita", 45, 49, 65, 0, "tackle", "growl", " ", " ")
totodile_l5 = Pokemon("Totodile", 50, 65, 64, 0, "scratch", "leer", " ", " ")

totodile_l5.tackle()