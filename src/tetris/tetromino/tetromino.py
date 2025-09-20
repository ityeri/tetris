from .tetromino_shape import TetrominoShape
from .tetromino_type import TetrominoType


class Tetromino:
    def __init__(self, x: float, y: float, type: TetrominoType):
        self.x: float = x
        self.y: float = y
        self.type: TetrominoType = type
        self.angle: int = 0

    @property
    def current_shape(self) -> TetrominoShape:
        return self.type.default_shape.rotate(self.angle)

    @property
    def left(self) -> int:
        return round(self.x - self.current_shape.center_diagonal_offset)

    @property
    def top(self) -> int:
        return round(self.y - self.current_shape.center_diagonal_offset)

    @property
    def right(self) -> int:
        return self.left + self.current_shape.size

    @property
    def bottom(self) -> int:
        return self.top + self.current_shape.size

    def get_at(self, x: int, y: int) -> bool:
        return self.current_shape.get_at(
            round(x - self.x + self.type.default_shape.center_diagonal_offset),
            round(y - self.y + self.type.default_shape.center_diagonal_offset)
        )