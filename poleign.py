import argparse
import time
import os
import requests
import json
import easygui
from playsound import playsound

# Hellian Praticing Mode

def hellianeasy():
    os.system("cls")
    print("You selected Easy mode for Hellian, now let's start in 4 second")
    time.sleep(4)
    print("Follow Aim in bots for 5 Minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    os.system("cls")
    for i in range(301):
        print(f"Follow Aim in bots for {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do One tap for bots for 8 minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(481):
        print(f"Follow Aim in bots for {i}/480 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do Standart Flick for 5 minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(301):
        print(f"Do Standart Flick {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do double flick for 8 minutes. starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(481):
        print(f"Do double flick {i}/480 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    for i in range(301):
        print(f"get some rest {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Try to hit more than 8 bots in the Medium difficulty section. Press Enter if you did.")
    os.system("pause > nul")
    print("Try to hit more than 2 bots in the Hard difficulty section. Press Enter if you did.")
    os.system("pause > nul")
    for i in range(301):
        print(f"get some rest {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Solve the spike twice on Medium  mode. Press Enter if you did.")
    os.system("pause > nul")
    print("Place the spike twice in Medium mode and try to protect it. Press Enter if you did.")
    os.system("pause > nul")
    print("Play deathmatch 2 times. This is last task to compelete.")
    os.system("pause > nul")
    print("You compeleted the tasks, thank you for using. Have a nice day!")
    time.sleep(5)
    exit()

def helliannormal():
    os.system("cls")
    print("You selected Medium mode for Hellian, now let's start in 4 second")
    time.sleep(4)
    print("Follow Aim in bots for 5 Minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    os.system("cls")
    for i in range(301):
        print(f"Follow Aim in bots for {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do One tap for bots for 8 minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(481):
        print(f"Follow Aim in bots for {i}/480 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do Standart Flick for 5 minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(301):
        print(f"Do Standart Flick {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do double flick for 8 minutes. starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(481):
        print(f"Do double flick {i}/480 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    for i in range(301):
        print(f"get some rest {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Try to hit more than 15 bots in the Medium difficulty section. Press Enter if you did.")
    os.system("pause > nul")
    print("Try to hit more than 6 bots in the Hard difficulty section. Press Enter if you did.")
    os.system("pause > nul")
    for i in range(301):
        print(f"get some rest {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Solve the spike twice on Hard  mode. Press Enter if you did.")
    os.system("pause > nul")
    print("Place the spike twice in Hard mode and try to protect it. Press Enter if you did.")
    os.system("pause > nul")
    print("Play deathmatch 2 times. This is last task to compelete.")
    os.system("pause > nul")
    print("You compeleted the tasks, thank you for using. Have a nice day!")
    time.sleep(5)
    exit()

def hellianhard():
    os.system("cls")
    print("You selected Hard mode for Hellian, now let's start in 4 second")
    time.sleep(4)
    print("Follow Aim in bots for 5 Minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    os.system("cls")
    for i in range(301):
        print(f"Follow Aim in bots for {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do One tap for bots for 10 minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(601):
        print(f"Follow Aim in bots for {i}/480 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do Standart Flick for 5 minutes. Starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(301):
        print(f"Do Standart Flick {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Do double flick for 10 minutes. starting timer for 5 seconds.")
    time.sleep(5)
    for i in range(601):
        print(f"Do double flick {i}/480 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    for i in range(301):
        print(f"get some rest {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Try to hit more than 25 bots in the Medium difficulty section. Press Enter if you did.")
    os.system("pause > nul")
    print("Try to hit more than 13-15 bots in the Hard difficulty section. Press Enter if you did.")
    os.system("pause > nul")
    for i in range(301):
        print(f"get some rest {i}/300 Second")
        time.sleep(1)
        os.system("cls")
    playsound('notif.wav')
    print("Solve the spike twice on Hard  mode. Press Enter if you did.")
    os.system("pause > nul")
    print("Place the spike twice in Hard mode and try to protect it. Press Enter if you did.")
    os.system("pause > nul")
    print("Play deathmatch 2 times. This is last task to compelete.")
    os.system("pause > nul")
    print("You compeleted the tasks, thank you for using. Have a nice day!")
    time.sleep(5)
    exit()

# Miyagi Praticing Mode

def miyagieasy():
    os.system("cls")
    print("You selected Easy mode for Miyagi. Now let's start for 5 second.")
    time.sleep(5)
    print("Destroy 15 bots in Easy Mode with sheriff. Press Enter if you did.")
    os.system("pause > nul")
    print("Destroy 6 bots in Medium Mode with sheriff. Press Enter if you did.")
    os.system("pause > nul")
    print("Target 50 bots in Target Mode with Guardian. Plase Open Strafe Mode too. Press Enter if you did.")
    os.system("pause > nul")
    print("Play 1-2 DeathMatch, if you see a man, do the strafe like the bots do, if the man can't shoot you with a gun, shoot him. Press Enter if you did.")
    os.system("pause > nul")
    print("You compeleted the tasks, thank you for using. Have a nice day!")
    time.sleep(5)
    exit()

def miyaginormal():
    os.system("cls")
    print("You selected Easy mode for Miyagi. Now let's start for 5 second.")
    time.sleep(5)
    print("Destroy 30 bots in Easy Mode with sheriff. Press Enter if you did.")
    os.system("pause > nul")
    print("Destroy 15 bots in Medium Mode with sheriff. Press Enter if you did.")
    os.system("pause > nul")
    print("Target 50 bots in Target Mode with Guardian. Plase Open Strafe Mode too. Press Enter if you did.")
    os.system("pause > nul")
    print("Play 1-2 DeathMatch, if you see a man, do the strafe like the bots do, if the man can't shoot you with a gun, shoot him. Press Enter if you did.")
    os.system("pause > nul")
    print("You compeleted the tasks, thank you for using. Have a nice day!")
    time.sleep(5)
    exit()

def miyagihard():
    os.system("cls")
    print("You selected Easy mode for Miyagi. Now let's start for 5 second.")
    time.sleep(5)
    print("Destroy 30 bots in Easy Mode with sheriff. Press Enter if you did.")
    os.system("pause > nul")
    print("Destroy 30 bots in Medium Mode with sheriff. Press Enter if you did.")
    os.system("pause > nul")
    print("Target 50 bots in Target Mode with Guardian. Plase Open Strafe Mode too. Press Enter if you did.")
    os.system("pause > nul")
    print("Play 1-2 DeathMatch, if you see a man, do the strafe like the bots do, if the man can't shoot you with a gun, shoot him. Press Enter if you did.")
    os.system("pause > nul")
    print("You compeleted the tasks, thank you for using. Have a nice day!")
    time.sleep(5)
    exit()











def main():
    parser = argparse.ArgumentParser(description='Commands')
    parser.add_argument('-p', '--parametre', metavar='Mode', type=str, help='Poligon Praticing Mode')
    parser.add_argument('-d', '--diger_parametre', metavar='Difficulty', type=str, help='Difficulty Mode To be easier or harder')
    args = parser.parse_args()
    print("Checking for updates")
    fetchUpdateUrl = "https://poleign.glitch.me/b1.json"
    fetchUrlToUpdate = requests.get(fetchUpdateUrl)
    data = json.loads(fetchUrlToUpdate.text)
    fetchUrlToUpdate.raise_for_status()
    checkUpdate = data['UpToDate']
    if checkUpdate == "Required":
        easygui.msgbox("You are using old version of Poleign. You can download latest version for new features and bug patches.", title="Update Checker")
        os.system("start https://github.com/benilyasss/Poleign")
    else: 
        print("You are using Last version of Poleign")
    
    if args.parametre == "Hellian":
        print("Using Hellian Poligon")
    elif args.parametre == "Miyagi":
        print("Using Esport Poligon")
    else:
        print("Error you didnt used -p= or you used it wrongly")
    
    
    if args.diger_parametre == "Easy":
        if args.parametre == "Hellian":
            hellianeasy()
        if args.parametre == "Miyagi":
            miyagieasy()
    elif args.diger_parametre == "Medium":
        if args.parametre == "Hellian":
            helliannormal()
        if args.parametre == "Miyagi":
            miyaginormal()
    elif args.diger_parametre == "Hard":
        if args.parametre == "Hellian":
            hellianhard()
        if args.parametre == "Miyagi":
            miyagihard()
    else: 
        print("Error you didnt used -d= or you used it wrongly")

if __name__ == "__main__":
    main()
