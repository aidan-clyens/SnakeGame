from .block import Block


class Snake:
    def __init__(self):
        self._blocks = []

    def update(self):
        for block in self._blocks:
            block.update()

    def render(self, screen):
        for block in self._blocks:
            block.render(screen)
