# PROJECT 1: SNAKE, WATER, GUN GAME
'''We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.'''

import random   # Used to generate random choices for the computer.
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a Draw")

else:

    if(computer==-1 and you==1):
        print("you win!")

    elif(computer==-1 and you==0):
        print("you lose!")

    elif(computer==1 and you==-1):
        print("you lose!")

    elif(computer==1 and you==0):
        print("you win!")

    elif(computer==0 and you==-1):
        print("you win!")

    elif(computer==0 and you==1):
        print("you lose!")

    else:
        print("Something went wrong")

