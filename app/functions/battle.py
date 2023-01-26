# Todo:
# Tie in Mon and Move classes from /app/classes and mon from /functions/generate_mon and /data, and have mon fight. Put together god awful math for types, crits, etc. 

import sys
sys.path.insert(0, '../..')
from app.classes.mon import Mon
from app.classes.move import Move
import time as t
import psycopg2
import msvcrt

class Define_mon_tuple():
    def __init__(self, attributes:tuple) -> None:
        self.attributes = attributes

    def generate_dict(self, attributes):
        mon_dict = {
            "Name": attributes[1],
            "Level": attributes[2],
            "Max HP": attributes[3],
            "HP": attributes[3],
            "Attack": attributes[4],
            "Defense":attributes[5],
            "Speed":attributes[6],
            "Evasion":attributes[7],
            "Accuracy":attributes[8],
            "Element":attributes[9],
            "Moves":attributes[10]
        }

        return mon_dict
        # (9, 'Watertalon', 5, 18, 49, 37, 33, 1.0, 1.0, 'Water', 'Water gun, Growl, Leer, Sand Attack')



element = ""
sql_lib = {
    "ElementNames" : "SELECT element FROM elements;",
    "MonWithElement": f"SELECT * FROM mon WHERE mon_element = "
}

def connector():
    return psycopg2.connect(
        host = "localhost",
        database = "mon_db",
        user = "postgres",
        password = "king1926",
        port = 5432
    )

def sql_get_data(query):
    with connector() as con:
        with con.cursor() as cur:
            cur.execute(query)
    
            db_data = cur.fetchall()
    return db_data

def display_element_options(sql): # Prints numbered options in friendly format
    print("You may pick from the following: \n")
    options = sql_get_data(sql)
    for n, i in enumerate(options):
        element_str = f"{n+1}: {i[0]}"
        if len(element_str) < 8:
            element_str = f"{element_str}\t\t"
        else:
            element_str = f"{element_str}\t"
        print(element_str, end='')
        if (n+1) % 4 == 0:
            print("")
    print("")

def create_element_dict(): # Create list of elements used in player_pick_mon
    options = sql_get_data(sql_lib["ElementNames"])
    element_dict= dict()
    for n, i in enumerate(options):
        element_num = f"{n+1}"
        element_str = f"{i[0]}"
        element_str = element_str.lower()
        element_dict[element_num] = element_str
    return element_dict

def player_pick_element():
    element_options = create_element_dict()
    t.sleep(2)
    player_input = ""
    while player_input not in element_options.keys() or player_input not in element_options.values():
        print("What element Mon would you like? Type 'options' to see the different elements.\n")
        player_input = ""
        player_input = input("Choose an element.")
        player_input = player_input.lower()

        if player_input == 'options':
            display_element_options(sql_lib["ElementNames"])
            t.sleep(1)
            input("Press Enter to continue.")
            print("\nPress Enter to coninue\n")
            continue

        elif player_input in element_options.keys():
            player_input = element_options.get(player_input)
            player_input = player_input.capitalize() # type: ignore
            return player_input
        
        elif player_input in element_options.values():
            player_input = player_input.capitalize()
            return player_input

        elif player_input.lower() == "quit":
            return quit

        else:
            print(f"{player_input} is not an option - please try again.")
            continue

def player_pick_mon():
    player_element = player_pick_element()
    print(f"You've chosen the {player_element} element\n")
    sql_query = sql_lib["MonWithElement"]
    sql_query += f"'{player_element}';"

    mon_choices = sql_get_data(sql_query)

    mon_1 = Define_mon_tuple(mon_choices[0])
    mon_2 = Define_mon_tuple(mon_choices[1])
    mon_3 = Define_mon_tuple(mon_choices[2])
    mon_1 = mon_1.generate_dict(mon_1.attributes)
    mon_2 = mon_2.generate_dict(mon_2.attributes)
    mon_3 = mon_3.generate_dict(mon_3.attributes)

    mon_list = [mon_1, mon_2, mon_3]
    mon_names = [mon_1.get("Name"), mon_2.get("Name"), mon_3.get("Name")]

    print(f"You've got three Mon to choose from: ")
    for n, i in enumerate(mon_list):
            print(f"{n+1}: {i['Name']}\t", end='')
    print('\nWho do you choose?')
    t.sleep(1.5)
    player_mon = ""

    while player_mon not in mon_names:
        player_mon = ""
        player_mon = input("Enter the number or name of your Mon")
        t.sleep(1)

        if player_mon in mon_names:
            player_mon = Mon()


    return


def start_game():
    # Initialize Variables
    player_mon = ""
    computer_mon = ""

    print("Hello Mon Trainer! In this game you will choose your Mon, and fight a computer opponent.")
    t.sleep(1.3)

    player_mon = player_pick_mon()
    return
    



start_game()