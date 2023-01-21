# Todo:
# Create Mon Class (Ref old_doke/mon_rules.py line 9)
import psycopg2
import random
import csv

class Mon:
    def __init__(self, name:str, level: int, max_hp: int, attack: int, defense:int, speed:int, accuracy:float, evasion:float, element:str
                 ):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.accuracy = accuracy
        self.evasion = evasion
        self.element = element
        self.moves = []
        self.stats = {
            "NAME": str(name),
            "LVL": int(level),
            "HP": int(max_hp),
            "ATK": int(attack),
            "DEF": int(defense),
            "SP": int(speed),
            "EVA": float(evasion),
            "ACC": float(accuracy),
            "ELM": str(element),
            "MVS": list()
        }

elements = [ # List of all mon elements
    'Normal',
    'Fire', 
    'Water',
    'Electric', 
    'Grass', 
    'Ice', 
    'Fighting', 
    'Poison', 
    'Ground', 
    'Flying', 
    'Psychic', 
    'Bug', 
    'Rock', 
    'Ghost', 
    'Dragon', 
    'Dark', 
    'Steel', 
    'Fairy' 
]
suffix = [ # List of suffixes for mon naming
    'claw', 'tooth', 'fang', 'paw', 'talon', 'tail', 'feather', 'wing', 'fist', 'foot', 'digon', 'rax', 'dog', 'fox', 'cat', 'lion', 'monkey', 'eagle', 'parrot'
    ]

def create_names() -> list: # generates mon names
    mon_dex = []

    for i in elements:
        for _ in range(3):
            name = i + random.choice(suffix)
            if name not in mon_dex:
                mon_dex.append(name)
            else:
                pass
    return mon_dex

def init_mon_dex() -> list: # ensures mon_dex is full
    mon_dex = []
    while True:
        mon_dex = create_names()
        if len(mon_dex) == 54:
            break
        else:
            continue
    return mon_dex

def create_mon_objects(): # generates mon_objects
    mon_names = init_mon_dex()
    mon_dex = []

    for i in mon_names:
        name = i
        for j in elements:
            if j in name:
                element = j
        level = 5
        max_hp = random.randint(18, 25)
        attack = random.randint(30, 50)
        defense = random.randint(30,50)
        speed = random.randint(20, 40)
        accuracy = 1.0
        evasion = 1.0

        mon = Mon(name, level, max_hp, attack, defense, speed, accuracy, evasion, element)

        mon_dex.append(mon)
    
    return mon_dex

mon_dex = create_mon_objects()
# def write_to_db():
