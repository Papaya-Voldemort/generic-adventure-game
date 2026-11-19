commands = {
    "help":{
        'action':"list avalable commands and what they do"
    },
    "man":{
        'action':"explain in detail what a specific command does and its syntax"
    }
}

def help():
    for i in commands:
        commandname = i
        print(f"{i}")
        print(f"    run the command {i} to {commands[i]['action']}.")
        print()

help()