player_pos = {
    "x": 0,
    "y": 0,
    "z": 0,
    "q": 0,
    "t": 1 #zero to represent something that is not an event
}

class Place:
    def __init__(self, x=0, y=0, z=0, q=0, t=0, item=None, creature=None, message=None, name=None):
        #pos
        self.x    = x
        self.y    = y
        self.z    = z
        self.q    = q
        self.t    = t

        #about
        self.item        = item
        self.creature    = creature
        self.message     = message
        self.name        = name

places = []
places.append(Place(x=10, y=10, z=10, q=10, t=10, message="2"))
