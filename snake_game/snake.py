from .snake_block import SnakeBlock
from .direction import Direction
import pygame


class Snake:
    def __init__(self):
        self._head_position = [200, 200]
        self._direction = Direction.Left

        self._blocks = []
        self._blocks.append(SnakeBlock(self._head_position, self._direction))

    def update(self):
        self.set_direction()

        prev_dir = self._direction
        for i in range(len(self._blocks)):
            self._blocks[i].update(prev_dir)
            prev_dir = self._blocks[i]._direction

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
        if self._blocks[0].collides(food):
            return True

        return False

    def add_new_block(self):
        pos = self._blocks[-1]._position
        direction = self._blocks[-1]._direction
        print(f"Created block: {pos}")
        print(f"Num blocks: {len(self._blocks)}")
        self._blocks.append(SnakeBlock(pos, direction))
