# import portal

class Tile:

    def __init__(self, tileType):
        # portalExit defaults to nothing unless specified during instantiation.
        self.type = tileType
        self.key = False
        self.player = False

    # tileType should be one of the following:
    # "wall"
    # "lava"
    # "empty"
    # "exit"
    # "portalEntrance"
    # "portalExit"

    def isWall(self):
        return self.type == "wall"

    def isLava(self):
        return self.type == "lava"

    def isEmpty(self):
        return self.type == "empty"

    def isExit(self):
        return self.type == "exit"

    def isWormhole(self):
        return self.type == "wormhole"

    def isWormholeExit(self):
        return self.type == "wormholeExit"

    def hasKey(self):
        return self.key

    def hasPlayer(self):
        return self.player

    def isNotValidKeyTile(self):
        # This function returns true if a key can NOT go onto this tile
        if self.type == "wormhole" or self.type == "wormholeExit" or self.type == "wall" or self.hasKey() or self.hasPlayer():
            return True

        return False
