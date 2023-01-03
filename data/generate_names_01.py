# Step 1 in generating poke's: Create name 

import csv
import random

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

