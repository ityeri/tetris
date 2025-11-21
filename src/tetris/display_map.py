from blessed import Terminal

from .fixed_map import FixedMap
from .tetromino import Tetromino
from .tetromino import TetrominoType

term = Terminal()


class DisplayMap:
    def __init__(self, *, width: int=10, height: int=22, fixed_map: FixedMap, tetromino: Tetromino):
        self.width: int = width
        self.height: int = height
        self.data: list[list[TetrominoType | None]] = \
            [[fixed_map.get_at(x, y) for x in range(fixed_map.width)] for y in range(fixed_map.height)]

        for y in range(tetromino.top, tetromino.bottom):
            for x in range(tetromino.left, tetromino.right):
                try:
                    if tetromino.get_at(x, y):
                        self.data[y][x] = tetromino.type
                except IndexError: pass

    def __getitem__(self, position: tuple[int, int]) -> TetrominoType | None:
        if position[0] < 0 or position[1] < 0: raise IndexError
        return self.data[position[1]][position[0]]