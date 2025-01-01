player_pos = {
    "x": 0,
    "y": 0,
    "z": 0,
    "q": 0,
    "t": 1 #zero to represent something that is not an event
}

class Place:
    def __init__(self, x=0, y=0, z=0, q=0, t=0, item=None, creature=None, message=None, name=None, region=None):
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
        self.region      = region

places = []
places.append(Place(x=10, y=10, z=10, q=10, t=10, message="2"))

##################
# main game loop #
##################
game_running = True
while(game_running):
    print("your position:")
    #do I need to use keys?
    print(player_pos[0], player_pos[1], player_pos[2], player_pos[3])
    print("current time is:")
    print(player_pos[4])
    next_move = input("next move:")
