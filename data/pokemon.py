

class Pokemon:
    def __init__(self, name: str, element: str, level: int, max_hit_points: int, attack: int, defense: int, speed: int):
        self.name = name
        self.element = element
        self.level = level
        self.max_hit_points = max_hit_points
        self.attack = attack
        self.defense = defense
        self.speed = speed