# Chad Reynolds
# 12/28/13
# create a surface display for the game

from pygame import Surface, display, draw
from constants import *

class GameScreen(object):
	"""A display for the game."""

	def __init__(self, list):
		"""Creates display."""
		self.screen = display.set_mode((SCREEN_X, SCREEN_Y))
		display.set_caption("PyPong v2")
		self.pieces = list

		self.draw_all()

	def draw_background(self):
		"""Draws the background of the game."""
        	self.screen.fill(SCREEN_COLOR)
        	draw.line(self.screen, SCREEN_OBJECT_COLOR, (SCREEN_X / 2, 0), (SCREEN_X / 2, SCREEN_Y))

	def draw_all(self):
		"""Draws the background and all of the game pieces."""
		self.draw_background()
		for piece in self.pieces:
			piece.draw_on_screen(self.screen)
		display.flip()
