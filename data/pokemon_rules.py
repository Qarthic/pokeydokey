# Step 1 in generating poke's: Create name 

import csv
import random

# Pokemon Class

class Pokemon:
    def __init__(self, name: str, element: str, level: int, max_hit_points: int, attack: int, defense: int, speed: int, evasion: float, accuracy: float, moves: list):
        self.name = name
        self.element = element
        self.level = level
        self.max_hit_points = max_hit_points
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.evasion = evasion
        self.accuracy = accuracy
        self.moves = moves


# Generate Names START

prefix = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Fly', 'Ghost', 'Grass', 'Ground', 'Ice', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']
suffix = ['claw', 'tooth', 'fang', 'paw', 'talon', 'tail', 'feather', 'wing', 'fist', 'foot', 'digon', 'rax']

# creates random names from above data
def create_names():
    num_to_create = int(input("Input a number: "))
    pokedex = []

    for _ in range(num_to_create):
        name = random.choice(prefix) + random.choice(suffix)
        if name not in pokedex:
            pokedex.append(name)
        else: 
            pass
    return pokedex

# generates .csv file from create_names function
def generate_file():
    pokedex = create_names()
    filename = input("What would you like to name the file: ")

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name'])

        for i in pokedex:
            writer.writerow([i])

    return filename

# Generate Names STOP

# Generate Moves START

class Move:
  def __init__(self, pp, name, element, target):
    self.pp = int(pp)
    self.name = str(name)
    self.element = str(element)
    self.target = str(target)

class Damaging(Move):

    def __init__(self, pp: int, name: str, element: str, target: str, power: float, accuracy: float):
        super().__init__(pp, name, element, target)
        self.power = float(power)
        self.accuracy = float(accuracy)

    # To-do: Import Pokemon to determine power when hitting a target

    def crit_check(self):
        if random.randrange(0, 255) in range(0, (P.speed/2)):
            return True
        else:
            return False

    def attack(self):
        if random.randrange(0, 100) in range(0, (P.accuracy * 100)):
            self.target.hp - ((self.power + P.attack) * self.target.defense)

class Buff_Debuff(Move):
    def __init__(self, pp: int, name: str, buff: bool, target: str, stage: int, stat: str):
        super().__init__(pp, name, bool(buff), target)
        self.stage = int(stage)
        self.stat = stat
    
    def attack(self):
        if random.randrange(0, 100) in range(0, (P.accuracy * 100)):
            modified_stat = self.stat
            if self.buff == True: 
                modified_stat += (self.stage / 10)
            else: 
                modified_stat -= (self.stage / 10)


water_gun = Damaging(25, "Water Gun", "Water", "Foe", .4, 1)
bullet_punch = Damaging(30, "Bullet Punch", "Steel", "Foe", .3, 1)
rock_tomb = Damaging(15, "Rock Tomb", "Rock", "Foe", .6, .95)
confusion = Damaging(25, "Confusion", "Psychic", "Foe", .5, 1)
sludge = Damaging(20, "Sludge", "Poison", "Foe", .65, 1)
tackle = Damaging(35, "Tackle", "Normal", "Foe", .4, 1)
growl = Buff_Debuff(40, "Growl", True, "Foe", 1, "Attack")
leer = Buff_Debuff(30, "Leer", False, "Foe", 1, "Defense")
powder_snow = Damaging(25, "Powder Snow", "Ice", "Foe", .4, 1)
bulldoze = Damaging(20, "Bulldoze", "Ground", "Foe", .6, 1)
sand_attack = Buff_Debuff(15, "Sand Attack", False, "Foe", 1, "Accuracy")
razor_leaf = Damaging(25, "Razor Leaf", "Grass", "Foe", .55, .95)
shadow_sneak = Damaging(30, "Shadow Sneak", "Ghost", "Foe", .4, 1)
gust = Damaging(35, "Gust", "Flying", "Foe", .4, 1)
ember = Damaging(25, "Ember", "Fire", "Foe", .4, 1)
rock_smash = Damaging(15, "Rock Smash", "Fighting", "Foe", .4, 1)
fairy_wind = Damaging(30, "Fairy Wind", "Fairy", "Foe", .4, 1)
thunder_shock = Damaging(30, "Thunder Shock", "Electric", "Foe", .4, 1)
twister = Damaging(20, "Twister", "Dragon", "Foe", .4, 1)
bite = Damaging(25, "Bite", "Dark", "Foe", .6, 1)
struggle_bug = Damaging(20, "Struggle Bug", "Bug", "Foe", .5, 1)

move_list = [water_gun, bullet_punch, rock_tomb, confusion, sludge, tackle, growl, leer, powder_snow, bulldoze, sand_attack, razor_leaf, shadow_sneak, gust, ember, rock_smash, fairy_wind, thunder_shock, twister, bite, struggle_bug]

element = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Fly', 'Ghost', 'Grass', 'Ground', 'Ice', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

def create_moveset_list():
    move_set = {}
    for i in element: 
        move_set[i] = []
        for j in move_list:
            if j.element == i:
                move_set[i].append(j)
        move_set[i].append(growl)
        move_set[i].append(leer)
        move_set[i].append(sand_attack)
    return move_set

# Generate moves STOP

# Generate final pokedex file START

element = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Fly', 'Ghost', 'Grass', 'Ground', 'Ice', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

def extract_from_file(file):
    
    with open(file, 'r') as dex_file:
        reader = csv.reader(dex_file)
        working_list = []

        for row in reader:
            working_list.append(row)
        return working_list 

def generate_pokemon():
    poke_data = extract_from_file(generate_file())
    move_set = create_moveset_list()

    with open('pokedex.csv', 'w', newline='') as pokedex:
        writer = csv.writer(pokedex)
        
        writer.writerow(['Name', 'Element', 'Level', 'Max HP', 'Attack', 'Defense', 'Speed', 'Accuracy', 'Evasion', 'Moves'])

        for mon in poke_data:
            mon = mon[0]
            max_hp = random.randint(19, 23)
            attack = random.randint(30, 50)
            defense = random.randint(30, 50)
            speed = random.randint(20, 40)
            accuracy = 1.0
            evasion = 1.0

            if mon == 'name':
                pass
            else:
                for i in element:
                    if i in mon:
                        moves = move_set[i]
                        writer.writerow([str(mon), i, 5, max_hp, attack, defense, speed, accuracy, evasion, moves])
        finished = "Pokedex generated. Good luck Mr. Ketchum! "
        return finished

# generate_pokemon()

# Generate final pokedex file STOP

