from .snake import Snake
from .block import Block
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, ROWS, COLS, GRID_SIZE
import pygame
import random


class Game:
    def __init__(self):
        pygame.init()

        self._screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self._clock = pygame.time.Clock()

        self._food = Block([
            random.randint(0, COLS) * GRID_SIZE,
            random.randint(0, ROWS) * GRID_SIZE
        ])
        self._snake = Snake()

        self._running = True

    def run(self):
        while self._running:
            self.poll_events()

            self.update()
            self.render()

            self._clock.tick(10)

    def quit(self):
        pygame.quit()

    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def update(self):
        self._snake.update()

        if self._snake.lose():
            self._running = False

        if self._snake.collides_food(self._food):
            self._food.set_position([
                random.randint(0, COLS) * GRID_SIZE,
                random.randint(0, ROWS) * GRID_SIZE
            ])

            self._snake.add_new_block()

    def render(self):
        self._screen.fill(pygame.Color(0, 0, 0))

        self._food.render(self._screen)
        self._snake.render(self._screen)

        pygame.display.flip()
