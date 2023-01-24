# Todo:
# Generate mon and moveset from the db
import sys
sys.path.insert(0, '../..')
import random
import psycopg2
import csv
from app.classes.mon import Mon as mon
from app.classes.move import Move as move


con = psycopg2.connect(
    host = "localhost",
    database = "mon_db",
    user = "postgres",
    password = "king1926",
    port = 5432
)

cur = con.cursor()

cur.execute("select * from mon")

db_pull = cur.fetchall()

def assign_movesets():
    mon_dex =[]
    for row in db_pull:

        # assign mon stats

        name = row[1]
        level = row[2]
        hp = row[3]
        max_hp = row[3]
        attack = row[4]
        defense = row[5]
        speed = row[6]
        evasion = row[7]
        accuracy = row[8]
        element = row[9]

        # finish mon stats

        # set move objects and assign to mon moves

        con_2 = psycopg2.connect(
            host = "localhost",
            database = "mon_db",
            user = "postgres",
            password = "king1926",
            port = 5432
        )

        cur2 = con_2.cursor()

        cur2.execute(f"SELECT move_name, move_element, move_pp, move_power, move_accuracy, move_buff, move_stat, move_stage, move_target FROM moves m JOIN elements e ON e.element_id = m.move_element_id WHERE m.move_stage > 0 OR m.move_element = '{element}' ORDER BY m.move_id;")

        move_set = cur2.fetchall()

        moves = []
        for m in move_set:
            current_move = move(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8])
            moves.append(current_move)


        current_mon = mon(name=name, level=level, max_hp=max_hp, hp=hp, attack=attack, defense=defense, speed=speed, accuracy=accuracy, evasion=evasion, element=element, moves=moves) 

        mon_dex.append(current_mon)
        con_2.close()

    return mon_dex

mon_dex = assign_movesets()

con.close()
