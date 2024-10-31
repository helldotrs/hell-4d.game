player_pos = {
    "x": 0,
    "y": 0,
    "z": 0,
    "q": 0,
    "t": 0
}

class Pos:
    def __init__(self, x=0, y=0, z=0, q=0, t=0, item=None, creature=None, message=None, name=None):
        self.x = x
        self.y = y
        self.z = z
        self.q = q
        self.t = t
        self.item = item
        self.creature = creature
        self.message = message
        self.name = name
