import random
from datetime import datetime
from data import SUPPORTED_RACES, RACE_DATA, GENERIC_PERSONALITIES

def generate_gender(gender: str = "") -> str:
    """
    Generates a gender. "Non-Binary" has a lower chance to generate than "Male" and "Female".
    """
    if gender.lower() not in ["male", "female", "non-binary", "nonbinary"]:
        weights: list = [3, 3, 1]
        gender = random.choices(["Male", "Female", "Non-Binary"], weights=weights, k=1)[0]
    
    return gender

def generate_race(race: str= "") -> str:
    """
    Generates a race. Some races have lower chances to generate than others, humans have the highest chance to generate.
    """
    if race == "":
        weights: list = [10, 8, 8, 8, 2, 8, 8, 8, 2, 8, 7, 7, 5, 1]
        race = random.choices(["Human", "Halfling", "Elf", "Dwarf", "Gnome", "Giant", "Goliath", "Orc", "Dragonborn", "Half-Elf", "Half-Orc", "Tiefling", "Kobold", "Warforged"], weights=weights, k=1)[0]
    else:
        pass

    return race

def generate_name(name: str = "", race: str = "", gender: str = "") -> str:
    """
    Generates a name. Names are race specific (with a chance to use a generic name instead).
    """
    first_name_type: int = random.randint(1, 4)
    has_middle_name: int = random.randint(1, 8)
    middle_name_type: int = random.randint(1, 4)
    last_name_type: int = random.randint(1, 4)
    full_name = ""
    race = race.title()
    
    if name != "":
        return(name)
    if race in SUPPORTED_RACES:
        #First name generator for supported races
        if first_name_type <= 3:
            if gender.lower() in ["male", "female"]:
                full_name += random.choice(RACE_DATA[race]["names"][gender.lower()])
            else:
                full_name += random.choice(RACE_DATA[race]["names"]["male"] + RACE_DATA[race]["names"]["female"])
        else:
            if gender.lower() in ["male", "female"]:
                full_name += random.choice(RACE_DATA["Generic"]["names"][gender.lower()])
            else:
                full_name += random.choice(RACE_DATA["Generic"]["names"]["male"] + RACE_DATA["Generic"]["names"]["female"])

        #Middle name generator for supported races
        if has_middle_name == 8:
            if middle_name_type <= 2 or race.title() == "Dragonborn":
                full_name += f" {random.choice(RACE_DATA[race]["names"]["middle"])}"
            else:
                full_name += f" {random.choice(RACE_DATA["Generic"]["names"]["middle"])}"

        #Last name generator for supported races
        if last_name_type <= 3:
            full_name += f" {random.choice(RACE_DATA[race]["names"]["last"])}"
        else:
            full_name += f" {random.choice(RACE_DATA["Generic"]["names"]["last"])}"
    else:
        #First name generator for unsupported races
        if gender.lower() in ["male", "female"]:
            full_name += random.choice(RACE_DATA["Generic"]["names"][gender.lower()])
        else:
            full_name += random.choice(RACE_DATA["Generic"]["names"]["male"] + RACE_DATA["Generic"]["names"]["female"])

        #Middle name generator for unsupported races
        if has_middle_name == 8:
            full_name += f" {random.choice(RACE_DATA["Generic"]["names"]["middle"])}"
        #Last name generator for unsupported races
        full_name += f" {random.choice(RACE_DATA["Generic"]["names"]["last"])}"
    
    return full_name


def generate_age(race: str = "", age: str = None, child: str = "", m_age: str = None, c_age: str = None) -> int:
    """
    Generates an age. Age ranges are based on race and if the NPC is a child.
    """
    min_age: int = None

    #Convert user input (str) into bool variables
    try:
        max_age: int = int(m_age)
    except Exception:
        max_age = None
    try:
        child_age: int = int(c_age)
    except Exception:
        child_age = None
    try:
        current_age: int = int(age)
    except Exception:
        current_age = None
        
    if child.lower() == "y" or child.lower() == "yes":
        is_child: bool = True
    else:
        is_child = False

    #Make sure that all the variables used in this function are valid values
    if min_age != None:
        if min_age <= 0:
            min_age = 1
    if child_age != None and min_age != None:
        if child_age < min_age:
            child_age = 1
    if max_age != None and child_age != None:
        if max_age < child_age:
            max_age = child_age + 1
        if child_age != None:
                min_age: int = child_age - child_age // 4

    if current_age != None:
        pass
    elif max_age != None and child_age != None and is_child == False:
        current_age = random.randint(child_age, max_age)
    elif max_age != None and child_age != None and is_child == True:
        current_age = random.randint(min_age, child_age)
    elif is_child == False and race.title() in SUPPORTED_RACES:
        current_age = random.randint(RACE_DATA[race.title()]["ages"]["child"], RACE_DATA[race.title()]["ages"]["max"])
    elif is_child == True and race.title() in RACE_DATA["Supported_Races"]:
        current_age = random.randint(RACE_DATA[race.title()]["ages"]["min"], RACE_DATA[race.title()]["ages"]["child"])
    elif is_child == False:
        current_age = random.randint(RACE_DATA["Generic"]["ages"]["child"], RACE_DATA["Generic"]["ages"]["max"])
    elif is_child == True:
        current_age = random.randint(RACE_DATA["Generic"]["ages"]["min"], RACE_DATA["Generic"]["ages"]["child"])
    else:
        raise Exception("something broke in the age generator")
        
    return current_age

def generate_profession(job: str = "", child: str = "", a_job: str = "") -> str:
    """
    Generate a profession. Generates from a unique table if the NPC is a child.
    """
    
    #Convert the user input (str) into bool variables
    if child.lower() == "y" or child.lower() =="yes":
        is_child: bool = True
    else:
        is_child: bool = False

    if a_job.lower() == "y" or a_job.lower() =="yes":
        adult_job: bool = True
    else:
        adult_job: bool = False

    if job == "" and is_child == False or job == "" and adult_job == True:
        job = random.choice(["Farmer", "Blacksmith", "Cleric", "Paladin", "Knight", "Guard", "Merchant", "Wandering Trader", "Magician", "Wizard", "Lumberjack", "Tailor", "Butcher", "Baker", "Stonemason", "Weaver", "Winemaker", "Fisherman", "Shoemaker/Cobbler", "Wheelwright", "Roofer", "Locksmith", "Tanner", "Tax Collector", "Belt Maker", "Armourer", "Cook", "Servant", "Dyer", "Goldsmith", "Hatmaker", "Tailor", "Scrybe", "Tinsmith", "Carter/Coachman", "Birdcatcher", "Painter", "Tavern Keeper", "Sadler", "Messenger", "Ropemaker", "Miller", "Turner", "Gardener", "Barber", "Librarian", "Jobless"])
    elif job == "" and is_child == True:
        job = random.choice(["Student", "Apprentice", "Jobless", "Farmhand", "Assistant"])
    else:
        pass

    return job


def generate_stats() -> tuple[str, str]:
    """
    Generate ability scores based on D&D.
    """
    
    def stat_generator() -> int:
        stat_list: list = []
        for i in range(4):
            stat_list.append(random.randint(1, 6))
            
        stat_list.sort()
        return sum(stat_list[1:])
    
    strength: int = stat_generator()
    dexterity: int = stat_generator()
    constitution: int = stat_generator()
    intelligence: int = stat_generator()
    wisdom: int = stat_generator()
    charisma: int = stat_generator()

    return f"\033[1;37mStr\033[0m [{strength}], \033[1;37mDex\033[0m [{dexterity}], \033[1;37mCon\033[0m [{constitution}], \033[1;37mInt\033[0m [{intelligence}], \033[1;37mWis\033[0m [{wisdom}], \033[1;37mCha\033[0m [{charisma}]", f"Str [{strength}], Dex [{dexterity}], Con [{constitution}], Int [{intelligence}], Wis [{wisdom}], Cha [{charisma}]"

def generate_speech_quirk() -> str:
    """
    Generate a speech quirk to make the NPC more memorable.
    """
def generate_speech_quirk() -> str:
    quirks: list = [
        "with a big mouth", "as if they had something in their throat", 
        "as if they were hiding something", "very fast", "slowly", 
        "everything as if it was a question", "only in rhymes", 
        "with a germanic accent", "with an italian accent", 
        "with a british accent", "with a french accent", 
        "without pausing between words", "every word as written", 
        "hesitantly", "with a stutter", "with a small mouth", 
        "with their mouth closed", "breathily", "just generally strangely", 
        "like a snake", "as if they just finished a marathon", 
        "angrily", "like a detective noir", "in third person", "overly dramatic"
    ]

    forbidden_groups = [
        {"very fast", "slowly", "without pausing between words", "with a stutter"},
        {"with a big mouth", "with a small mouth", "with their mouth closed"},
        {"with a germanic accent", "with an italian accent", "with a british accent", "with a french accent"}
    ]

    while True:
        selection = random.sample(quirks, 2)
        is_invalid = False
        
        for group in forbidden_groups:
            overlap = group.intersection(set(selection))
            if len(overlap) > 1:
                is_invalid = True
                break
        
        if not is_invalid:
            return f"Speaks {selection[0]} and {selection[1]}"

def generate_lore() -> tuple[str, int, list[str]]:
    """
    Generates the first half of the lore string.
    """
    lore: str = ""
    personality_cat: list = []
    secondary_option: int = random.randint(1, 5)
    choose_option: int = random.randint(1, 12)
    match choose_option:
        case 1:
            lore += "they lost their village "
            personality_cat = ["traumatized", "emotionless", "depressed"]
            match secondary_option:
                case 1:
                    lore += "to a fire"
                case 2:
                    lore += "to a natural disaster"
                case 3:
                    lore += f"to {random.choice(["a dragon", "a terrasque", "a wyrm", "a wyvern", "bandits", "a lich", "a war", "plague"])}"
                case 4:
                    lore += "long ago"
                case 5:
                    lore += "a great tragedy"
        case 2:
            lore += "they are known "
            personality_cat = ["smug", "self concious", "annoying"]
            match secondary_option:
                case 1:
                    lore += f"for commiting {random.choice(["arson", "theft", "murder", "robbery", "breaking and entering", "various crimes"])}"
                case 2:
                    lore += "for some reason"
                case 3:
                    lore += f"for {random.choice(["their smile", "their voice", "their kindness", "their rudeness", "protecting the innocent", "their acrobatics", "their sense of humor", "their high (insert highest skill here)"])}"
                case 4:
                    lore += f"to {random.choice(["go on explosive rants", "help others", "trick others", "do backflips and barrel rolls", "tell people to COOL IT", "run around wildly", "tell bad jokes and puns", "not know a lot of things"])}"
                case 5:
                    lore += "among locals"
        case 3:
            lore += "they secretly "
            personality_cat = ["helpful", "shy", "secretive"]
            match secondary_option:
                case 1:
                    lore += "help others"
                case 2:
                    lore += "are running away from their past"
                case 3:
                    lore += f"love {random.choice(["themselves", "hobgoblins", "stealing candy from kids", "just being lazy", "helping others", "wandering in solitude"])}"
                case 4:
                    lore += f"hate {random.choice(["themselves", "hobgoblins", "other races", "their living situation", "helping others", "a party member"])}"
                case 5:
                    lore += "have a crush on a PC"
        case 4:
            lore += "they are on a quest "
            personality_cat = ["devoted", "happy", "determined"]
            match secondary_option:
                case 1:
                    lore += "for vengeance"
                case 2:
                    lore += "for redemption"
                case 3:
                    lore += f"to find {random.choice(["themselves", "their arch nemisis", "their lost lover", "their child", "their pet", "salvation", "a purpose", "solitude"])}"
                case 4:
                    lore += "revive a long lost relative"
                case 5:
                    lore += f"to regain their {random.choice(["honor", "memory", "wisdom", "love"])}"
        case 5:
            lore += "they believe "
            personality_cat = ["gullible", "determined", "passive"]
            match secondary_option:
                case 1:
                    lore += "that they are worthless if they don't achieve something big"
                case 2:
                    lore += "in the gods"
                case 3:
                    lore += f"that they {random.choice(["can change the world", "can do anything", "will cahnge the world", "are important", "are useless", "are intelligent"])}"
                case 4:
                    lore += "that they can trust nobody"
                case 5:
                    lore += "that the party is their enemy"
        case 6:
            lore += "they "
            personality_cat = ["arrogant", "smug", "suspicious"]
            match secondary_option:
                case 1:
                    lore += "behave in suspicious ways"
                case 2:
                    lore += "dont know a lot about the world"
                case 3:
                    lore += f"believe that they are {random.choice(["more important than everyone else", "useless", "a lost cause"])}"
                case 4:
                    lore += "make other people do their work for them"
                case 5:
                    lore += "don't care about what others think of them"
            #The logic below is meant to be inclusive, PLEASE feel free to add to this list, I know that there are a lot of unique gender identities out there.
            #If you have a problem with this piece of code being here because you dislike members of the lgbtq+ community or people with mental disabilities/mental health problems: consider adapting a more loving worldview, hate is not welcome here
        case 7:
            lore += "they are " 
            #these are just 3 random traits I came up with, feel free to change
            personality_cat = ["kind", "depressed", "passive"]
            match secondary_option:
                case 1:
                    lore += f"{random.choice(["autistic", "neurodivergent"])}"
                case 2:
                    lore += f"{random.choice(["homosexual", "bisexual", "pansexual"])}"
                case 3:
                    lore += "introverted"
                case 4:
                    lore += f"{random.choice(["asexual", "aromantic", "aroace"])}"
                case 5:
                    lore += "not who they wish to be"
        case 8:
            lore += "they are known as "
            personality_cat = ["kind", "fearful", "frightening"]
            match secondary_option:
                case 1:
                    lore += f"a {random.choice(["doctor", "master of their craft", "hero", "great one", "criminal", "coward"])}"
                case 2:
                    lore += f"{generate_name()}"
                case 3:
                    lore += "the only survivor of a great war"
                case 4:
                    lore += "a horrible person"
                case 5:
                    lore += "untrustworthy"
        case 9:
            lore += "they recently lost "
            personality_cat = ["depressed", "traumatized", "emotional"]
            match secondary_option:
                case 1:
                    lore += f"a {random.choice(["close friend", "family member", "parent", "lover", "pet"])}"
                case 2:
                    lore += f"their special {random.choice(["Pickaxe", "Hammer", "Spear", "Sword", "Rapier", "Shield", "Axe", "Item"])}"
                case 3:
                    lore += "something important to them"
                case 4:
                    lore += f"their {random.choice(["way of life", "belives", "will to live", "hope", "dreams"])}"
                case 5:
                    lore += "their true love"
        case 10:
            lore += "they keep having "
            personality_cat = ["paranoid", "fearful", "hopeful"]
            match secondary_option:
                case 1:
                    lore += f"nightmares about {random.choice(["a great tragedy", "darkness", "a plaque", "lost love", "death", "the end of the world"])}"
                case 2:
                    lore += f"dreams about {random.choice(["love", "darkness", "light", "a happier life", "a lost family member", "the gods", "wealth"])}"
                case 3:
                    lore += f"thoughts about {random.choice(["suicide", "running away", "following their dreams", "confessing their love", "something far beyond mortals"])}"
                case 4:
                    lore += f"dreams from the perspective of {random.choice(["a deity", "a wild animal", "a different person", "a PC"])}"
                case 5:
                    lore += "difficulty breathing"
        case 11:
            lore += "they dislike "
            personality_cat = ["lonely", "arrogant", "pychopathic"]
            match secondary_option:
                case 1:
                    lore += f"a {random.choice(["local blacksmith", "PC", "local trader", "local ruler", "parent of theirs"])} due to {random.choice(["a minor disagreement", "a confilct of interest", "a conflict of believes", "something minor", "a tragedy"])}"
                case 2:
                    lore += "warlocks"
                case 3:
                    lore += f"talking to the party due to {random.choice(["their attitude", "difference of believes", "a minor disagreement"])}"
                case 4:
                    lore += "their job"
                case 5:
                    lore += "other people"
        case 12:
            lore += f"they {random.choice(["recently ", ""])}heard a rumor "
            personality_cat = ["gullible", "hateful", "greedy"]
            match secondary_option:
                case 1:
                    lore += f"that {random.choice(["dragons", "wizards", "dragonborn", "spellcasters", "the party"])} are {random.choice(["murderers", "criminals", "cultists", "dangerous", "bad people"])}"
                case 2:
                    lore += "everything they care for has been destroyed"
                case 3:
                    lore += f"about {random.choice(["a monster's", "a king's", "a deity's", "a party member's", "the party's"])} {random.choice(["greed", "past", "crimes", "curse", "hate"])}"
                case 4:
                    lore += "about the party"
                case 5:
                    lore += f"of {random.choice(["an incredible treasure", "a horrible curse", "an ancient spell", f"a powerful {random.choice(['warlock', 'wizard', 'sorcerer', 'Paladin', 'Warrior'])}"])}"
        
    return lore, choose_option - 1, personality_cat
    
def generate_lore_2(lore_cat: int) -> str:
    """
    Generates the second half of the lore string, 
    based on the lore_cat variable set in generate_lore().
    """
    lore: str = ""
    secondary_option: int = random.randint(1, 2)
    tertiary_option: int = random.randint(1, 5)
    if secondary_option == 1:
        lore += "and "
    else:
        lore += "but "

        #beware of the evil and intimidating lore cat! /j
    
    match lore_cat:
        case 0: #"they lost their village"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "they promised to rebuild it"
                        case 2:
                            lore += "they fled from it"
                        case 3:
                            lore += "they lost their entire family to it"
                        case 4:
                            lore += "they still mourn"
                        case 5:
                            lore += "they swore to never forget"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "they weren't there when it happened"
                        case 2:
                            lore += "they managed to save almost everyone"
                        case 3:
                            lore += "they hated it there anyways"
                        case 4:
                            lore += "they had something to do with it"
                        case 5:
                            lore += "that was a long time ago"
        case 1: #"they are known"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "have that reputation for a reason"
                        case 2:
                            lore += "don't know about it"
                        case 3:
                            lore += "are trying to get rid of this reputation"
                        case 4:
                            lore += "don't know how they got this reputation"
                        case 5:
                            lore += "that is their biggest achievement in life"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "they don't deserve this reputation"
                        case 2:
                            lore += "have no clue why people think that"
                        case 3:
                            lore += "don't like this reputation"
                        case 4:
                            lore += "only they think that they are known for this"
                        case 5:
                            lore += "that's just a straight-up lie"
        case 2: #"they secretly"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "love to tell people about it"
                        case 2:
                            lore += f"are hiding it {random.choice(['pretty well', 'incredibly well', 'horribly'])}"
                        case 3:
                            lore += "hope that no one can tell"
                        case 4:
                            lore += "hope to keep it a secret"
                        case 5:
                            lore += "they hate it"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "suck at hiding it"
                        case 2:
                            lore += "can't keep a secret"
                        case 3:
                            lore += "don't realize it"
                        case 4:
                            lore += "are desperately trying to hide it"
                        case 5:
                            lore += "no one believes them when they try to tell somebody"
        case 3: #"they are on a quest"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "have recently made great progress"
                        case 2:
                            lore += "refuse to give up, no matter how many obstacles they face"
                        case 3:
                            lore += "just recently started it"
                        case 4:
                            lore += "they just didn't think they could do it... until recently"
                        case 5:
                            lore += "they take it seriously"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "recently faced a major setback"
                        case 2:
                            lore += "they've been busy with other things"
                        case 3:
                            lore += "they have given up on it long ago"
                        case 4:
                            lore += "already failed"
                        case 5:
                            lore += "have no hope of succeeding"
        case 4: #"they believe"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "stand by this"
                        case 2:
                            lore += "refuse to let anyone tell them otherwise"
                        case 3:
                            lore += "will debate anyone who belives in a different worldview"
                        case 4:
                            lore += "love to tell people about this"
                        case 5:
                            lore += "try to apply this to everything"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "are always open to a different worldview"
                        case 2:
                            lore += "that's only what they tell people"
                        case 3:
                            lore += "but only because of tradition"
                        case 4:
                            lore += "don't want people to know about it"
                        case 5:
                            lore += "they also think there is more to the world"
        case 5: #"they"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "no one knows why"
                        case 2:
                            lore += f"this is due to a {random.choice(['recent', 'old', ''])} health issue"
                        case 3:
                            lore += "tell everyone about it"
                        case 4:
                            lore += "refuse to change their ways"
                        case 5:
                            lore += "don't think others notice"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "everyone already knows about this"
                        case 2:
                            lore += "no one believes this to be true"
                        case 3:
                            lore += "they don't think that matters"
                        case 4:
                            lore += "no one else seems to notice"
                        case 5:
                            lore += "that is an obvious lie"
        case 6: #"they are"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "not afraid to admit it"
                        case 2:
                            lore += "are annoyingly vocal about it"
                        case 3:
                            lore += "intentionally hide it"
                        case 4:
                            lore += "want society to become more accepting of people like them"
                        case 5:
                            lore += "think this makes them special"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "are too afraid to tell people about it"
                        case 2:
                            lore += "don't want to admit it"
                        case 3:
                            lore += "don't realize it"
                        case 4:
                            lore += "don't want people to know about it"
                        case 5:
                            lore += "are forced to behave 'normal'"
        case 7: #"they are known as"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "they are the only one that doesn't know this"
                        case 2:
                            lore += "like this name more than their actual name"
                        case 3:
                            lore += "they hate this nickname"
                        case 4:
                            lore += "no one knows where this came from"
                        case 5:
                            lore += "try to keep it a secret"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "they wish this wasn't the case"
                        case 2:
                            lore += "they want people to stop calling them that"
                        case 3:
                            lore += "only close friends get to call them that"
                        case 4:
                            lore += "don't want people to know about it"
                        case 5:
                            lore += "refuse to acknowledge it"
        case 8: #"they recently lost"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "they still mourn this"
                        case 2:
                            lore += "they are responsible for it"
                        case 3:
                            lore += "they blame only themselves for it"
                        case 4:
                            lore += "they blame everyone else for it"
                        case 5:
                            lore += "wish to undo this"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "they refuse to think about it"
                        case 2:
                            lore += "haven't been able to mourn"
                        case 3:
                            lore += "they don't know this yet"
                        case 4:
                            lore += "haven't told anybody about it"
                        case 5:
                            lore += "they actually wanted this to happen"
        case 9: #"they keep having"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "are concerned by this"
                        case 2:
                            lore += "need to tell somebody about it"
                        case 3:
                            lore += "keep bringing it up"
                        case 4:
                            lore += "are trying to hide it"
                        case 5:
                            lore += "are genuinely freaked out by this"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "forget about it every time"
                        case 2:
                            lore += "don't think it's important"
                        case 3:
                            lore += "haven't told anybody"
                        case 4:
                            lore += "this is normal for them"
                        case 5:
                            lore += "they want no one to know"
        case 10: #"they dislike"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "this is just annoying for everyone involved"
                        case 2:
                            lore += "refuse to apologize"
                        case 3:
                            lore += "this is entirely their fault"
                        case 4:
                            lore += "it has ruined their life"
                        case 5:
                            lore += f"this has made them {random.choice(['infamous', 'famous'])}"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "no one really cares"
                        case 2:
                            lore += "they don't act upon it"
                        case 3:
                            lore += "don't tell anybody about it"
                        case 4:
                            lore += "they are able to change"
                        case 5:
                            lore += "there is a greater story behind it"
        case 11: #"they (recently) heard a rumor"
            match secondary_option:
                case 1:
                    match tertiary_option:
                        case 1:
                            lore += "are letting it shape their worldview"
                        case 2:
                            lore += "they are convinced it's true"
                        case 3:
                            lore += "tell people about it"
                        case 4:
                            lore += "it is the only thing they want to talk about"
                        case 5:
                            lore += "didn't think to question it"
                case 2:
                    match tertiary_option:
                        case 1:
                            lore += "they didn't believe it"
                        case 2:
                            lore += "they secretly started it"
                        case 3:
                            lore += "can't quite remember it right"
                        case 4:
                            lore += "hate it"
                        case 5:
                            lore += "think it might only be partially true"

    return lore
def variable_maker(specifications: list) -> tuple[str, str, str, str, int, str, str, str, str, str, str, str, str, list[str, str]]:
    specifications = (specifications + [""] * 9)[:9]
    gender = generate_gender(specifications[2].strip())
    race: str = generate_race(specifications[1].strip())
    sub_race: str = ""
    if race in RACE_DATA and RACE_DATA[race]["sub_races"] != None:
        sub_race = f"({random.choice(RACE_DATA[race]['sub_races'])})"
    name: str = generate_name(specifications[0].strip(), race, gender)
    age: str = generate_age(race, specifications[3].strip(), specifications[4].strip(), specifications[5].strip(), specifications[6].strip())
    profession: str = generate_profession(specifications[7].strip(), specifications[4].strip(), specifications[8].strip())
    stats, stats_clean = generate_stats()
    speech_quirk: str = generate_speech_quirk()
    lore1, lore1_cat, personality1 = generate_lore()
    lore2: str = generate_lore_2(lore1_cat)
    while True:
        lore3, lore3_cat, personality2 = generate_lore()
        if lore3_cat == lore1_cat:
            continue
        break
    lore4: str = generate_lore_2(lore3_cat)
    lore_tags = personality1 + personality2
    extra_traits = random.sample(GENERIC_PERSONALITIES, 3)
    pool = list(set(lore_tags + extra_traits))
    personality = random.sample(pool, 2)
    return gender, race, sub_race, name, age, profession, stats, stats_clean, speech_quirk, lore1, lore2, lore3, lore4, personality
