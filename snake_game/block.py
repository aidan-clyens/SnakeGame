from .constants import GRID_SIZE
import pygame


class Block:
    def __init__(self, pos):
        self._position = pos
        self._size = [GRID_SIZE, GRID_SIZE]

        self._image = pygame.Surface(self._size)
        self._image.fill(pygame.Color(255, 255, 255))
        self._rect = self._image.get_rect()

    def update(self, pos=None):
        if pos is not None:
            self._position = pos

        self._rect.x = self._position[0]
        self._rect.y = self._position[1]

    def render(self, screen):
        screen.blit(self._image, [self._rect.x, self._rect.y])

    def collides(self, block):
        return self._rect.colliderect(block._rect)
