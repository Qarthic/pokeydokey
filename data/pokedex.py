class Pokemon:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

class Bulbasaur(Pokemon): # Subclass 1 of Pokemon
  def __init__(self, name, id):
    super().__init__(name, id)
    self.type = "Grass"
    self.moves = {
      "Tackle": dict(),
      "Growl": dict(),
      "Vine Whip": dict(), 
      "Growth": dict()
    }
    self.level = 5
    self.hp = 39
    self.attack = 52
    self.defense = 43
    self.speed = 65

class Charmander(Pokemon): # Subclass 1 of Pokemon
  def __init__(self, name, id):
    super().__init__(name, id)
    self.type = []
    self.moves = dict()
    self.level = 5
    self.hp = 39
    self.attack = 52
    self.defense = 43
    self.speed = 65

class Charmander(Pokemon): # Subclass 1 of Pokemon
  def __init__(self, name, id):
    super().__init__(name, id)
    self.type = []
    self.moves = dict()
    self.level = 5
    self.hp = 39
    self.attack = 52
    self.defense = 43
    self.speed = 65

charmander = Pokemon("Charmander", 1)
