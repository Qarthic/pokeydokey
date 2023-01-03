# Step 2 of generating poke's: Assing type and randomize stats

# from data import moves
from generate_names_01 import generate_file
from moves import create_moveset_list
import csv
import random

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

generate_pokemon()
