from .block import Block
from enum import Enum
import pygame


class Direction(Enum):
    Left = 1
    Right = 2
    Up = 3
    Down = 4


class Snake:
    def __init__(self):
        self._blocks = []

        self._direction = Direction.Left

    def update(self):
        self.set_direction()

        for block in self._blocks:
            block.update()

    def render(self, screen):
        for block in self._blocks:
            block.render(screen)

    def set_direction(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a]:
            self._direction = Direction.Left

        if pressed[pygame.K_d]:
            self._direction = Direction.Right

        if pressed[pygame.K_w]:
            self._direction = Direction.Up

        if pressed[pygame.K_s]:
            self._direction = Direction.Down
