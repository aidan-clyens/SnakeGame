from .constants import GRID_SIZE
import pygame


class Block:
    def __init__(self, pos):
        self._size = [GRID_SIZE, GRID_SIZE]

        self._image = pygame.Surface(self._size)
        self._image.fill(pygame.Color(255, 255, 255))
        self._rect = self._image.get_rect()
        self._rect.x = pos[0]
        self._rect.y = pos[1]

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self._image, [self._rect.x, self._rect.y])
