
import sys
sys.path.append("pokeydokey\data")

from data import pokemon_rules as pr
import random

pokedex = pr.extract_from_file("pokedex.csv")

element = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Fly', 'Ghost', 'Grass', 'Ground', 'Ice', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

def display_options():
    print("1. Bug       5. Fairy        9. Ghost        13. Poison      17. Water\n2. Dark      6. Fighting     10. Grass       14. Psychic\n3. Dragon    7. Fire         11. Ground      15. Rock        \n4. Electric  8. Fly          12. Ice         16. Steel\n")

def create_mon_object(mon):
    mon = pr.Pokemon(mon[0], mon[1], mon[2], mon[3], mon[4], mon[5], mon[6], mon[7], mon[8], mon[9])
    return mon

def vowel(mon) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if mon.name[0] in vowels:
        answer = f"an {mon.name}"
        return answer
    else:
        answer = f"a {mon.name}"
        return answer

def player_pick_mon() -> pr.Pokemon:
    print(f"Hello adventurer! What element 'mon would you like to choose?")
    display_options()

    player_choice = input("-> ")
    try:
        int(player_choice)
    except:
        player_choice = input("Invalid selection. Please choose 1, 2, or 3.\n-> ")

    player_choice = element[int(player_choice)-1]
    print(f"You've decided on a {player_choice} type 'mon.\n")

    n = random.randrange(1, 41)
    choose_dex = pokedex[n::]

    for num, i in enumerate(choose_dex):
        if choose_dex[num][1] == player_choice:
            player_mon = create_mon_object(i)
            print(f"You have selected {vowel(player_mon)}")
            return player_mon


def computer_pick_mon() -> pr.Pokemon:
    print("Now your rival will select their 'mon.\n")

    randselection = int(random.randrange(1, len(pokedex)))
    computer_mon = create_mon_object(pokedex[randselection])

    print(f"Your rival has selected {vowel(computer_mon)}")

    return computer_mon

my_mon = player_pick_mon()
comp_mon = computer_pick_mon()
