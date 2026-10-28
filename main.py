# TODO:
# - add settings

import time
from datetime import datetime
from generators import variable_maker
from commands import commands
from colorama import init
from base import do_log, Dev_Write, Read_Setting, Initial
import traceback
import sys
from printer import Print_NPC

Initial()

def main():
    """
    This is where the magic happens! main() reads the user input, checks if it is a command (and runs the command if it is), 
    generates an NPC based on the user input, saves the NPC to the log.txt file and prints it out.
    """
    init(autoreset=True)

    Dev_Write(f"\n\n <[Session: {datetime.now()}]> \n")

    print("""if any values does not have a valid input, it will use default values
    Input structure: [Name], [Race], [Gender], [Age], [IsChild Y/N], [MaxAge], [MatureAge], [Job], [AdultJob Y/N]

    NPCs will be saved to the 'log.txt' file in the directory (folder) the program is stored in, allowing you to access NPCs from the last session
    NPCs from the session before that are stored in 'log_prev.txt' as a safety net.

    if this is your first time using this tool or you need a refresher, please type \033[1;39m!help\033[0m
    to quit, type \033[1;39m!quit\033[0m
    for a list of other commands, type \033[1;39m!commands
    \033[0m
        
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
            commands(parts[0], parts[1], parts[2]) 
            continue

        specifications = user_input.split(",")
        
        padding = [""] * 32
        specifications += padding

        Dev_Write("--<| GENERATING VARIABLES |>--")
        
        try:
            gender, race, sub_race, name, age, profession, stats, stats_clean, speech_quirk, lore1, lore2, rep, personality = variable_maker(specifications)
            Dev_Write("generated successfully")
        except Exception as e:
            Dev_Write("Failed to generate:" + traceback.format_exc() + "")
            print("ERROR DURING GENERATION: " + f"{e}")
            sys.exit()

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
        Reputation: {rep}
        Lore: {lore1} {lore2}
        Personality: {personality[0]}, {personality[1]}
                """)

        Print_NPC(gender, race, sub_race, name, age, profession, stats, stats_clean, speech_quirk, lore1, lore2, rep, personality)

if __name__ == "__main__":
        main()
