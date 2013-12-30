# Chad Reynolds
# 12/28/13
# manager for the game

from pygame import event, time, key
from pygame.locals import *
from moverect import MoveRect
from gamescreen import GameScreen
from constants import *

class GameManager(object):
	"""A manager to run the game."""
	def __init__(self):
		"""Creates all of the games pieces and objects, then starts gameloop."""
		self.ball = MoveRect(SCREEN_X / 2, SCREEN_Y / 2, BALL_WIDTH, BALL_HEIGHT, BALL_DX, BALL_DY, BALL_COLOR)
		self.ballmove = False

		self.player1 = MoveRect(SCREEN_X / 8 * 7, SCREEN_Y / 2, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_DX, PADDLE_DY, PADDLE_COLOR)
		self.p1move = False
		self.player2 = MoveRect(SCREEN_X / 8 * 1, SCREEN_Y / 2, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_DX, PADDLE_DY, PADDLE_COLOR)
		self.p2move = False
		self.screen = GameScreen([self.ball, self.player1, self.player2])

		self.clock = time.Clock()

		self.run()

	def run(self):
		"""Runs the actual game."""
		done = False
		while not done:
			self.clock.tick(30)

			for x in event.get():
				if x.type == QUIT or (x.type == KEYDOWN and x.key == K_ESCAPE):
					done = True

				# p1 controls
				if x.type == KEYDOWN and x.key == K_UP:
					self.player1.change_speed(0, -3)
					self.p1move = True

				if x.type == KEYUP and x.key == K_UP:
					self.p1move = False

				if x.type == KEYDOWN and x.key == K_DOWN:
					self.player1.change_speed(0, 3)
					self.p1move = True

				if x.type == KEYUP and x.key == K_DOWN:
					self.p1move = False
	
				# p2 controls
				if x.type == KEYDOWN and x.key == K_w:					
					self.player2.change_speed(0, -3)
					self.p2move = True

				if x.type == KEYUP and x.key == K_w:					
					self.p2move = False

				if x.type == KEYDOWN and x.key == K_s:
					self.player2.change_speed(0, 3)
					self.p2move = True

				if x.type == KEYUP and x.key == K_s:
					self.p2move = False

				# ball controls
				if x.type == KEYDOWN and x.key == K_v:
					self.ballmove = True

				if x.type == KEYDOWN and x.key == K_b:
					self.ballmove = False

			if self.p1move:
				self.player1.move_rect()

			if self.p2move:
				self.player2.move_rect()

			if self.ballmove:
				self.ball.detect_collision([self.player1, self.player2])
				self.ball.move_rect()

			self.screen.draw_all()
