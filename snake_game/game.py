from .snake import Snake
from .block import Block
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class Game:
    def __init__(self):
        pygame.init()

        self._screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self._clock = pygame.time.Clock()

        self._food = Block([100, 100])
        self._snake = Snake()

        self._running = True

    def run(self):
        while self._running:
            self.poll_events()

            self.update()
            self.render()

            self._clock.tick(60)

    def quit(self):
        pygame.quit()
    
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
    
    def update(self):
        self._food.update()
        self._snake.update()

    def render(self):
        self._food.render(self._screen)
        self._snake.render(self._screen)
        pygame.display.flip()