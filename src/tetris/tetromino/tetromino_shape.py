class TetrominoShape:
    def __init__(self, size: int, shape: list[list[bool]]):
        self.center_diagonal_offset: float = size / 2
        self.size: int = size
        self.shape: list[list[bool]] = shape

    def get_at(self, x, y) -> bool:
        if x < 0 or y < 0:
            raise IndexError()
        return self.shape[y][x]

    def rotate(self, angle: int) -> 'TetrominoShape':
        return TetrominoShape(
            self.size,
            [
                [
                    self.get_at(*self._pos_rotate(-angle, new_x, new_y))
                    for new_x in range(self.size)
                ] for new_y in range(self.size)
            ]
        )

    def _pos_rotate(self, angle: int, x: int, y: int) -> tuple[int, int]:
        rx, ry = x - self.center_diagonal_offset, y - self.center_diagonal_offset
        if angle % 4 == 0:
            return x, y
        elif angle % 4 == 1:
            return round(-ry + self.center_diagonal_offset) - 1, x
        elif angle % 4 == 2:
            return round(-rx + self.center_diagonal_offset) - 1, round(-ry + self.center_diagonal_offset) - 1
        else:
            return y, round(-rx + self.center_diagonal_offset) - 1

    def print_shape(self, empty_chr: str = " ", solid_chr: str = "■"):
        for line in self.shape:
            print("".join([solid_chr * 2 if value else empty_chr * 2 for value in line]))