import sys
import time


# Use tap() action to simulate player tapping the a button for games
def tap():
    print(input("\nTap [Enter] to continue.. "))

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



def faint():
        print_slow("You're head feels light before you know it you fall to the ground, "
                   "and just like that your vision goes\ndark\n")
        print_slow("3.....2.....1......You have fainted\n")
        tap()

def look():
        print("You take a long look at your surroundings.")
        print_slow("...............")
        tap()

def battle():
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
        print("That wasn't a valid entry...")
        tap()
        battle("battling")

def run_away():
        print("You attempt to run away!")
        print_slow(".................")
        tap()

