help_commands = """
help - stop it, get some help
start - starts the engine
stop - stops the engine
rules - rules (not 34)
nudes - will send u ashe maree nudes
quit - dont even think about it
"""
play_command = "wroom-wroom.."
rules_command = "rule 63: every character has... wait, wrong page\nrule 1: no rules"
state = False

print("hewwo.. uwu owo.. i dont want to help u but type help if u want")

while True:
    user_input = input().lower()
    if user_input.__contains__("help"):
        print(help_commands)
    elif user_input.__contains__("start") and state == True:
        print("dude its already wroom wroom-ing wtf")
    elif user_input.__contains__("start"):
        print(play_command)
        state = True
    elif user_input.__contains__("rules"):
        print(rules_command)
    elif user_input.__contains__("stop") and state == False:
        print("dude its already stoped wtf")
    elif user_input.__contains__("stop"):
        print("wrooooom.... stoped")
        state = False
    elif user_input.__contains__("nudes"):
        print("gotem")
    elif user_input.__contains__("quit"):
        print("all i wanted from life is goth anime bitch")
        break
    else:
        print("i dunno what u just typed")