from .block import Block
from .direction import Direction
from .constants import GRID_SIZE
import pygame


class Snake:
    def __init__(self):
        self._head_position = [200, 200]
        self._direction = Direction.Left

        self._blocks = []
        self._blocks.append(Block([200, 200], self._direction))

    def update(self):
        self.set_direction()

        pos = self._blocks[0].position()

        if self._direction == Direction.Left:
            pos[0] -= GRID_SIZE
            self._blocks.insert(0, Block(pos, self._direction))
        if self._direction == Direction.Right:
            pos[0] += GRID_SIZE
            self._blocks.insert(0, Block(pos, self._direction))
        if self._direction == Direction.Up:
            pos[1] -= GRID_SIZE
            self._blocks.insert(0, Block(pos, self._direction))
        if self._direction == Direction.Down:
            pos[1] += GRID_SIZE
            self._blocks.insert(0, Block(pos, self._direction))

        self._blocks.pop()

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

    def collides_food(self, food):
        for block in self._blocks:
            if block.collides(food):
                return True

        return False

    def lose(self):
        for i in range(1, len(self._blocks)):
            if self._blocks[0].collides(self._blocks[i]):
                return True

        return False

    def add_new_block(self):
        pos = self._blocks[-1].position()
        direction = self._blocks[-1]._direction

        if direction == Direction.Left:
            pos[0] += GRID_SIZE
        if direction == Direction.Right:
            pos[0] -= GRID_SIZE
        if direction == Direction.Up:
            pos[1] += GRID_SIZE
        if direction == Direction.Down:
            pos[1] -= GRID_SIZE

        self._blocks.append(Block(pos, direction))
