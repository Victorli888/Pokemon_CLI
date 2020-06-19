"""
mv1 = moveset 1 (attack move, power up move , etc)
pokemon_l5 = pokemon name and its level
** NOTE move sets are currently a string value as a place holder. The plan is to create a method that will have an
effect in game when called on this will be under
"""


class Pokemon:
    def __init__(self, name, hp, attack, defence, mv1, mv2, mv3, mv4):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.mv1 = mv1
        self.mv2 = mv2
        self.mv3 = mv3
        self.mv4 = mv4


cyndiquil_l5 = Pokemon("Cyniquil", 39, 52, 43, "tackle", "smokescreen", " ", " ")
chikorita_l5 = Pokemon("Chikorita", 45, 49, 65, "tackle", "growl", " ", " ")
totodile_l5 = Pokemon("Totodile", 50, 65, 64, "scratch", "leer", " ", " ")
