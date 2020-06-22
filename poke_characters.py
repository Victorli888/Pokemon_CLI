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
            damage = self.attack * .12
            if crit is True:
                print("It was a Critical Hit!")
                damage = damage * 1.5
                print(f"inflicted {damage} points of damage")
                return damage
            print(f"inflicted {damage} points of damage")
            return damage
        else:
            print("Attack was a miss...")

    def scratch(self):
        print(f"{self.name} Used Scratch...")
        Actions.tap()
        # Check for Hit/Miss
        hit = Actions.chance(95)

        # Check stats and reference damage accordingly
        if hit is True:
            print("It was a successful hit!")
            damage = self.attack * .12
            print(f"inflicted {damage} points of damage")
            return damage
        else:
            print("Attack was a miss...")

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


cyndiquil_l5 = Pokemon("Cyndiquil", 39, 52, 43, 65, "Tackle", "Smokescreen", " ", " ")
chikorita_l5 = Pokemon("Chikorita", 45, 49, 65, 45, "Tackle", "Growl", " ", " ")
totodile_l5 = Pokemon("Totodile", 50, 65, 64, 43, "Scatch", "Leer", " ", " ")


