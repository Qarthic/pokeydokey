import sys 
sys.path.append("mon_battle/app/classes")
import random
import csv


# Todo:
# Create Move class, and Damage/Buff subclasses (Ref old_doke/dex_data/mon_rules.py lines 68, 84, 94)
# Also, this should be a table. 

# 'name', 'element', 'pp', 'stage','element','power','accuracy','buff','stat','stage','target'
# 'Tackle', 'Normal', 25, 0.4, 1.0, False, None, 0, 'False'

class Move:
    def __init__(self, name: str, element:str, pp: int, power:float, accuracy:float, buff:bool, stat:str, stage:int, target:str):
        self.name = name
        self.element = element
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.buff = buff
        self.stat = stat
        self.stage = stage
        self.target = target
        self.stats = {
            'name': name,
            'element': element, 
            'pp': pp, 
            'accuracy': power, 
            'buff': accuracy,
            'stat': stat,
            'stage': stage,
            'target': target
        }

# class Attack(Move):
#     def __init__(self, pp: int, name: str, element: str, target: str, power: float, accuracy: float):
#         super().__init__(pp, name, element, target)
#         self.power = power
#         self.accuracy = accuracy
    
# class Buff_Debuff(Move):
#     def __init__(self, pp: int, name: str, buff: bool, target: bool, stage: int, stat: str):
#         super().__init__(pp, name, target) # type: ignore
#         self.stage = stage
#         self.buff = buff
#         self.stat = stat


# moves = [
#     ['name','element','pp', 'power','accuracy','buff','stat','stage','target'],
#     ['Tackle', 'Normal', 25, 0.4, 1, False, None, 0, False],
#     ['Water Gun', 'Water', 25, 0.4, 1, False, None, 0, False],
#     ['Bullet Punch', 'Steel', 30, 0.3, 1, False, None, 0, False],
#     ['Rock Tomb', 'Rock', 15, 0.6, 0.95, False, None, 0, False],
#     ['Confusion', 'Psychic', 25, 0.5, 1, False, None, 0, False],
#     ['Sludge', 'Poison', 20, 0.65, 1, False, None, 0, False],
#     ['Tackle', 'Normal', 35, 0.4, 1, False, None, 0, False],
#     ['Powder Snow', 'Ice', 25, 0.4, 1, False, None, 0, False],
#     ['Bulldoze', 'Ground', 20, 0.6, 1, False, None, 0, False],
#     ['Razor Leaf', 'Grass', 25, 0.55, 0.95, False, None, 0, False],
#     ['Shadow Sneak', 'Ghost', 30, 0.4, 1, False, None, 0, False],
#     ['Gust', 'Flying', 35, 0.4, 1, False, None, 0, False],
#     ['Ember', 'Fire', 25, 0.4, 1, False, None, 0, False],
#     ['Rock Smash', 'Fighting', 15, 0.4, 1, False, None, 0, False],
#     ['Fairy Wind', 'Fairy', 30, 0.4, 1, False, None, 0, False],
#     ['Thunder Shock', 'Electric', 30, 0.4, 1, False, None, 0, False],
#     ['Twister', 'Dragon', 20, 0.4, 1, False, None, 0, False],
#     ['Bite', 'Dark', 25, 0.6, 1, False, None, 0, False],
#     ['Struggle Bug', 'Bug', 20, 0.5, 1, False, None, 0, False],
#     ['Leer', None, 30, None, None, False, 'Defense', 1, False],
#     ['Sand Attack', None, 15, None, None, False, 'Accuracy', 1, False],
#     ['Growl', None, 40, None, None, False, 'Attack', 1, False]
#  ]

# elements = mon.elements 



# def create_move_csv():
#     with open('moves.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(moves[0])

#         for i in moves[1::]:
#             writer.writerow(i)

#     return file