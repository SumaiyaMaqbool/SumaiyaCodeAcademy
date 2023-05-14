from random import *
x = randint(1,100)
while (True):
    user_input = int (input ("Guess a number between 1 and 100 : "))

    if (user_input>100 or user_input<1 ):
        print ("Your guess is ouside the range")
    elif (user_input>x):
        print ("Go lower")
    elif (user_input<x):
        print("Go higher")
    elif (user_input==x):
        print("Congratualtion you win")
        break
    else:
        print("Invalid entry")
