"""
All in character dialouges will be stored in this script.py file, All characters are organized in Alphabet order.
"""
import Actions
def proffesor_diag_1(player_name):
    print(f"Ah... hello {player_name}, my name is Professor Oak")
    Actions.tap()
    print(f"There's a vast world to be explored out there with millions of Pokemon to catch")
    Actions.tap()
    print(f"Are you ready to start your adventure?")
    Actions.tap()
def proffesor_diag_2():
    print("On the table are 3 Pokemon, Please choose wisely... ")
    Actions.tap()
    print("1st we have Chikorita a Grass type")
    Actions.tap()
    print("2nd we have Totodile a Water type")
    Actions.tap()
    print("3rd we have Cyndaquill a Fire type")
    Actions.tap()
def proffesor_diag_3():
    print("Great Pick please take care of them and cherish your Pokemon the rest of your life")
    Actions.tap()
    print("Before I forget go see Yash for your PokeDex")
    Actions.tap()

def yash_diag_1():
        print("Oh Hi there, I'm Yash. I'm pretty busy at the moment. I would go talk to the Professor first.")
        Actions.tap()

def yash_diag_2():
        print("Oh hi there, Oak asked me to give you something?")
        Actions.tap()
        print("... OH RIGHT, here you go.... A Pokedex, you can use it to log and learn more about Pokemon")
        Actions.tap()



def mom_diag_1(player_name):
    print(f"{player_name}, You're finally up! I was worried you were going to sleep the whole day away!")
    Actions.tap()
    print("I wanted to let you know that, Professor Oak wants to talk to you! But you should do that after"
              "\na bit of breakfast.")
    Actions.tap()
def mom_diag_2():
    print("Why hello dear! I'm a little busy with house work so why don't you play outside? ")
    Actions.tap()

