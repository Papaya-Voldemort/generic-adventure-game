import utils
import time
import random
import shell
import shutil

name = "tung tung tung sahur"
fname = "brr brr patapim"
loadBool = False
pkgs = []

def pacman(package):
    print("resolving dependencies...")
    time.sleep(.125)
    print("looking for conflicting packages...")
    time.sleep(.125)
    print()
    print(f"Packages (1) gameshore-26.12.1")
    print()
    print(f"Total Installed Size: {random.uniform(1.3,5.79):.2f} GiB")
    print()
    proceed = input(":: Proceed with installation? [Y/n]").strip().capitalize()
    if proceed == "N":
        return
    else:
        print("(1/1) checking keys in keyring")
    pkgs.append(package)


def terminal(user,device):
    print("welcome to msh!\nfor a list of commands, type help")
    while True:
        prompt = input(f"[{user.lower()}@{device}] ~ ").strip()
        lprompt = prompt.split()
        mcomm = lprompt[0]
        if prompt == "help":
            shell.help()
        elif "ssh rocky@192.168.42.73" == prompt:
            time.sleep(.125)
            terminal("rocky","portable-earth-thinking-machine")
        elif "man" == mcomm:
            shell.man(prompt.split())
        elif "clear" == mcomm:
            utils.clrscreen()
        elif "exit" == mcomm:
            return
        elif user == "rocky" and prompt == "sudo pacman -S gameshore":
            pacman("gameshore")
        else:
            print(f"msh: command not found: {mcomm}")
        if user == fname:
            print("remember that rocky's ip address is 192.168.42.73")
            

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
    print("He also uses Arch Linux [btw]")
    utils.wait()
    print("At least he plans on paying you quite well.")
    utils.wait(True)
    print("You will need to use his package manager (pacman) to install the GameShore CLI.")
    utils.wait()
    print("")
    utils.wait(True)
    terminal(fname, "office1-desktop")


utils.loading(loadBool)
playGame()
