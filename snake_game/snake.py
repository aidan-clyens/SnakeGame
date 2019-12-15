from .block import Block
from .constants import GRID_SIZE
from enum import Enum
import pygame


class Direction(Enum):
    Left = 1
    Right = 2
    Up = 3
    Down = 4


class Snake:
    def __init__(self):
        self._head_position = [200, 200]
        self._direction = Direction.Left

        self._blocks = []
        self._blocks.append(Block(self._head_position))

    def update(self):
        self.set_direction()

        if self._direction == Direction.Left:
            self._head_position[0] -= GRID_SIZE
        
        if self._direction == Direction.Right:
            self._head_position[0] += GRID_SIZE
        
        if self._direction == Direction.Up:
            self._head_position[1] -= GRID_SIZE
        
        if self._direction == Direction.Down:
            self._head_position[1] += GRID_SIZE
        
        prev_pos = self._head_position
        for i in range(len(self._blocks)):
            self._blocks[i].update(prev_pos)
            prev_pos = self._blocks[i]._position
        
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
