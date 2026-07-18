import os
import sys
from datetime import datetime
from generators import variable_maker

def commands(user_input: str, argument: str):
    """
    Works but needs improvement.
    Please only add new commands if you deem they are necessary.
    """
    if user_input.lower() == "!help":
        print("""
    \033[1;39mInput structure:\033[0m [Name], [Race], [Gender], [Age], [IsChild Y/N], [MaxAge], [MatureAge], [Job], [AdultJob Y/N]
            
    \033[1;39mExample Command:\033[0m Scales, Dragonborn, Female, 32, Y, MaxAge,,Blacksmith,
    \033[1;39mExample Command Output:\033[0m
        \033[0;32mName:\033[0m Scales
        \033[0;36mAge:\033[0m 32
        \033[0;34mRace:\033[0m Dragonborn
        \033[0;35mProfession:\033[0m Blacksmith
        \033[0;31mStats:\033[0m Str [9], Dex [14], Con [12], Int [11], Wis [10], Cha [11]
        \033[0;32mSpeech Quirk:\033[0m Speaks like a snake and breathily
        \033[0;36mLore:\033[0m they lost their village to a lich and they fled from it
    
    As you can see, you do not need to fill out every field, some fields are not required!
        (if a field that \033[1;39mis\033[0m required is left empty, it will generate a value)
    
    You may also notice that each individual entry is seperated by a Comma. 
    If you forget to do this, the program \033[1;39mwill\033[0m read every single input as part of the name.
    
    If you want to leave an info field empty, simply do not type any character between the commas.
    
    This program is made to handle not giving any input;
    if you simply press enter without giving any information, the program generates a fully random NPC.
    
    \033[1;39mSome values cannot be manually input!\033[0m
    Complex values like lore or stats cannot be entered by the user, the reason for this is that
    this program is meant to quickly generate NPCs for the GM during a TTRPG session, not to make pre-planned
    NPC stat blocks
    
    \033[1;39mWhat does each input do?\033[0m
    [Name] - \033[2;39mWill be used as the name of the NPC\033[0m
                \033[2;39m- Will generate a race specific name if not specified\033[0m
    [Race] - \033[2;39mWill be used as the race of the NPC\033[0m
                \033[2;39m- Will generate a race if not specified\033[0m
                \033[2;39m- If the race is not supported by the generator, it will be treated as a Human\033[0m
    [Gender] - \033[2;39mWill be used as the gender of the NPC\033[0m
                \033[2;39m- Will generate a gender if not specified\033[0m
                \033[2;39m- If the gender is anything besides 'Male' or 'Female' it will be changed to 'Non-Binary'\033[0m
    [Age] - \033[2;39mWill be used as the age of the NPC\033[0m
                \033[2;39m- Will generate a race specific age if not specified\033[0m
    [IsChild] - \033[2;39mDetermines what age range the generator uses when generating Age\033[0m
                \033[2;39m- Ignored if Age is specified\033[0m
                \033[2;39m- Will default to 'No' if not specified\033[0m
                \033[2;39m- 'Yes', 'No', 'Y', 'N' are all valid inputs (not case sensitive)\033[0m
    [MaxAge] - \033[2;39mOverrides the maximum age if specified\033[0m
                \033[2;39m- Ignored if IsChild is set to Yes or Age is specified\033[0m
                \033[2;39m- If specified, the generator will ignore all Age presets of the NPC's race,\033[0m
                \033[2;39m  it instead generates a random age in the range of [MatureAge] and [MaxAge]\033[0m
    [MatureAge] - \033[2;39mOverrides Mature Age if specified\033[0m
                \033[2;39m- Ignored if age is specified\033[0m
                \033[2;39m- This is the age at which your NPC's race reaches maturity (E.g. 18 for Humans)\033[0m
                \033[2;39m- Used as the minimum age when generating an adult and the maximum age when\033[0m
                \033[2;39m  generating a child\033[0m
    [Job] - \033[2;39mWill be used as the profession of the NPC if specified\033[0m
                \033[2;39m- Will generate a profession if not specified\033[0m
                \033[2;39m- Will generate a profession from a unique set of professions if not specified\033[0m
                \033[2;39m  and 'IsChild' is set to 'Yes'\033[0m
    [AdultJob] - \033[2;39mForces an adult job to be used\033[0m
                \033[2;39m- Ignored if 'isChild' is set to 'No'\033[0m
                \033[2;39m- Forces the generator to pick a profession from the Adult profession Table\033[0m
                \033[2;39m  even if 'IsChild' is set to 'Yes'\033[0m
            """)
    elif user_input.lower() == "!test":
        def tester(TestNum: int, specifications: list):
            with open("dev_log.log", "a") as dev_file:
                try:
                    variable_maker(specifications)
                    print(f"\033[0;92mTEST {TestNum} SUCCESS\033[0m")
                    dev_file.write(f"TEST {TestNum} SUCCESS\n")
                except Exception as e:
                    dev_file.write(f"TEST {TestNum} FAILED - {str(e)}\n")
                    print(f"\033[0;91mTEST {TestNum} FAILED\033[0m")
        try:
            loops: int = int(argument)
        except:
            loops: int = 1000
        specifications: list = []
        padding = [""] * 32
        specifications += padding
        counter: int = 1

        with open("dev_log.log", "a") as dev_file:
            dev_file.write(f"--- Test Session: {datetime.now()} ---\n")
            while counter <= loops:
                try:
                    variable_maker(specifications)
                    dev_file.write(f"Loop {counter}. SUCCESS\n")
                    print(f"\033[0;92mLOOP SUCCESS {counter}\033[0m")
                except Exception as e:
                    dev_file.write(f"Loop {counter}: FAILED - {str(e)}\n")
                    print(f"\033[0;91mLOOP FAILED {counter}\033[0m")
                
                counter += 1

        tester(1, ["Name", "Race", "Gender", "Age", "N", "MaxAge", "MatureAge", "Job", ""])
        tester(2, ["1200494", "W.D. Gaster", "Pain", "Age", "D20", "-100", "10", "Dungeon Master", "Nothing to see here"])
        tester(3, ["", "", "", "", "", "", "", "", ""])
        tester(4, ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        tester(5, ["☺", "☻", "♥", "♦", "♣", "♠", "•", "◘", "○"])
        tester(6, ["\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n"])
        tester(7, ["A" * 1000])
        tester(8, [",,,,,,,,"])
        tester(9, ["Name", "Race", "Gender", "9999999999999999999999999999999999999999999999999999999", "N", "9999999999999999999999999999999999999999999999999999999", "9999999999999999999999999999999999999999999999999999999", "Job", ""])
        tester(10, ["\033[1;91m", "\033[1;91m", "\033[1;91m", "\033[1;91m", "\033[1;91m", "\033[1;91m", "\033[1;91m", "\033[1;91m", "\033[1;91m", "\033[1;91m"])
        tester(11, ["", "", "", "", "", "100", "10", "", ""])
        tester(12, ["", "", "", "", "y", "100", "10", "", ""])
        
        print("\033[1;97mYOUR CODE WORKS\033[0m")

    if user_input.lower() == "!quit":
        sys.exit()

    if user_input.lower() == "!clear_dev":
        with open("dev_log.log", "w") as file:
            file.write("")
    
