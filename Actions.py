import sys,time,story

def print_slow(str):
    type_speed = 200
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(10.0 / type_speed)


class Player_A():
    def faint(self):
        print_slow("You're head feels light before you know it you fall to the ground, and just like that your vison goes\n"
              "dark\n")
        print_slow("3.....2.....1......You have fainted\n")
        story.tap

    def battle(self):
        print("You are ready to battle. Please make a Choice")
        print("[A} Attack\n[B] Items\n[C] Pokemon\n[D] Run")

