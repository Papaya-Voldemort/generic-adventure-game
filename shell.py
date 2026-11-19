commands = {
    "help":{
        'action':"list avalable commands and what they do"
    },
 #   "man":{
 #       'action':"explain in detail what a specific command does and its syntax"
 #   },
    "clear":{
        'action':"clears the screen"
    },
    "exit":{
        'action':"exit your current shell"
    }
}

def help():
    for i in commands:
        commandname = i
        print(f"{i}")
        print(f"    run the command {i} to {commands[i]['action']}")
        print()

def man(comm):
    print("access and print manpage for command <comm> from respective .txt")