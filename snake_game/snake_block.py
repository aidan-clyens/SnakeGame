from .block import Block
from .direction import Direction
from .constants import GRID_SIZE


class SnakeBlock(Block):
    def __init__(self, pos, direction):
        Block.__init__(self, pos)

        self._direction = direction

    def update(self, direction=None):
        if direction is not None:
            self._direction = direction

        if self._direction == Direction.Left:
            self._position[0] -= GRID_SIZE

        if self._direction == Direction.Right:
            self._position[0] += GRID_SIZE

        if self._direction == Direction.Up:
            self._position[1] -= GRID_SIZE

        if self._direction == Direction.Down:
            self._position[1] += GRID_SIZE

        Block.update(self)
