import sys
import time
import random


# Use tap() action to simulate player tapping the a button for games
def tap():
    print(input("\nTap [Enter] to continue... "))


def chance(success_rate):
    result = random.random() * 100
    if success_rate >= result:
        return True  # action attempt passes
    else:
        return False  # action attempt failed


def print_slow(a_string):
    type_speed = 200
    for letter in a_string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(10.0 / type_speed)


def print_normal(a_string):
    type_speed = 5200
    for letter in a_string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(10.0 / type_speed)


def faint():
    print_slow("You're head feels light before you know it you fall to the ground and just like that your vision goes\n"
               "dark\n")
    print_slow("3.....2.....1......You have fainted\n")
    tap()


def look():
    print("You take a long look at your surroundings.")
    print_slow("...............")
    tap()


def run_away():
    print("You attempt to run away!")
    print_slow(".................")
    tap()
    result = chance(60)

    if result is True:
        print("You successfully got away!")
    else:
        print("You failed to get away.")
