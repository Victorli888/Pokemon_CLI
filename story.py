import sys,time,random
type_speed = 750
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(10.0/type_speed)


print("Welcome to the world of Pokemon! Where we enslave animals big "
           "and large to fight for our entertainment")
class Player_Configuration():
    def __init__(self, player_name, player_gender):
        self.player_name = player_name
        self.player_gender = player_gender  # I need to check whether or not this stuff is necessary
    def player_config():

        print("\nPlease tell me are you a Boy or a Girl?")
        player_gender = input("> ")

        if player_gender == "Boy" or player_gender == "Girl":
            print(player_gender)

        else:
            print("That's not what I asked for...")
            Player_Configuration.player_config()

        print("ahhh I see. Please tell me your name")
        player_name = input("> ")
        print_slow(f"Ok {player_name} welcome to Pallet Town your Pokemon Journey starts now!")

class Pallet_Town(Player_Configuration):
    def player_home(self):
        print("You wake up in comfortable bed in room that Mom always keeps clean. You see a [PC],[Door], and [Bed].")
        ans = input("> ")
        if ans == "Bed":
            print("It's like 11AM are you sure you want to  go back to bed?")
            print("[A] Yes I am sad and I want to go back to bed. or [B] No I'm going to do something today.")
            ans = input("> ")
            if ans == "A":
                print("Congratulations you wasted an entire day!~~~")
                Pallet_Town.player_home("Awake")
            elif ans == "No":
                print("That's the spirit!")
                Pallet_Town.player_home("Awake")
        elif ans == "PC":
            pass

        elif ans == "Door":
            pass

        else:
            print("That is not a valid section please try again.")
            Pallet_Town.player_home("Awake")





# Player_Configuration.player_config()
Pallet_Town.player_home("Awake")


