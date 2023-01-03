# Dictionary of Pokemon and their stats

# from data import moves
import csv
import random

element = ['fire', 'water', 'ice', 'grass', 'dark', 'ghost', 'fly', 'rock', 'ground', 'steel', 'fairy', 'fighting', 'electric', 'poison', 'bug', 'dragon', 'psychic']

def extract_from_file(file):
    with open(file, 'r') as dex_file:
        reader = csv.reader(dex_file)
        working_list = []

        for row in reader:
            working_list.append(row)
        return working_list 

def generate_pokemon():
    poke_data = extract_from_file('dex_1.csv')
    
    with open('pokedex.csv', 'w', newline='') as pokedex:
        writer = csv.writer(pokedex)
        
        writer.writerow(['Name', 'element', 'Level', 'Max HP', 'Attack', 'Defense', 'Speed', 'Accuracy', 'Evasion'])

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
                        writer.writerow([str(mon), i, 5, max_hp, attack, defense, speed, accuracy, evasion])


generate_pokemon()
