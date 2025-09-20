from .tetromino import Tetromino
from .tetromino.tetromino_type import TetrominoType


class FixedMap:
    def __init__(self, width: int = 10, height = 22):
        self.width: int = width
        self.height: int = height
        self.data: list[list[TetrominoType | None]] = [[None for x in range(width)] for y in range(height)]

    def get_at(self, x: int, y: int) -> TetrominoType | None:
        if x < 0 or y < 0: raise IndexError
        return self.data[y][x]

    def set_at(self, x: int, y: int, value: TetrominoType | None):
        if x < 0 or y < 0: raise IndexError
        self.data[y][x] = value

    def is_collisional(self, x: int, y: int) -> bool:
        try:
            return self.get_at(x, y) is not None
        except IndexError:
            if 0 <= x < self.width and y < self.height:
                return False
            else:
                return True

    def is_collision(self, tetromino: Tetromino) -> bool:
        for y in range(tetromino.top, tetromino.bottom):
            for x in range(tetromino.left, tetromino.right):
                if self.is_collisional(x, y) and tetromino.get_at(x, y):
                    return True

        return False