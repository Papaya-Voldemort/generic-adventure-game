import utils
import time
import random
import shell


name = "tung tung tung sahur"
fname = "brr brr patapim"
loadBool = False

def terminal(user,device):
    utils.clrscreen()
    print("welcome to msh!\nfor a list of commands, type help")
    while True:
        prompt = input(f"[{user.lower()}@{device}] ~ ").strip()
        lprompt = prompt.split()
        mcomm = lprompt[0]
        if prompt == "help":
            shell.help()
        elif "ssh rocky@192.168.42.73" == prompt:
            terminal("rocky","portable-earth-thinking-machine")
        elif "man" == mcomm:
            shell.man(prompt.split())
        elif "clear" == mcomm:
            utils.clrscreen()
        elif "exit" == mcomm:
            return
            

def playGame():
    print("Welcome to CorpNet IT Helpdesk")
    utils.wait()
    name = input("What is your name?\n:").strip().title()
    while name == "" or name.isnumeric():
        if name.isnumeric():
            print("Do your parents not love you?")
            utils.wait()
        print("Invalid name. Please try again.")
        utils.wait(True)
        name = input("What is your name?\n:").strip().title()
    fname = name.split(maxsplit=1)[0]
    utils.clrscreen()
    print(f"Hi {name}!")
    utils.wait()
    print("You have a VERY VERY important task today.")
    utils.wait()
    print("Today you must help Rocky download GTA IV")
    utils.wait()
    print("He plans to take all of December off due to a *sudden* cold.")
    print("( ͠° ͟ʖ ͡°)")
    utils.wait()
    print("However, your client is approxamatley 16.3 light years away on Erid and the only connection you have to his computer is a remote shell.")
    utils.wait()
    print("You will have to SSH into his computer and install GTA IV using the GameShore CLI")
    utils.wait()
    print("At least he plans on paying you quite well.")
    terminal(fname, "office1-desktop")


utils.loading(loadBool)
playGame()
