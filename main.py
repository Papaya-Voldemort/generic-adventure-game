import utils
import time
import random

waitTime = 3.5
name = "tung tung tung sahur".title()
loadBool = False

def playGame():
    print("Welcome to gamename")
    time.sleep(waitTime)
    name = input("What is your name?\n:").strip().title()
    while name == "" or name.isnumeric():
        if name.isnumeric():
            print("Do your parents not love you?")
            time.sleep(waitTime)
        print("Invalid name. Please try again.")
        time.sleep(waitTime)
        utils.clrscreen()
        name = input("What is your name?\n:").strip().title()
    utils.clrscreen()
    print(f"Hi {name}!")
    time.sleep(waitTime * 2)


utils.loading(loadBool)
playGame()