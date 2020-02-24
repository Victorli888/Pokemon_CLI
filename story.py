print("Welcome to the world of Pokemon! Where we enslave animals big and large to fight and perform for our pleasure")

def player_config():
    global gender
    print("Please tell me are you a Boy or a Girl?")
    gender = input("> ")

    if gender == "Boy" or gender == "Girl":
            print(gender)

    else:
        print("That's not what I asked for...")
        player_config()

    print("ahhh I see. Please tell me your name")

