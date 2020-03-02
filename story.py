import dialouge
import Actions


invalid = "\nThat is not a valid section please try again."
tap = input("[Press Enter] ")

print("Welcome to the world of Pokemon! Where we enslave animals big "
           "and large to fight for our entertainment\n")

class Single_events():  # FIND A WAY TO MAKE THIS WORK

    def mom_intro(self):
        # x = True
        # if x is True:
        dialouge.Mom.diag_1("talking")
        # else:
        #     print("Failed")





class Player_Configuration():
    def __init__(self, player_name, player_gender):
        self.player_name = player_name
        self.player_gender = player_gender  # I need to check whether or not this stuff is necessary
    def player_config(self):

        print("\nPlease tell me are you a Boy or a Girl?")
        player_gender = input("> ")

        if player_gender == "Boy" or player_gender == "Girl":
            print(player_gender)

        else:
            print("That's not what I asked for...")
            Player_Configuration.player_config()

        print("ahhh I see. Please tell me your name")
        player_name = input("> ")
        Actions.print_slow(f"Ok {player_name} welcome to Pallet Town your Pokemon Journey starts now!\n")
        tap
        # I need to make sure that these save into a variable that can used globally without using Global.


class Bedroom():
    def player_awake(self):
        print("You wake up in comfortable bed in room that Mom always keeps clean. "
              "You see 3 Options:\n[PC]\n[Door]\n[Bed].")
        ans = input("> ")
        if ans == "Bed":
            print("It's like 11AM are you sure you want to  go back to bed?")
            tap
            print("[A] Yes I am sad and I want to go back to bed. or [B] No I'm going to do something today.")
            ans = input("> ")
            if ans == "A":
                print("Congratulations you wasted an entire day!~~~")
                Bedroom.player_awake("awake")
            elif ans == "B":
                print("That's the spirit!")
                Bedroom.player_room("standing")
            else:
                print(invalid)
                Bedroom.player_room("standing")
        elif ans == "PC":
            print("You walk and sit at your PC")
            Bedroom.player_pc("PC")
        elif ans == "Door":
            print("You exit your room and walk out your room.")
            Kitchen.door("kitchen")

        else:
            print(invalid)
            Bedroom.player_awake("Awake")

    def player_room(self):
        print("You find yourself standing in your room and you find 3 things to choose from [PC],[Door], and [Bed]")
        ans = input("> ")
        if ans == "Bed":
            print("You go to sleep")
            Actions.print_slow("........................................................................\n")
            Bedroom.player_awake("Awake")
        elif ans == "PC":
            Bedroom.player_pc("PC")
        elif ans == "Door":
            print("You open the door and walkout")
            Kitchen.door("standing")
        else:
            print(invalid)
            Bedroom.player_room("standing")

    def player_pc(self):
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
            Bedroom.player_room("standing")

        else:
            print(invalid)
            Bedroom.player_pc("PC")


class Kitchen():

    def door(self):
        Single_events.mom_intro("talk")

        print("You enter the living room What would you like to do now?"
              "\n[A] Eat Mom's delicious breakfast!"
              "\n[B] Talk to Mom."
              "\n[C] Leave the house.")
        ans = input("> ")
        if ans == "A":
            Kitchen.breakfast("delicious")
        elif ans == "B":
            pass  # Home.mom(talk)
        elif ans == "C":
            Kitchen.left_without_breaky("lol u are dead")
        else:
            print(invalid)
            Kitchen.door("standing")

    def mom(self):
        pass # This is where I will put her dialogue options
    def left_without_breaky(self):
        print("You're really going to leave without eating Mom's famous breakfast? [Y] or [N]")
        ans = input("> ")
        if ans == "Y":
            print("You're absolutely heartless...")
            tap
            Actions.Player_A.faint("dead")
            Bedroom.player_awake("Awake")
        elif ans == "N":
            print("Good lad, Now go eat that breakfast.")
            Kitchen.door("kitchen")
        else:
            print(invalid)
            Kitchen.left_without_breaky("standing")

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
            Kitchen.fin_breakfast("standing")

    def breakfast(self):
        print("You eat a hearty delicious breakfast and you feel ready to tackle the day.")
        Kitchen.fin_breakfast("full")


class Oak_lab():
    def lobby(self):
        print("You enter the famous Kanto Pokemon Laboratory. What would you like to do next? ")
        print("[A] Look around\n[B] Approach Yash\n[C] Approach Professor Oak")
        ans = input("> ")
        if ans == "A":
            pass  # Actions.look.lab
        if ans == "B":
            pass  # Yash Dialouge
        if ans == "C":
            pass  # professor Oak dialouge



# class First_battle():
#     print("You walk with you new pokemon and a unknown person approaches you...")

# Player_Configuration.player_config("configure")
Bedroom.player_awake("Awake")
# Kitchen.breakfast("kitchen")

