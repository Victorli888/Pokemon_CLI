import dialouge
import Actions

# to simply show that this is an invalid choice
invalid = "\nThat is not a valid section please try again."
indev = "This section is in development."


def pokemon_intro():
    print("Hello there! Welcome to the world of POKEMON! My name is OAK! People call me the POKEMON PROF!")
    Actions.tap()
    print("This world is inhabited by creatures called POKEMON! For some people, POKEMON are pets.")
    Actions.tap()
    print("Others use them for fights. Myself...I study POKEMON as a profession.")
    Actions.tap()


def player_config():
    print("\nFirst, Please tell me are you a Boy or a Girl?")
    player_gender = input("> ")

    if player_gender == "Boy" or player_gender == "Girl":
        print("Excellent!")

    else:
        print(invalid)
        player_config()

    print("Now, Please tell me your name.")
    select_name = input("> ")
    print(f"Ok {select_name} welcome to Pallet Town your Pokemon Journey starts now!\n")
    Actions.tap()
    return select_name


def mom_intro_event():
    print("You gently open your eyes and you see a more than familiar face.")
    Actions.tap()
    print("You see your mother staring you straight in the face. gitty with excitement.")
    Actions.tap()
    dialouge.mom_diag_1(player_name)
    print("She sneaks out the room closing the door behind her.")
    player_awake()

def player_awake():
    print("You wake up in comfortable bed in room that Mom always keeps clean.You see 3 Options:\n[PC]\n[Door]\n[Bed].")
    ans = input("> ")
    if ans == "Bed":
        print("It's like 11AM are you sure you want to  go back to bed?")
        Actions.tap()
        print("[A] Yes I am sad and I want to go back to bed. or [B] No I'm going to do something today.")
        ans = input("> ")
        if ans == "A":
            print("Congratulations you wasted an entire day!~~~")
            player_awake()
        elif ans == "B":
            print("That's the spirit!")
            player_room()
        else:
            print(invalid)
            player_room()
    elif ans == "PC":
        print("You walk and sit at your PC")
        player_pc()

    elif ans == "Door":
        print("You exit your room and walk out your room.")
        door()

    else:
        print(invalid)
        player_awake()


def player_room():
    print("You find yourself standing in your room and you find 3 things to choose from \n[PC],\n[Door]\n[Bed]")
    ans = input("> ")
    if ans == "Bed":
        print("You go to sleep")
        Actions.print_slow("........................................................................\n")
        player_awake()
    elif ans == "PC":
        player_pc()
    elif ans == "Door":
        print("You open the door and walkout")
        door()
    else:
        print(invalid)
        player_room()


def player_pc():
    print("Your PC boots and you have 3 selections to pick from\n> [Pokebox]\n> [Bank]\n> [Exit]")
    ans = input("> ")
    if ans == "Pokebox":
        print(indev)
        pass
    elif ans == "Bank":
        print(indev)
        pass
    elif ans == "Exit":
        print("Exiting PC...")
        player_room()

    else:
        print(invalid)
        player_pc()


def door():

    print("""You enter the living room What would you like to do now?
    \n[A] Eat Mom's delicious breakfast!
    \n[B] Talk to Mom.
    \n[C] Leave the house.""")
    ans = input("> ")
    if ans == "A":
        breakfast_eaten()
    elif ans == "B":
        dialouge.mom_diag_2()
        door()
    elif ans == "C":
        without_breakfast()
    else:
        print(invalid)
        door()


def without_breakfast():
    print("You're really going to leave without eating Mom's famous breakfast? [Y] or [N]")
    ans = input("> ")
    if ans == "Y":
        print("You leave at your own loss then...")
        Actions.tap()
        Actions.faint()
        player_awake()
    elif ans == "N":
        print("Good lad, Now go eat that breakfast.")
        door()
    else:
        print(invalid)
        without_breakfast()


def breakfast_eaten():
    print("You eat a hearty delicious breakfast and you feel ready to tackle the day.")
    fin_breakfast()


def fin_breakfast():
    print("What would you like to do next?\n[A] Talk to Mom.\n[B] Leave the house.")
    ans = input("> ")
    if ans == "A":
        print("You walk towards your mom and see that she's washing dishes at the kitchen sink")
        Actions.tap()
        dialouge.mom_diag_2()
        fin_breakfast()
    elif ans == "B":
        print("You place your hand on the door and walk out into wonderful outdoors.")
        Actions.tap()
        outside_world()
    else:
        print(invalid)
        fin_breakfast()


def outside_world():
    print("You see gorgeous blue skies, the field of short green grass that surround your small town. You see..."
          "\n [A] The Pallet Town PokeLab"
          "\n [B] The Westward Ocean Coastline"
          "\n [C] You're House.")
    print("Which would you like to visit first?")
    ans = input("> ")
    if ans == "A":
        print("You make your way over to the Pallet Town PokeLab")
        Actions.tap()
        print("As you approach the building the automatic doors swing open and you find yourself in the lobby.")
        lobby()
    elif ans == "B":
        print(indev)
        pass  # Add method for the "West Ward Ocean Coast line", and loop back to outside world
    elif ans == "C":
        print("You take a look front yard and the house you grew up in...")
        Actions.tap()
        print("You walk towards the door and enter your childhood home.")
        print(indev)
        pass  # door() method needs to be fixed so the player can back track into his room and exit w/0 replaying intro.


def lobby():
    print("You're in the famous Kanto Pokemon Laboratory. What would you like to do next? ")
    print("[A] Look around\n[B] Approach Yash\n[C] Approach Professor Oak")
    ans = input("> ")
    if ans == "A":
        Actions.look()
        print("You see all sorts of machines and gadgets. You even see Pokemon relaxing and waddling around.")
        Actions.tap()
        print("After glancing around you go back to the task at hand.")
        Actions.tap()
        lobby()
    if ans == "B":
        print(" You find a man in lab coat that is busy at work")
        Actions.tap()
        dialouge.yash_diag_1()
        lobby()
    if ans == "C":
        oak_intro()


def oak_intro():
    print("You walk up to the leading Poke expert in your region.")
    Actions.tap()
    dialouge.proffesor_diag_1(player_name)
    print("[A] Yes I'm ready.\n[B] No I'd like to look around a bit longer")
    ans = input("> ")
    if ans == "A":
        poke_selection()
    elif ans == "B":
        print("You go back to the front lobby of the PokeLab.")
        Actions.tap()
        lobby()
    else:
        print(invalid)
        oak_intro()


def poke_selection():
    pass  # Player will select pokemon here


def grass():
    """
    This is where a Random Pokemon will appear, and where you will find a random item if you search long enough.
    This will show case the inventory system and the battle system as well as the capture system
    """
    print("You find a large field of tall grass would you like to? ")
    pass


def rival():
    """
    This will be the final boss for this project, This is where you will need to acess the inventory system to use
    items. and use your extra pokemon to fight your rival. This will show case a different conditions, i.e
    (Not being able to run away or attempting to capture a trainers pokemon.
    """
    pass

player_name = "Ash"
# Intro
# pokemon_intro()
# player_name = player_config()
# mom_intro_event()
# player_awake()
# breakfast()  # right now this should be removed as it serves no purpose
# lobby()

fin_breakfast()