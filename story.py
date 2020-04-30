import dialouge, Actions

# to simply show that this is an invalid choice
invalid = "\nThat is not a valid section please try again."


print("Welcome to the world of Pokemon! Where animals big "
           "and large are enslaved to fight for our entertainment\n")




def player_config():
    print("\nPlease tell me are you a Boy or a Girl?")
    player_gender = input("> ")

    if player_gender == "Boy" or player_gender == "Girl":
        print(player_gender)

    else:
        print("That's not what I asked for...")
        player_config()

    print("ahhh I see. Please tell me your name")
    player_name = input("> ")
    print(f"Ok {player_name} welcome to Pallet Town your Pokemon Journey starts now!\n")
    Actions.tap()
    return player_name




def player_awake():
    print("You wake up in comfortable bed in room that Mom always keeps clean. "
              "You see 3 Options:\n[PC]\n[Door]\n[Bed].")
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
    print("You find yourself standing in your room and you find 3 things to choose from [PC],[Door], and [Bed]")
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
    print("Your PC boots and you have 3 selections to pick from"
              "\n> [Pokebox]"
              "\n> [Bank]"
              "\n> [Exit]")
    ans = input("> ")
    if ans == "Pokebox":
        print("In development")
        pass
    elif ans == "Bank":
        print("In development")
        pass
    elif ans == "Exit":
        print("Exiting PC...")
        player_room("standing")

    else:
        print(invalid)
        player_pc("PC")


def door():

    print("You enter the living room What would you like to do now?"
              "\n[A] Eat Mom's delicious breakfast!"
              "\n[B] Talk to Mom."
              "\n[C] Leave the house.")
    ans = input("> ")
    if ans == "A":
        breakfast("delicious")
    elif ans == "B":
        pass  # Home.mom(talk)
    elif ans == "C":
        left_without_breaky("lol u are dead")
    else:
        print(invalid)
        door("standing")

def mom(self):
        pass # This is where I will put her dialogue options
def left_without_breaky(self):
    print("You're really going to leave without eating Mom's famous breakfast? [Y] or [N]")
    ans = input("> ")
    if ans == "Y":
        print("You're absolutely heartless...")
        Actions.tap()
        Actions.Player_A.faint("dead")
        player_awake("Awake")
    elif ans == "N":
        print("Good lad, Now go eat that breakfast.")
        door("kitchen")
    else:
        print(invalid)
        left_without_breaky("standing")

def fin_breakfast(self):
    print("What would you like to do next?"
              "\n[A] Talk to Mom."
              "\n[B] Leave the house.")
    ans = input("> ")
    if ans == "A":
        pass  # Kitchen.mom("talk")
    elif ans =="B":
        pass  # Next stage is outside
    else:
        print(invalid)
        fin_breakfast("standing")

def breakfast(self):
    print("You eat a hearty delicious breakfast and you feel ready to tackle the day.")
    fin_breakfast("full")



def lobby(self):
    print("You enter the famous Kanto Pokemon Laboratory. What would you like to do next? ")
    print("[A] Look around\n[B] Approach Yash\n[C] Approach Professor Oak")
    ans = input("> ")
    if ans == "A":
        Actions.Player_A.look("Lab")
    if ans == "B":
        print(" You find a slim man in lab coat that is busy at work")
        Actions.tap()
        dialouge.Yash.diag_1("Intro")
        Actions.tap()
        lobby("lobby")
    if ans == "C":
        pass  # professor Oak dialouge

def Grass():
    """
    This is where a Random Pokemon will appear, and where you will find a random item if you search long enough.
    This will show case the inventory system and the battle system as well as the capture system
    """
    print("You find a large field of tall grass would you like to? ")
    pass

def Rival():
    """
    This will be the final boss for this project, This is where you will need to acess the inventory system to use
    items. and use your extra pokemon to fight your rival. This will show case a different conditions, i.e
    (Not being able to run away or attempting to capture a trainers pokemon.
    """
    pass

player_config()
player_awake()
"""
Play mom intro once create
"""
# breakfast()  # right now this should be removed as it serves no purpose
lobby()

