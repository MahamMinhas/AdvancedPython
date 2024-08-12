import random


game=["rock", "paper", "scissors"]

system=random.choice(game)
user=input("Select an option: 1. Rock   2. Paper  3. Scissors:  ")

if(user=="Rock"):
    if(user==system):
        print("Tie")
    elif(user != system):
        if(user and system=="Paper"):
            print(f"Better Luck Next Time! {system} vs. {user}")
        else:
            print(f"Woohoo!! You Won {system} vs. {user}")

elif(user=="Paper"):
    if(user==system):
        print("Tie")
    elif(user != system):
        if(user and system=="Scissors"):
            print(f"Better Luck Next Time! {system} vs. {user}")
        else:
            print(f"Woohoo!! You Won {system} vs. {user}")
            
else:
    if(user==system):
        print("Tie")
    elif(user != system):
        if(user and system=="Rock"):
            print(f"Better Luck Next Time! {system} vs. {user}")
        else:
            print(f"Woohoo!! You Won {system} vs. {user}")
