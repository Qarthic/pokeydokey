# A dictionary of moves and their power

class Move:
  def __init__(self, pp, name, type, target):
    self.pp = pp
    self.name = name
    self.type = type
    self.target = target

class Damaging(Move):
  def __init__(self, pp, name, type, target, power, accuracy):
    super().__init__(pp, name, type, target)
    self.power = power
    self.accuracy = accuracy
  
  def attack(self):
    self.target.hp - self.power

class Buff_Debuff(Move):
  def __init__(self, pp, name, type, target, stat, stage):
    super().__init__(pp, name, type, target)
    self.stage = stage
    self.stat = stat
  
  def attack(self):
    self.target.stat -= self.stage

tackle = Damaging(35, "Tackle", "Normal", "Foe", 40, 100)
growl = Buff_Debuff(40, "Growl", "Normal", "Foe", "Atk", 1)