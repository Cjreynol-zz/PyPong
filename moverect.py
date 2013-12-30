# Chad Reynolds
# 12/28/13
# Create a moveable rectangle for pong ball and paddle

from pygame import Rect, draw
from constants import *

class MoveRect(Rect):
	"""A moveable rectangle for creating ball and paddles."""

	def __init__(self, left, top, width, height, dx, dy, color):
		"""Creates the Rect() and stores the x and y velocities."""

		super(MoveRect, self).__init__(left, top, width, height)

		self.dx = dx
		self.dy = dy

		self.color = color

	def move_rect(self):
		"""Moves Rect by it's own speed."""
		if (self.left + self.dx < 0) or (self.left + self.width + self.dx > SCREEN_X):
			self.reflect("x")
		if (self.top + self.dy < 0) or (self.top + self.height + self.dy > SCREEN_Y):
			self.reflect("y")

		self.move_ip(self.dx, self.dy)

	def change_speed(self, new_dx, new_dy):
		"""Alters the speed of the Rect."""
		self.dx = new_dx
		self.dy = new_dy

	def draw_on_screen(self, surface):
		"""Draws the MoveRect on the given surface."""
		draw.rect(surface, self.color, self)

	def reflect(self, axis):
		"""Reflects the MoveRect, for use with collisions."""
		if axis == "x":
			self.dx *= -1
		elif axis == "y":
			self.dy *= -1
		else:
			raise ValueError("Axis must be either 'x' or 'y' for reflection.")

	def detect_collision(self, list):
		"""Detects if there are any collisions with a list of rects."""
		index = self.collidelist(list)
		if index != -1:
			self.handle_collision(list[index])

	def handle_collision(self, rect):
		"""Determines which axis of movement the collision is on and reflects self."""
		if self.detect_left(rect) or self.detect_right(rect): 
			self.reflect("x")

		elif self.detect_top(rect) or self.detect_bot(rect):
			self.reflect("y")

	def detect_left(self, rect):
		"""Detects if a collision has happened on left side of self."""
		if (self.left < rect.left + rect.width) and (self.left > rect.left):
			if ((self.top < rect.top + rect.height) and (self.top > rect.top)) or ((self.top + self.height > rect.top) and (self.top + self.height < rect.top + rect.height)):
				return True
		return False

	def detect_right(self, rect):
		"""Detects if a collision has happened on the right side of self."""
		if (self.left + self.width < rect.left + rect.width) and (self.left + self.width > rect.left):
			if ((self.top < rect.top + rect.height) and (self.top > rect.top)) or ((self.top + self.height > rect.top) and (self.top + self.height < rect.top + rect.height)):
				return True
		return False

	def detect_top(self, rect):
		"""Detects if a collision has happened on the top side of self."""
		if (self.top < rect.top + rect.height) and (self.top > rect.top):
			if ((self.left < rect.left + rect.width) and (self.left > rect.left)) or ((self.left + self.width < rect.left + rect.width) and (self.left + self.width > rect.left)):
				return True
		return False

	def detect_bot(self, rect):
		"""Detects if a collision has happend on the bottom side of self."""
		if (self.top + self.height < rect.top + rect.height) and (self.top + self.height > rect.top):
			if ((self.left < rect.left + rect.width) and (self.left > rect.left)) or ((self.left + self.width < rect.left + rect.width) and (self.left + self.width > rect.left)):
				return True
		return False
