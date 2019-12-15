import pygame

class Block:
    def __init__(self, pos, size):
        self._position = pos
        self._size = size

        self._image = pygame.Surface(size)
        self._image.fill(pygame.Color(255, 255, 255))

    def update(self, pos=None):
        if pos is not None:
            self._position = pos

    def render(self, screen):
        screen.blit(self._image, self._position)