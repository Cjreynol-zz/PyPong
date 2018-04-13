from pygame import Rect


class VelRect(Rect):
    """
    A pygame Rect with additional attributes for keeping track of velocity.
    """

    def __init__(self, start_pos, dimensions):
        super().__init__(*start_pos, *dimensions)
        self.start_pos = start_pos
        self.dx = 0
        self.dy = 0

    def reset(self):
        self.x, self.y = self.start_pos
        self.dx, self.dy = 0, 0

    def move_vel(self):
        self.x += self.dx
        self.y += self.dy

    def collision_with(self, other):
        return self.colliderect(other)

    def reflect_x(self):
        self.dx *= -1

    def reflect_y(self):
        self.dy *= -1
