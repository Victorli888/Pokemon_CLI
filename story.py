import dialouge
import Actions
import poke_characters
import trainer_battle

# to simply show that this is an invalid choice
invalid = "\nThat is not a valid section please try again."
indev = "This section is in development."


def error():
    print(invalid)
    Actions.tap()


def pokemon_intro():
    print("Game Tip: When prompted the game will ask you to answer questions answer with the word contained in [ ].")
    Actions.tap()
    print("Hello there! Welcome to the world of pokemon! My name is OAK! People call me the Professor!")
    Actions.tap()
    print("This world is inhabited by creatures called pokemon! For some people, pokemon are pets.")
    Actions.tap()
    print("Others use them for fights. Myself...I study pokemon as a profession.")
    Actions.tap()



def player_config():
    print("\nFirst, Please tell me what's your gender?")
    player_gender = input("> ")

    print("okay I'll write that down! I'm filling out a form here and no one cares so It can be whatever")
    Actions.tap()

    print("Excellent! Everything is looking good on my end")

    print("Now, Please tell me your name.")
    select_name = input(">My name is: ")
    num = len(select_name)
    while num < 3:
        print("That's a really short name please we're friends here tell me your full name")
        select_name = input("> My name is: ")
        num = len(select_name)

    print(f"Ok {select_name} welcome to Pallet Town your Pokemon Journey starts now!\n")
    Actions.tap()
    return select_name


def mom_intro_event(player_name):
    print("You gently open your eyes and you see a more than familiar face.")
    Actions.tap()
    print("You see your mother staring you straight in the face. gitty with excitement.")
    Actions.tap()
    dialouge.mom_diag_1(player_name)
    print("She sneaks out the room closing the door behind her.")
    player_awake()


def player_awake():
    Actions.tap()
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
        print("You try to access your pokebox but it looks like the system is down for maintenance.")
        player_pc()

    elif ans == "Bank":  # View Bank
        print("You Log in your Bank Credentials and your account summary appears")
        Actions.tap()
        print("~~~ Account Summary ~~~"
              "\nCheckings: $0"
              "\nSavings: $0")
        Actions.tap()
        print("Mom really should give me an allowance...")
        Actions.tap()
        print("You exit back to the PC")
        player_pc()

    elif ans == "Exit":  # Exit
        print("Exiting PC...")
        player_room()

    else:
        print(invalid)
        player_pc()


def door():
    print("You walk down the stairs and you see mom put down some food on the dining room table.")
    Actions.tap()
    print("Mom:  Hello dear! I just made you some breakfast!")
    Actions.tap()
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
        oak_intro(player_name)

    elif ans == "D":  # Exit lab
        print("You turn around and exit back from where you entered.")
        Actions.tap()
        pallet_town()
    else:
        print(invalid)
        poke_lab()


def oak_intro(player_name):
    print("You walk up to the leading Poke expert in your region.")
    Actions.tap()
    dialouge.proffesor_diag_1(player_name)
    print("[A] Yes I'm ready.\n[B] No I'd like to look around a bit longer")
    ans = input("> ")
    if ans == "A":
        print("Follow me over here then mah boy")

    elif ans == "B":
        print("You go back to the front lobby of the PokeLab.")
        Actions.tap()
        poke_lab()

    else:
        print(invalid)
        oak_intro(player_name)


"""
I will need to add the pokemon the user picked into to his working inventory system in poke_selection. At the moment
we only have dialogue. 

I need to create a variable to save the pokemon that the user inputs, [Selection will be hard coded for Cyndiquil]
"""


def poke_selection():

    print("We have 3 Pokemon to adopt from.")
    Actions.tap()
    print("Please choose from either, \n[A] Cyndaquil\n[B] Totodile\n[C] Chikorita")
    ans = input("> ")
    if ans == "A":  # choose Cyndaquil
        print(" This is Cyndiquil, a fire type! Are you sure this is who you want? [Y] or [N]")
        ans = input("> ")
    if ans == "Y":
        print("You Chose Cyndiquil!")
        Actions.tap()
        player_poke = poke_characters.cyndiquil_l5
        return player_poke

    elif ans == "B":  # choose Totodile
        print(" This is Totodile, a water type! Are you sure this is who you want? [Y] or [N]")
        ans = input("> ")
    if ans == "Y":
        print("You Chose Totodile!")
        Actions.tap()
        player_poke = poke_characters.totodile_l5
        return player_poke

    elif ans == "C":  # choose Chikorita
        print("This is Chikorita, a grass type! Are you sure this is who you want? [Y] or [N]")
        ans = input("> ")
    if ans == "Y":
        print("You chose Chikorita!")
        player_poke = poke_characters.chikorita_l5
        Actions.tap()
        return player_poke

    print("No problem Take your time!")
    return None






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
        print("You tip toe up to the professor to talk to him.")
        Actions.tap()
        print("What are you still doing here? Adventure is out there waiting for you!")
        poke_lab2()

    elif ans == "D":  # Exit lab
        print("You turn around and exit back from where you entered.")
        Actions.tap()
        pass

    else:
        print(invalid)
        poke_lab2()


"""
scratched for now, can be re-implemented after 1.0 release. after poke_lab2
"""
# def grass():
#     """
#     This is where a Random Pokemon will appear, and where you will find a random item if you search long enough.
#     This will show case the inventory system and the battle system as well as the capture system
#     """
#     print("You find a large field of tall grass would you like to? ")
#     pass


def rival(player_poke):
    # Rival Pokemon
    rival_poke = poke_characters.totodile_rival

    # Rival Pokemon will reset HP before every encounter
    rival_poke.reset_stats()
    print("Congratulations! Now you ready to adventure out in the world as a pokemon trainer. ")
    Actions.tap()
    print("As you step out of the Lab you see someone waiting just around the corner")
    Actions.tap()
    print(" A strange red haired trainer with a black jacket approaches you!")
    Actions.tap()
    dialouge.rival_diag_1()
    if player_poke == poke_characters.cyndiquil_l5:
        # Player Pokemon
        p_poke = poke_characters.cyndiquil_l5
        cy_moves = {"move1": poke_characters.tackle, "move2": poke_characters.smokescreen}
        cy_move_names = ["tackle", "smokescreen"]
        o_toto_moves = {"move1": poke_characters.scratch, "move2": poke_characters.leer}
        # Battle Sequence
        first_battle = trainer_battle.TrainerBattle("Rival Gary", rival_poke, p_poke, cy_moves, cy_move_names, o_toto_moves)
        player_poke = first_battle.battle()
        return player_poke
    elif player_poke == poke_characters.totodile_l5:
        # Player Pokemon
        p_poke = poke_characters.totodile_l5
        toto_moves = {"move1": poke_characters.scratch, "move2": poke_characters.leer}
        toto_move_names = ["scratch", "leer"]
        o_toto_moves = {"move1": poke_characters.scratch, "move2": poke_characters.leer}
        # Battle Sequence
        first_battle = trainer_battle.TrainerBattle("Rival Gary", rival_poke, p_poke, toto_moves, toto_move_names, o_toto_moves)
        player_poke = first_battle.battle()
        return player_poke
    elif player_poke == poke_characters.chikorita_l5:
        # Player Pokemon
        p_poke = poke_characters.chikorita_l5
        chika_moves = {"move1": poke_characters.tackle, "move2": poke_characters.growl}
        chika_move_names = ["tackle", "growl"]
        o_toto_moves = {"move1": poke_characters.scratch, "move2": poke_characters.leer}
        # Battle Sequence
        first_battle = trainer_battle.TrainerBattle("Rival Gary", rival_poke, p_poke, chika_moves, chika_move_names, o_toto_moves)
        p_poke = first_battle.battle()
        return p_poke
    else:
        print("SOMETHING WENT WRONG!")


def post_rival_battle():
    Actions.tap()
    print("You see the stranger run away abandoning his totodile")
    Actions.tap()
    print("You approach Totodile and you see that he is in deep need of a new home")
    Actions.tap()


def adopt_totodile():
    print("Do you wish to adopt Totodile? [Y] or [N]")
    ans = input("> ")
    if ans == "N":
        print("How could you not want to adopt something this cute?! think again")
        adopt_totodile()
    if ans == "Y":
        print("You adopted Totodile!")


def toto_realization():
    print("As you hold Totodile a little closer you notice he has a silver coin on his neck")
    Actions.tap()
    print('You read the coin and find that it says: \nName: Toto\nAddress: Gold Coast Building #3')
    Actions.tap()
    print("Gold Coast?! That's across the ocean")
    Actions.tap()
    print("You make a realization that Toto was stolen from his home and should be reunited with his real home")
    Actions.tap()
    print("You step back into Pallet town and briskly make your way across town")


def pallet_town_2():
    Actions.tap()
    print("You see gorgeous blue skies, the field of short green grass that surround your small town. You see..."
          "\n [A] The Pallet Town PokeLab"
          "\n [B] The Westward Ocean Coastline"
          "\n [C] You're House.")
    print("Which would you like to visit first?")
    ans = input("> ")
    if ans == "A":  # For Pallet Town Poke Lab
        print("We're running out of time We should really get to the dock before we miss the last ferry")
        pallet_town_2()

    elif ans == "B":  # For Westward Ocean Coastline
        print("You look left and you walk down the path to the Westward Ocean Coastline")
        westward_coast_2()

        pass  # Add method for the "West Ward Ocean Coast line", and loop back to outside world
    elif ans == "C":  # For Home
        print("We're running out of time We should really get to the dock before we miss the last ferry")
        pallet_town_2()
    else:
        print(invalid)
        pallet_town_2()


def westward_coast_2():
    Actions.tap()
    print("You reach the beach with the warm sun hitting your back and the fresh ocean breeze hitting your face ")
    Actions.tap()
    print("What do you decide to do next?\n[A] Visit Dock\n[B] Go Fish\n[C] Turn Back ")
    ans = input(">")
    if ans == "A":  # Take a boat to go to Gold Coast
        print(" You approach the West Coast Shoreline Ferry Station")
        dock()
    elif ans == "B":  # Go Fish
        print("You decide its a wonderful day to go fishing! but then you realize you don't even have a fishing rod...")
        Actions.tap()
        print("without hesitation you see Toto dive in trying to catch the fish!")
        Actions.tap()
        print("Unable to catch anything he crawls out the water and back next to you, and you get back to the task at"
              " hand")
        westward_coast_2()
    elif ans == "C":  # Turn around
        print("As gorgeous and relaxing it is you decide to turn back and head back to pallet town")
        pallet_town_2()
    else:
        print(invalid)
        westward_coast_2()


# This is where you'll get a ticket to get to Gold Coast from West Coast Shore line
def dock():
    Actions.tap()
    print("As you approach you see this large ship that sways back and forth in the water.")
    Actions.tap()
    print("As your eyes wander around. You see the ticket booth off to the left making last calls for boarding tickets")
    Actions.tap()
    print("you approach the ticket counter and you see a tired ticketer. as he looks to you he says:")
    dialouge.ticketer_diag_1()
    ans = input("> Type either [Y] or [N]. ")
    if ans == "Y":
        print("You buy the ticket and board the ship to get ready for your adventure in Gold Coast")
        Actions.tap()
        print("You stumble around the corridors of the ship trying to find your cabin E22")
        print("At the end of the hallway you finally find your cabin!")
    elif  ans =="N":
        dialouge.ticketer_diag_2()
        print("You feel as if you're not ready so you walk back to the beach think what you really want to do next.")
        westward_coast_2()
    else:
        print(invalid)
        dock()


def ship_cabin(player_poke):
    Actions.tap()
    print(f"You open the door and take a load off. You watch {player_poke} and Toto play around the room.")
    print("As you sit down you feel your fatigue overwhelm you.")
    Actions.tap()
    print("it's been a long day and you start to close your eyes for a second.")
    Actions.tap()
    print("Part 1 Finished!")
    print("Thanks so much for playing!")


# Game Intro / set up
pokemon_intro()
player_name = player_config()

# Mother introduction
mom_intro_event(player_name)


# Player selects a pokemon if choice is invalid the function will re-call itself until answer is valid
player_pokemon = poke_selection()
while player_pokemon is None:
    player_pokemon = poke_selection()


# # New Pokemon saved to player and fight with Rival starts
player_pokemon = rival(player_pokemon)
while player_pokemon.hp <= 0:
    dialouge.rival_diag_2()
    print("GAME OVER")
    print("To Revert to last save please tap any key to continue")
    Actions.tap()
    Actions.print_slow("Reverting to last save........save loaded.")
    Actions.tap()
    player_pokemon.reset_stats()
    player_pokemon = rival(player_pokemon)

# Rival Defeated dialogue continues...
# dialouge.rival_diag_3()

# Adopting totodile
post_rival_battle()
adopt_totodile()

# End game revealed
toto_realization()

# Back to Pallet Town
pallet_town_2()
ship_cabin(player_pokemon.name)



