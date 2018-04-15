from pygame import Rect

from collision_dir import CollisionDir


class VelRect(Rect):
    """
    A pygame Rect with additional attributes for keeping track of velocity.
    """

    def __init__(self, start_pos, dimensions):
        super().__init__(*start_pos, *dimensions)
        self.start_pos = start_pos
        self.dimensions = dimensions
        self.dx = 0
        self.dy = 0
        self.last_x = 0
        self.last_y = 0

    def reset(self):
        self.last_x, self.last_y = self.x, self.y
        self.x, self.y = self.start_pos
        self.dx, self.dy = 0, 0

    def move_vel(self):
        self.last_x, self.last_y = self.x, self.y
        self.x += self.dx
        self.y += self.dy

    def collision_with(self, other):
        direction = None
        if self.colliderect(other):
            if self.last_y + self.dimensions[1] <= other.last_y:
                direction = CollisionDir.NORTH
            elif self.last_x >= other.last_x + other.dimensions[0]:
                direction = CollisionDir.EAST
            elif self.last_y >= other.last_y + other.dimensions[1]:
                direction = CollisionDir.SOUTH
            elif self.last_x + self.dimensions[0] <= other.last_x:
                direction = CollisionDir.WEST
            else:
                raise RuntimeError("Could not determine collision direction.")
        return direction

    def reflect_x(self):
        self.dx *= -1

    def reflect_y(self):
        self.dy *= -1
