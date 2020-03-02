import sys,time,story,random

def print_slow(str):
    type_speed = 200
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(10.0 / type_speed)

def print_normal(str):
    type_speed = 5200
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(10.0 / type_speed)


class Player_A():
    def faint(self):
        print_slow("You're head feels light before you know it you fall to the ground, "
                   "and just like that your vison goes\ndark\n")
        print_slow("3.....2.....1......You have fainted\n")
        story.tap

    def look(self):
        print("You take a long look at your surroundings.")
        print_slow("...............")
        story.tap

    def battle(self):
        print("You are ready to battle. Please make a Choice\n")
        print("[A} Attack\n[B] Items\n[C] Pokemon\n[D] Run")
        ans = input("> ")
        if input == "A":
            pass # create attacks ( make another script for move lists)
        elif input == "B":
            pass # from the inventory, create a menu of items that is avalible for the player to use.
        elif input == "C":
            pass # create a menu for Pokemon avaliable for the Player to call upon.
        elif input == "D":
            pass # create a method  in Actions.py that randomized the chance of being able to run.
        else:
            print(story.invalid)

    def run_away(self):
        print("You attempt to run away!")
        print_slow(".................")
        story.tap