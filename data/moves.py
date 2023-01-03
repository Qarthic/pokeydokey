# from data import Pokemon
from pokemon import Pokemon as P
import random

# A dictionary of moves and their power

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

print(move_list.count(Move.element("Normal")))