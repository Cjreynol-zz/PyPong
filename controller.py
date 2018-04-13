from pygame import event, init, quit
from pygame.locals import QUIT, KEYDOWN, KEYUP
from pygame.locals import K_DOWN, K_ESCAPE, K_s, K_SPACE, K_UP, K_w

from pygame.time import Clock

from pypong import PyPong
from screen import Screen


class Controller:
    """
    The manager for both the game state and the screen state, as well as the 
    event handler.
    """

    FPS = 30

    def __init__(self):
        init()
        self.view = Screen()
        self.game = PyPong(*self.view.screen_dimensions())

        self.done = False
        self.clock = Clock()

    def run_gameloop(self):
        while not self.done:
            self.clock.tick(self.FPS)
            self._handle_events(event.get())
            self.game.progress_game()
            self.view.render_screen(self.game)
        quit()

    def _handle_events(self, event_list):
        for event in event_list:
            if (event.type == QUIT or 
                        (event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.done = True

            if event.type == KEYDOWN and event.key == K_SPACE:
                self.game.start_ball()

            if event.type == KEYDOWN and event.key == K_w:
                self.game.p1_up()
            if event.type == KEYDOWN and event.key == K_s:
                self.game.p1_down()
            if event.type == KEYUP and (event.key == K_w or event.key == K_s):
                self.game.p1_stop()

            if event.type == KEYDOWN and event.key == K_UP:
                self.game.p2_up()
            if event.type == KEYDOWN and event.key == K_DOWN:
                self.game.p2_down()
            if event.type == KEYUP and (event.key == K_UP or event.key == K_DOWN):
                self.game.p2_stop()
