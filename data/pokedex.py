# Dictionary of Pokemon and their stats

# from data import moves
import csv
import random


class Pokemon:
    def __init__(self, name, type, level, max_hit_points, attack, defense, speed):
        self.name = str(name)
        self.type = str(type)
        self.level = int(level)
        self.max_hit_points = int(max_hit_points)
        self.attack = int(attack)
        self.defense = int(defense)
        self.speed = int(speed)



type = ['fire', 'water', 'ice', 'grass', 'dark', 'ghost', 'fly', 'rock', 'ground', 'steel', 'fairy', 'fighting', 'electric', 'poison', 'bug', 'dragon', 'psychic']

def extract_from_file(file):
    with open(file, 'r') as dex_file:
        reader = csv.reader(dex_file)
        working_list = []

        for row in reader:
            working_list.append(str(row))
        return working_list 

def generate_pokemon():
    poke_data = extract_from_file('dex_1.csv')
    
    with open('pokedex.csv', 'w', newline='') as pokedex:
        writer = csv.writer(pokedex)
        
        writer.writerow(['Name', 'Type', 'Level', 'Max HP', 'Attack', 'Defense', 'Speed'])

        for mon in poke_data:
            print(mon)
            max_hp = random.randint(19, 23)
            attack = random.randint(30, 50)
            defense = random.randint(30, 50)
            speed = random.randint(20, 40)

            if mon == 'name':
                pass
            else:
                for i in type:
                    if i in mon:
                        writer.writerow([str(mon), i, 5, max_hp, attack, defense, speed])


generate_pokemon()


# class Bulbasaur: # 
#   def __init__(self):
#     self.name = "Bulbasaur"
#     self.id = 1
#     self.type = "Grass"
#     self.moves = [moves.tackle, moves.growl]
#     self.level = 5
#     self.max_hp = 39
#     self.max_atk = 52
#     self.max_def = 43
#     self.max_spd = 65



