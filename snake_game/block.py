from .constants import GRID_SIZE
import pygame

class Block:
    def __init__(self, pos):
        self._position = pos
        self._size = [GRID_SIZE, GRID_SIZE]

        self._image = pygame.Surface(self._size)
        self._image.fill(pygame.Color(255, 255, 255))

    def update(self, pos=None):
        if pos is not None:
            self._position = pos

    def render(self, screen):
        screen.blit(self._image, self._position)