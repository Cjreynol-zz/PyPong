from enum import Enum


class CollisionDir(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    
    def __str__(self):
        return self.name
