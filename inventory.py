"""
acquiring more potions and pokeballs can be implemented for a later date. for now potions and pokeballs will be given to
the player when he begins his first poke-trainer battle.
"""


class Inventory:

    def __init__(self, item):
        self.item = item

    def use(self):
        if self.item <= 0:
            print("You have none to use.")
        else:
            self.item -= 1
        return self.item

    def obtain(self):
        self.item += 1
        return self.item


items = {"potion": 1, "super potion": 1, "pokeball": 5, "great ball": 3}
potion = Inventory(items["potion"])
super_potion = Inventory(items["super potion"])

# items["potion"] = potion.use()


