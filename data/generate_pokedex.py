import csv
import random

prefix = ['fire', 'water', 'ice', 'grass', 'dark', 'ghost', 'fly', 'rock', 'ground', 'steel', 'fairy', 'fighting', 'electric', 'poison', 'bug', 'dragon', 'psychic']
suffix = ['claw', 'tooth', 'fang', 'paw', 'talon', 'tail', 'feather', 'wing', 'fist', 'foot', 'digon', 'rax']

# creates random names from above data
def create_names():
    num_to_create = int(input())
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
    filename = input()

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name'])

        for i in pokedex:
            writer.writerow([i])

    return filename

generate_file()