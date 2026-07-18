#Storing generic race variables outside of the dictionary because multiple entries use them
GENERIC_MALE: list = ["Greg", "Steffan", "John", "Steve", "Baradun", "Bodger", "Maro", "Herg", "Hans", "Vincent", "Adrian", "Tate", "Daniel", "Danny", "Joe", "Ben", "Leon", "Leonard", "Benedict", "Adam", "Aidan", "Christian", "Florian", "Ned", "James", "Noah", "Matt", "Matheo", "Aron", "Elias", "Eliah", "Theo", "Theodore", "Paul", "Liam", "Olly", "Oliver", "Luca", "Kris", "Ash", "Alex", "Taylor", "Tolv", "Barney", "Bartholamew", "Bart", "Mathide", "Gunther"]
GENERIC_FEMALE: list = ["Olivia", "Charlotte", "Emma", "Ammi", "Amelia", "Luna", "Dess", "Noelle", "Jane", "Elizabeth", "Ace", "Rose", "Donna", "Martha", "Amy", "Clara", "Bill", "Billie", "Sarah", "Sandy", "Laura", "Lilly", "Zara", "Tamara", "Lilith", "Mara", "Lora", "Susie", "Melodie", "River", "Kris", "Ash", "Alex", "Taylor", "Natty", "Elga", "Helga", "Mathide", "Liz"]
GENERIC_MIDDLE: list = ["Van", "Vor", "Quinn", "Sage", "Blake", "Reese", "Ellis", "Gera", "Lari", "Kris", "Mario", "Ash", "Liv", "Korra", "Sorg", "Libbith", "Lee"]
GENERIC_LAST: list = ["Everwind", "Rockfell", "Walker", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Galindor", "Bramblecrack", "Treefell", "Everwood", "Toadfolk", "Risinger", "Cerola", "Ernst", "Dreemurr", "Everwinter", "Mulligan", "Vance", "Kleiner", "Barth"]

#If a race just uses the "Generic" entry in the dictionary, pelase do not add it to this list
SUPPORTED_RACES: list = ["Elf", "Dwarf", "Gnome", "Giant", "Goliath", "Orc", "Dragonborn", "Half-Elf", "Half-Orc", "Tiefling", "Kobold", "Warforged"]

#This dictionary stores all the race data
RACE_DATA: dict = {
    "Generic": {
        "names": {
            "male": GENERIC_MALE,
            "female": GENERIC_FEMALE,
            "middle": GENERIC_MIDDLE,
            "last": GENERIC_LAST,
        },
        "ages":{
            "max": 100,
            "child": 18,
            "min": 5,
        },
        "sub_races": None,
    },
    "Elf": {
        "names": {
            "male": ["Kydelius", "Marius", "Laridius", "Morad", "Linus", "Quintus", "Legolas", "Barodius", "Quandronus", "Listrius", "Leonard", "Torien", "Taradius", "Rowius", "Agarius", "Elowen", "Thaloin", "Harodius", "Vincent"],
            "female": ["Clariette", "Luna", "Rose", "River", "Elodie", "Laureen", "Isolde", "Zara", "Lyria", "Scara", "Korria", "Korra", "Lillith", "Iz", "Achilda", "Zillith", "Mali"],
            "middle": ["Lora", "Lore", "Matri", "Vor", "Silbien"],
            "last": ["Everwind", "Neverflow", "Shimmerfall", "Arcanius", "Flowerbloom", "Everwild", "Undertree", "Bloomfind", "Icebreak"],
        },
        "ages":{
            "max": 750,
            "child": 100,
            "min": 10,
        },
        "sub_races": ["High Elf", "Wood Elf", "Drow"],
    },
    "Dwarf": {
        "names": {
            "male": ["Nardol", "Niergo", "Horg", "Barag", "Lormish", "Borg", "Bodger", "Fred", "Mart"],
            "female": ["Nardie", "Niergie", "Horgie", "Baragie", "Lormie", "Borgie", "Bodgie", "Frederine", "Martie"],
            "middle": ["Of", "Vor", "Van", "Horog", "Skulltra"],
            "last": ["Dolomite", "Rockeater", "Skullbreaker", "Limestone", "Emerald", "Sulfur", "Ruby", "Sapphire"],
        },
        "ages":{
            "max": 350,
            "child": 50,
            "min": 8,
        },
        "sub_races": None,
    },
    "Gnome": {
        "names": {
            "male": ["Unome", "Trome", "Gerome", "Grome", "Stome", "Wome", "Fenome", "Zome"],
            "female": ["Unome", "Trome", "Gerome", "Grome", "Stome", "Wome", "Fenome", "Zome"],
            "middle": GENERIC_MIDDLE, #gnomes don't have unique middle names
            "last": ["Shroomhide", "Leafsteal", "Stealthstorm", "Treeclimb", "Minish"],
        },
        "ages":{
            "max": 350,
            "child": 25,
            "min": 6,
        },
        "sub_races": ["Forest Gnome", "Rock Gnome"],
    },
    "Giant": {
        "names": {
            "male": ["Galindor", "Grommash", "Kargath", "Dargor", "Azrog", "Brick", "Thyrm", "Bergelmir", "Melgroth"],
            "female": ["Galindor", "Grommash", "Kargath", "Dargor", "Azrog", "Brick", "Thyrm", "Bergelmir", "Melgroth"],
            "middle": GENERIC_MIDDLE,
            "last": ["Rockbreaker", "Stoneeater", "Blooddrinker", "Treepuncher", "Dirteater", "Mud"],
        },
        "ages":{
            "max": 800,
            "child": 50,
            "min": 7,
        },
        "sub_races": ["Cloud Giant", "Fire Giant", "Frost Giant", "Hill Giant", "Stone Giant", "Storm Giant"],
    },
    "Goliath": {
        "names": {
            "male": ["Galindor", "Grommash", "Kargath", "Dargor", "Azrog", "Thyrm", "Bergelmir", "Melgroth", "Darium", "Zabeth", "Sterob", "Glireth", "Zaraboth"],
            "female": ["Maritha", "Zaratroth", "Trithty", "Zlithra", "Sartha", "Trithity", "Glicera", "Griffy", "Tarita"],
            "middle": ["Za", "Yi", "Zu", "Yu", "Zor", "Yagi", "Zan"],
            "last": ["Rockbreaker", "Stoneeater", "Blooddrinker", "Treepuncher", "Dirteater", "Mud"],
        },
        "ages":{
            "max": 95,
            "child": 16,
            "min": 5,
        },
        "sub_races": ["Cloud Giant", "Fire Giant", "Frost Giant", "Hill Giant", "Stone Giant", "Storm Giant"],
    },
    "Orc": {
        "names": {
            "male": ["Galindor", "Grommash", "Kargath", "Dargor", "Azrog", "Brick", "Thyrm", "Bergelmir", "Melgroth", "Grog", "Larg", "Trommer"],
            "female": ["Galindor", "Grommash", "Kargath", "Dargor", "Azrog", "Brick", "Thyrm", "Bergelmir", "Melgroth"],
            "middle": GENERIC_MIDDLE,
            "last": ["Rockbreaker", "Stoneeater", "Blooddrinker", "Treepuncher", "Dirteater", "Mud", "Mountmover", "Cavedigger"],
        },
        "ages":{
            "max": 80,
            "child": 12,
            "min": 4,
        },
        "sub_races": None,
    },
    "Dragonborn": {
        "names": {
            "male": ["Scales", "Arjahn", "Donaar", "Kriv", "Nadarr", "Torrin", "Rhogar", "Ghesh", "Mehdrash", "Shamash"],
            "female": ["Akra", "Biri", "Daar", "Farideh", "Harann", "Havilar", "Jehri", "Kava", "Korinn", "Mishann"],
            "middle": ["Vor", "Van", "Of"], # Dragonborn will ALWAYS have a dragonborn middle name
            "last": ["Adderblood", "Thunderbringer", "Firebring", "Furytooth", "Landfall"],
        },
        "ages":{
            "max": 80,
            "child": 15,
            "min": 4,
        },
        "sub_races": ["Black (Acid)", "Blue (Lightning)", "Green (Poison)", "Red (Fire)", "White (Cold)", "Brass (Fire)", "Bronze (Lightning)", "Copper (Acid)", "Gold (Fire)", "Silver (Cold)"]
    },
    "Halfling": {
        "names": {
            "male": GENERIC_MALE,
            "female": GENERIC_FEMALE,
            "middle": GENERIC_MIDDLE,
            "last": GENERIC_LAST,
        },
        "ages":{
            "max": 150,
            "child": 20,
            "min": 5,
        },
        "sub_races": None,
    },
    "Half-Elf": {
        "names": {
            "male": ["Kydelius", "Marius", "Laridius", "Morad", "Linus", "Quintus", "Legolas", "Barodius", "Quandronus", "Listrius", "Leonard", "Torien", "Taradius", "Rowius", "Agarius", "Elowen", "Thaloin", "Harodius", "Vincent"],
            "female": ["Clariette", "Luna", "Rose", "River", "Elodie", "Laureen", "Isolde", "Zara", "Lyria", "Scara", "Korria", "Korra", "Lillith", "Iz", "Achilda", "Zillith", "Mali"],
            "middle": ["Lora", "Lore", "Matri", "Vor", "Silbien"],
            "last": ["Everwind", "Neverflow", "Shimmerfall", "Arcanius", "Flowerbloom", "Everwild", "Undertree", "Bloomfind", "Icebreak"],
        },
        "ages":{
            "max": 200,
            "child": 20,
            "min": 6,
        },
        "sub_races": None,
    },
    "Half-Orc": {
        "names": {
            "male": ["Galindor", "Grommash", "Kargathor", "Dargo", "Azorog", "Brigg", "Thierm", "Burgemhyr", "Meltrogroth", "Grog", "Lard", "Trom"],
            "female": ["Galinde", "Gromma", "Kargad", "Dagor", "Asrogg", "Baggi", "Thyrmi", "Bergel", "Melgro"],
                        "middle": ["Thyr", "Odin", "Freyr", "Freya", "Loki", "Thor", "Baldur"],
            "last": ["Rockbreaker", "Stoneeater", "Blooddrinker", "Treepuncher", "Dirteater", "Mud", "Mountmover", "Cavedigger"],
        },
        "ages":{
            "max": 80,
            "child": 14,
            "min": 4,
        },
        "sub_races": None,
    },
    "Tiefling": {
        "names": {
            "male": ["Gareti", "Sparati", "Norbi", "Irand", "Lorbit", "Zaron", "Lebtro", "Sato", "Mirot", "Laffi"],
            "female": ["Oberra", "Sparri", "Nastasha", "Larati", "Oroba", "Tasha", "Exrotta"],
            "middle": ["Satan", "Arerorer", "Loam", "Helo"],
            "last": ["Hellhunt", "Firebring", "villagerend", "Forestburn", "Hellhound", "Demise"],
        },
        "ages":{
            "max": 150,
            "child": 18,
            "min": 6,
        },
        "sub_races": ["Abyssal", "Chtonic", "Infernal"]
    },
    "Kobold": {
        "names": {
            "male": ["Bezzler", "Larcen", "Muri", "Arso", "Eft", "Buse", "Raud", "Assu", "Extor", "Terro"],
            "female": ["Aboci", "Famici", "Filici", "Fratci", "Maritici", "Matrici", "Parici", "Senci", "Suici", "Homici", "Genici"],
            "middle": ["Infrac", "Midemen", "Felo"],
            "last": ["Incars", "Fino", "Restut", "Forfe", "Probat", "Curf", "Exceut"],
        },
        "ages":{
            "max": 120,
            "child": 6,
            "min": 2,
        },
        "sub_races": None,
    },
    "Warforged": {
        "names": {
            "male": GENERIC_MALE,
            "female": GENERIC_FEMALE,
            "middle": ["Bot", "Puter", "Lator", "Vice"],
            "last": GENERIC_LAST,
        },
        "ages":{
            "max": 10000,
            "child": 30,
            "min": 18,
        },
        "sub_races": None
    },
}
