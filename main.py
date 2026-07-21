# MESSAGE TO OTHER DEVS:
# please run the command '!test' before submitting a pull request. (note that this command does take a number of loops as an argument, but please run it a minimum of 1000 (default number) times)
# even if you are very confident in your skills, we all make mistakes
# use !clear_dev to clear the dev_log.md file

import time
import os
from datetime import datetime
from generators import variable_maker
from commands import commands

def main():
    """
    This is where the magic happens! main() reads the user input, checks if it is a command (and runs the command if it is), 
    generates an NPC based on the user input, saves the NPC to the log.txt file and prints it out.
    """
    try:
        timestamp: str = datetime.now().strftime("%d.%m.%Y %H:%M")
    except Exception:
        timestamp: str = "???"

    #Check if the files 'log.txt', 'log_prev.txt' and "dev_log.md" can be accessed
    do_log: bool = True
    dev_log: bool = True
    try:
        with open("log.txt", "a") as f:
            pass
        with open("log_prev.txt", "a") as f:
            pass
    except (PermissionError, IOError):
        do_log = False

    try:
        with open("dev_log.log", "a") as f:
            pass
    except (PermissionError, IOError):
        dev_log = False

    #Make sure that the files can actually be written to
    if os.access("log.txt", os.W_OK):
        pass
    else:
        do_log = False
    if os.access("log_prev.txt", os.W_OK):
        pass
    else:
        do_log = False
    if os.access("dev_log.log", os.W_OK):
        pass
    else:
        dev_log = False


    #Overrides 'log_prev.txt' with the contents of 'log.txt' and clears 'log.txt' for usage
    if do_log == True:
        if os.path.exists("log.txt"):
            with open("log.txt", "r") as old_file:
                content: str = old_file.read()
            with open("log_prev.txt", "w") as file:
                file.write(content)
        with open("log.txt", "w") as file:
            file.write(f"this log was generated at {timestamp}\n\n")
    

    print("""if any values does not have a valid input, it will use default values
    Input structure: [Name], [Race], [Gender], [Age], [IsChild Y/N], [MaxAge], [MatureAge], [Job], [AdultJob Y/N]

    NPCs will be saved to the 'log.txt' file in the directory (folder) the program is stored in, allowing you to access NPCs from the last session
    NPCs from the session before that are stored in 'log_prev.txt' as a safety net.

    if this is your first time using this tool or you need a refresher, please type !help
    to quit, type !quit
        
    Press Enter to start generating!
    """)
    print("")

    #If the program can't access/create the 'log.txt' or 'log_prev.txt' files, it prints this warning
    if do_log == False:
        print("\033[1;5;4;91mCOULD NOT CREATE LOG FILE, THE PROGRAM WILL STILL FUNCTION BUT GENERATED NPCS WILL NOT BE SAVED\033[0m")
        print("\033[2;5;31mplease check if the program has the permissions required to create files in the current directory or start it as an administrator\033[0m")

    while True:

        user_input = input("").strip()
    

        #Check if the user input is a command
        if user_input.startswith("!"):
            parts = user_input.split(" ")
            part_pad = [""] * 4
            parts += part_pad
            com = parts[0]
            arg = parts[1]
            commands(com, arg) 
            continue

        specifications = user_input.split(",")
        
        padding = [""] * 32
        specifications += padding
        
        gender, race, sub_race, name, age, profession, stats, stats_clean, speech_quirk, lore1, lore2, lore3, lore4, personality = variable_maker(specifications)
        #Store the NPC in the log file
        if do_log == True:
            with open("log.txt", "a") as file:
                file.write(f"""
Name: {name} ({gender})
Age: {age}
Race: {race} {sub_race}
Profession: {profession}
Stats: {stats_clean}
Speech Quirk: {speech_quirk}
Reputation: {lore1} {lore2}
Lore: {lore3} {lore4}
Personality: {personality[0]}, {personality[1]}
                """)
        
        print("\033[8;37mNPC STAT BLOCK:\033[0m")
        time.sleep(0.1)
        print(f"\033[0;32mName:\033[0m {name} ({gender})")
        time.sleep(0.1)
        print(f"\033[0;36mAge:\033[0m {age}")
        time.sleep(0.1)
        print(f"\033[0;34mRace:\033[0m {race} {sub_race}")
        time.sleep(0.1)
        print(f"\033[0;35mProfession:\033[0m {profession}")
        time.sleep(0.1)
        print(f"\033[0;31mStats:\033[0m {stats}")
        time.sleep(0.1)
        print(f"\033[0;32mSpeech Quirk:\033[0m {speech_quirk}")
        time.sleep(0.1)
        print(f"\033[0;36mReputation:\033[0m {lore1} {lore2}")
        time.sleep(0.1)
        print(f"\033[0;34mLore:\033[0m {lore3} {lore4}")
        time.sleep(0.1)
        print(f"\033[0;35mPersonality:\033[0m {personality[0]}, {personality[1]}")


if __name__ == "__main__":
    main()
