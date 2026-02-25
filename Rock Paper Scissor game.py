# Rock Paper & Scissor game
import random

print("==========Welcome to Avsharma's Rock Paper Scissor Game==========")

while True:

    # starting point
    starting = str(input("Type S for Starting & N for Quite: "))
    if starting == "S" or starting == "s":
        print("===== Most Welcome you =====")
        system = random.choice([0, 1, 2])
        myoption = int(input("Enter your choice(Rock/Paper/Scissor): "))
        options = {0: "Rock", 1: "Paper", 2: "Scissor"}
        me = options[myoption]
        computer = options[system]
        print(f"You choose {me}")
        print(f"Computer choose {computer}")

        if system == myoption:
            print("Oh! Match draw Bro...")
        else:
            if system == 0 and myoption == 1:
                print("Hurrah! You win the match Bro...")
            elif system == 0 and myoption == 2:
                print("Oh! You loose the match Bro...")
            elif system == 1 and myoption == 0:
                print("Oh! You loose the match Bro...")
            elif system == 1 and myoption == 2:
                print("Hurrah! You win the match Bro...")
            elif system == 2 and myoption == 0:
                print("Hurrah! You win the match Bro...")
            elif system == 2 and myoption == 1:
                print("Oh! You loose the match Bro...")
            else:
                print("I think you wanna quite the game")

    else:

        print("Oh! Ok bye Bro")
        break



