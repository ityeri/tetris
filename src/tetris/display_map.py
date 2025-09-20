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

    # 이 매서드는 원래 여깄으면 안됨
    def flush_map(self, x: int, y: int, pixel_width: int, pixel_height: int):
        for pixel_y in range(self.height):
            for pixel_x in range(self.width):
                pixel_type = self.data[pixel_y][pixel_x]
                if pixel_type is None:
                    char = " "
                else:
                    char = term.on_color_rgb(*pixel_type.color)(" ")

                for subpixel_y in range(pixel_height):
                    print(
                        term.move_xy(
                            x + pixel_x * pixel_width,
                            y + pixel_y * pixel_height + subpixel_y
                        ) + char * pixel_width + " |"
                    )