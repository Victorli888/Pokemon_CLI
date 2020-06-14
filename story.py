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
    if ans == "Bed":  # Go to bed
        print("It's like 11AM are you sure you want to  go back to bed?")
        Actions.tap()
        print("[A] Yes I am sad and I want to go back to bed. or [B] No I'm going to do something today.")
        ans = input("> ")
        if ans == "A":  # I'm sure, Go to bed
            print("Congratulations you wasted an entire day!~~~")
            player_awake()
        elif ans == "B":  # Don't go to bed
            print("That's the spirit!")
            player_room()
        else:
            print(invalid)
            player_room()
    elif ans == "PC":  # open PC
        print("You walk and sit at your PC")
        player_pc()

    elif ans == "Door":  # Exit to the living room
        print("You exit your room and walk out your room.")
        door()

    else:
        print(invalid)
        player_awake()


def player_room():
    print("You find yourself standing in your room and you find 3 things to choose from \n[PC],\n[Door]\n[Bed]")
    ans = input("> ")
    if ans == "Bed":  # go to Bed
        print("You go to sleep")
        Actions.print_slow("........................................................................\n")
        player_awake()
    elif ans == "PC":  # Open PC
        player_pc()
    elif ans == "Door":  # Exit to living room
        print("You open the door and walkout")
        door()
    else:
        print(invalid)
        player_room()


def player_pc():
    print("Your PC boots and you have 3 selections to pick from\n> [Pokebox]\n> [Bank]\n> [Exit]")
    ans = input("> ")
    if ans == "Pokebox":  # View pokebox
        print(indev)
        pass
    elif ans == "Bank":  # View Bank
        print(indev)
        pass
    elif ans == "Exit":  # Exit
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
    if ans == "A":  # Eat Breakfast
        breakfast_eaten()
    elif ans == "B":  # Talk to Mom
        dialouge.mom_diag_2()
        door()
    elif ans == "C":  # Leave House without breakfast
        without_breakfast()
    else:
        print(invalid)
        door()


"""
door_2 serves as a checkpoint when the player finishes eating breakfast, so that they aren't required to eat breakfast
every time they enter the house
"""


def door_2():
    print("""You enter the living room What would you like to do now?
       \n[A] Talk to Mom.
       \n[B] Leave the house.""")
    ans = input("> ")
    if ans == "A":  # talk to mom
        dialouge.mom_diag_2()
        door_2()
    elif ans == "B":  # Exit
        pallet_town()
    else:
        print(invalid)
        door_2()


def without_breakfast():
    print("You're really going to leave without eating Mom's famous breakfast? [Y] or [N]")
    ans = input("> ")
    if ans == "Y":  # Leave with an empty stomach
        print("You leave at your own loss then...")
        Actions.tap()
        Actions.faint()
        player_awake()
    elif ans == "N":  # go back to eat breakfast
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
    if ans == "A":  # Talk to Mom
        print("You walk towards your mom and see that she's washing dishes at the kitchen sink")
        Actions.tap()
        dialouge.mom_diag_2()
        fin_breakfast()
    elif ans == "B":  # Leave house
        print("You place your hand on the door and walk out into wonderful outdoors.")
        Actions.tap()
        pallet_town()
    else:
        print(invalid)
        fin_breakfast()


def pallet_town():
    print("You see gorgeous blue skies, the field of short green grass that surround your small town. You see..."
          "\n [A] The Pallet Town PokeLab"
          "\n [B] The Westward Ocean Coastline"
          "\n [C] You're House.")
    print("Which would you like to visit first?")
    ans = input("> ")
    if ans == "A":  # For Pallet Town Poke Lab
        print("You make your way over to the Pallet Town PokeLab")
        Actions.tap()
        print("As you approach the building the automatic doors swing open and you find yourself in the lobby.")
        poke_lab()
    elif ans == "B":  # For Westward Ocean Coastline
        print("You look left and you walk down the path to the Westward Ocean Coastline")
        Actions.tap()
        westward_coast()
        print(indev)
        pass  # Add method for the "West Ward Ocean Coast line", and loop back to outside world
    elif ans == "C":  # For Home
        print("You take a look front yard and the house you grew up in...")
        Actions.tap()
        print("You walk towards the door and enter your childhood home.")
        Actions.tap()
        door_2()
    else:
        print(invalid)
        pallet_town()


"""
When the player obtains a Surfing Pokemon from Oak and surfs to Kanto from Westward Coast line is where i'll conclude
the game.

I may or may not add a fishing game element to the game, depending on its complexity, Most likely I will. It will have
a time with 3 dot prompts if you miss the third dot prompt you will fail to catch a fish. If I decide to go ahead with
this the Surf pokemon that is obtained to end the game should be obtained from this method.
"""


def westward_coast():
    print("You reach the beach with the warm sun hitting your back and the fresh ocean breeze hitting your face ")
    Actions.tap()
    print("What do you decide to do next?\n[A] Use Pokemon and Surf to the Kanto Region\n[B] Go Fish\n[C] Turn Back ")
    ans = input(">")
    if ans == "A":  # Surf to Kanto
        print(" You don't have any pokemon that can do that!")  # I think this is a great point to end the game..
        Actions.tap()
        westward_coast()
    elif ans == "B":  # Go Fish
        print("You decide its a wonderful day to go fishing! but then you realize you don't even have a fishing rod...")
        Actions.tap()
        westward_coast()
    elif ans == "C":  # Turn around
        print("As gorgeous and relaxing it is you decide to turn back and head back to pallet town")
        Actions.tap()
        pallet_town()
    else:
        print(invalid)
        westward_coast()


def poke_lab():
    print("You're in the famous Kanto Pokemon Laboratory. What would you like to do next? ")
    print("[A] Look around\n[B] Approach Lab Assistant\n[C] Approach Professor Oak\n[D] Exit Outside")
    ans = input("> ")
    if ans == "A":  # Look around
        Actions.look()
        print("You see all sorts of machines and gadgets. You even see Pokemon relaxing and waddling around.")
        Actions.tap()
        print("After glancing around you go back to the task at hand.")
        Actions.tap()
        poke_lab()
    elif ans == "B":  # Approach  Lab Assistant
        print(" You find a man in lab coat that is busy at work")
        Actions.tap()
        dialouge.assistant_diag_1()
        poke_lab()
    elif ans == "C":  # Approach Professor
        oak_intro()

    elif ans == "D":  # Exit lab
        print("You turn around and exit back from where you entered.")
        Actions.tap()
        pallet_town()
    else:
        print(invalid)
        poke_lab()


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
        poke_lab()
    else:
        print(invalid)
        oak_intro()


"""
I will need to add the pokemon the user picked into to his working inventory system in poke_selection. At the moment
we only have dialogue. 

I need to create a variable to save the pokemon that the user inputs
"""


def poke_selection():
    print("Follow me over here then! We have 3 Pokemon to adopt from.")
    Actions.tap()
    print("Please choose from either, \n[A] Cyndaquil\n[B] Totodile\n[C] Chikorita")
    ans = input("> ")
    if ans == "A":  # choose Cyndaquil
        print(" This is Cyndiquil, a fire type! Are you sure this is who you want? [Y] or [N]")
        ans = input("> ")
        if ans == "Y":
            print("You Chose Cyndiquil!")
            Actions.tap()
            post_poke_diag()
        elif ans == "N":
            print("No problem. take you time!")
            Actions.tap()
            poke_selection()
        else:
            print(invalid)
            poke_selection()
    elif ans == "B":  # choose Totodile
        print(" This is Totodile, a water type! Are you sure this is who you want? [Y] or [N]")
        ans = input("> ")
        if ans == "Y":
            print("You Chose Totodile!")
            Actions.tap()
            post_poke_diag()
        elif ans == "N":
            print("No problem. take you time!")
            Actions.tap()
            poke_selection()
        else:
            print(invalid)
            poke_selection()
    elif ans == "C":  # choose Chikorita
        print(" This is Chikorita, a grass type! Are you sure this is who you want? [Y] or [N]")
        ans = input("> ")
        if ans == "Y":
            print("You chose Chikorita!")
            Actions.tap()
            post_poke_diag()
        elif ans == "N":
            print("No problem. take you time!")
            Actions.tap()
            poke_selection()
        else:
            print(invalid)
            poke_selection()
    else:
        print(invalid)
        poke_selection()

# After selecting a pokemon new dialouge will follow next time the player enters the pokelab


def post_poke_diag():
    print("Congratulations on your new pokemon!")
    Actions.tap()
    print("As partners you'll travel the world and learn from each other.")
    Actions.tap()
    print("I wish you good luck!")
    Actions.tap()
    poke_lab2()


def poke_lab2():
    print("[A] Look around\n[B] Approach Lab Assistant\n[C] Approach Professor Oak\n[D] Exit Outside")
    ans = input("> ")
    if ans == "A":  # Look around
        Actions.look()
        print("You see all sorts of machines and gadgets. You even see Pokemon relaxing and waddling around.")
        Actions.tap()
        print("After glancing around you go back to the task at hand.")
        Actions.tap()
        poke_lab2()
    elif ans == "B":  # Approach  Lab Assistant
        print(" You find a man in lab coat that is busy at work")
        Actions.tap()
        dialouge.assistant_diag_1()
        poke_lab2()
    elif ans == "C":  # Approach Professor
        print("What are you still doing here? Adventure is out there waiting for you!")
        poke_lab2()

    elif ans == "D":  # Exit lab
        print("You turn around and exit back from where you entered.")
        Actions.tap()
        rival()  # This is where you battle your rival.

    else:
        print(invalid)
        poke_lab2()

# Scratch this part
# def grass():
#     """
#     This is where a Random Pokemon will appear, and where you will find a random item if you search long enough.
#     This will show case the inventory system and the battle system as well as the capture system
#     """
#     print("You find a large field of tall grass would you like to? ")
#     pass


def rival():
    """
    This will be the final boss for this project, This is where you will need to access the inventory system to use
    items. and use your extra pokemon to fight your rival. This will show case a different conditions, i.e
    (Not being able to run away or attempting to capture a trainers pokemon.
    """

    """
    Every event will need a new set of condition statements until we get to the end of the story.
    """
    pallet_town()
    pass


player_name = "Ash"
# Intro
# pokemon_intro()
# player_name = player_config()
# mom_intro_event()
# player_awake()
# breakfast()  # right now this should be removed as it serves no purpose
# lobby()
oak_intro()
