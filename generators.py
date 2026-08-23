import random
from datetime import datetime
from data import SUPPORTED_RACES, RACE_DATA, GENERIC_PERSONALITIES
from rep_lore_gen import *

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


def generate_stats(personality: list, profession: str) -> tuple[str, str]:
    def stat_generator() -> int:
        stat_list = [random.randint(1, 6) for _ in range(4)]
        stat_list.sort()
        return sum(stat_list[1:])

    # Base stats
    stats = {
        "str": stat_generator(),
        "dex": stat_generator(),
        "con": stat_generator(),
        "int": stat_generator(),
        "wis": stat_generator(),
        "cha": stat_generator(),
    }

    # Personality Modifiers
    pers_mods = {
        "stressed": {"con": -1},
        "depressed": {"cha": -2},
        "arrogant": {"cha": -4},
        "intelligent": {"int": 4},
        "cunning": {"int": 2},
        "honest": {"cha": 1},
        "deceitful": {"cha": 2},
        "analytical": {"int": 1},
        "dumb": {"int": -3},
        "annoying": {"cha": -4},
        "violent": {"str": 2},
        "shy": {"cha": -1}
    }

    # Profession Modifiers
    prof_mods = {
        "farmer": {"str": 2, "con": 1, "dex": 1, "wis": -1},
        "blacksmith": {"str": 2, "con": 1, "dex": 1, "wis": -1, "cha": -1},
        "cleric": {"wis": 1, "cha": 2},
        "paladin": {"con": 2, "str": 2, "dex": -1, "int": -1},
        "knight": {"con": 2, "str": 1, "dex": -1},
        "guard": {"con": 1, "str": 1},
        "merchant": {"cha": 3, "wis": 1, "con": -1, "str": -1},
        "wandering trader": {"cha": 2, "wis": 1, "str": -1},
        "magician": {"wis": 2, "int": 1, "dex": 1, "con": -1},
        "wizard": {"wis": 5, "int": 5, "str": -3, "dex": -2, "con": -2},
        "lumberjack": {"str": 2, "con": 1},
        "tailor": {"dex": 2, "int": 1},
        "stonemason": {"str": 2, "con": 1},
        "fisherman": {"str": 1, "dex": 1, "con": 1},
        "tax collector": {"cha": -2, "int": 1},
        "armourer": {"str": 1, "con": 1},
        "cook": {"con": 1, "dex": 1},
        "servant": {"dex": 1, "cha": -1},
        "dyer": {"int": 1, "con": 1},
        "goldsmith": {"dex": 2, "int": 1},
        "librarian": {"int": 3, "wis": 1, "str": -2},
        "messenger": {"dex": 2, "con": 1},
        "miller": {"str": 1, "con": 1},
        "apprentice": {"int": 1},
        "student": {"int": 2, "str": -1}
    }

    # Apply Personality
    for trait in personality:
        mods = pers_mods.get(trait.lower(), {})
        for stat, val in mods.items():
            stats[stat] += val

    # Apply Profession
    mods = prof_mods.get(profession.lower(), {})
    for stat, val in mods.items():
        stats[stat] += val

    # Floor at 1
    for key in stats:
        stats[key] = max(1, stats[key])

    s = stats # shorthand for the return string
    display = f"\033[1;37mStr\033[0m [{s['str']}], \033[1;37mDex\033[0m [{s['dex']}], \033[1;37mCon\033[0m [{s['con']}], \033[1;37mInt\033[0m [{s['int']}], \033[1;37mWis\033[0m [{s['wis']}], \033[1;37mCha\033[0m [{s['cha']}]"
    plain = f"Str [{s['str']}], Dex [{s['dex']}], Con [{s['con']}], Int [{s['int']}], Wis [{s['wis']}], Cha [{s['cha']}]"
    
    return display, plain

def generate_speech_quirk() -> str:
    """
    Generate a speech quirk to make the NPC more memorable.
    """
def generate_speech_quirk() -> str:
    quirks: list = [
        "with a germanic accent", "with a british accent", "with a french accent", "with an italian accent",
        "in a nervous manner", "in a serious manner", "quickly", "slowly", "with stutter", "with confidence",
        "like a snake", "in whispers", "in a loud voice", "in a quiet voice", "monotone", "in a bored tone"
    ]


    forbidden_groups = [
        {"with a germanic accent", "with a british accent", "with a french accent", "with an italian accent", "monotone"},
        {"in a nervous manner", "in a serious manner"},
        {"quickly", "slowly"},
        {"in a nervous manner", "with confidence"},
        {"with a stutter", "with confidence"},
        {"in whispers", "in a loud voice", "in a quiet voice"},
        {"with a stutter", "in a bored tone", "monotone"},
        {"in a nervous manner", "in a bored tone"},
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
    lore1, lore1_cat, personality1 = generate_lore()
    lore2: str = generate_lore_2(lore1_cat)
    rep1, personality2 = generate_rep()
    lore_tags = personality1 + personality2
    extra_traits = random.sample(GENERIC_PERSONALITIES, 3)
    pool = list(set(lore_tags + extra_traits))
    personality = random.sample(pool, 2)
    stats, stats_clean = generate_stats(personality, profession)
    speech_quirk: str = generate_speech_quirk()
    return gender, race, sub_race, name, age, profession, stats, stats_clean, speech_quirk, lore1, lore2, rep1, personality
