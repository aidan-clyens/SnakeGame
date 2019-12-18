from .direction import Direction
from .constants import GRID_SIZE
import pygame


class Block:
    def __init__(self, pos, direction=None):
        self._direction = direction
        self._size = [GRID_SIZE, GRID_SIZE]

        self._image = pygame.Surface(self._size)
        self._image.fill(pygame.Color(255, 255, 255))
        self._rect = self._image.get_rect()
        self._rect.x = pos[0]
        self._rect.y = pos[1]

    def render(self, screen):
        screen.blit(self._image, [self._rect.x, self._rect.y])

    def collides(self, block):
        return self._rect.colliderect(block._rect)

    def set_position(self, position):
        self._rect.x = position[0]
        self._rect.y = position[1]

    def position(self):
        return [self._rect.x, self._rect.y]
