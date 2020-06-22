"""
acquiring more potions and pokeballs can be implemented for a later date. for now potions and pokeballs will be given to
the player when he begins his first poke-trainer battle.
"""

items = {"potion": 3, "super potion": 1}
balls = {"pokeball": 5, "great ball": 3, "ultra ball": 1}

# ans = input("y/n")
# while ans:
#     print(items["potion"])
#     input("tap to continue")
#     if ans == "y":
#         items["potion"] -= 1
#
#     else:
#         print("potion not used")
#     ans = input("y/n")
#

"""
Experiement with using Class to build an active inventory instead of a hashmap.
UPDATE: I am most likely going to move in this direction.
"""


class Inventory:
    def __init__(self, quantity):
        self.quantity = quantity

    def potion(self):
        if self.quantity <= 0:
            print("You don't have any to use.")
            return self.quantity
        else:
            self.quantity -= 1
            print("Potion used! 30 HP was regained.")
            return self.quantity


potion = Inventory(1)  # Initialize Item for use
# print(potion.quantity) # For Quantity


def use():
    ans = input("Use Potion?:")
    if ans == "y":
        potion.potion()
        use()
    else:
        use()




