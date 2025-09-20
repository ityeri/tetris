from enum import Enum

from .tetromino_shape import TetrominoShape
from .wall_kick_data import WallKickData, i_tetromino_wall_kick_data, general_wall_kick_data


class TetrominoType(Enum):
    def __init__(
            self,
            default_shape: TetrominoShape,
            spawn_x: float,
            spawn_y: float,
            wall_kick_data: WallKickData,
            color: tuple[int, int, int]
    ):
        self.default_shape: TetrominoShape = default_shape
        self.spawn_x: float = spawn_x
        self.spawn_y: float = spawn_y
        self.wall_kick_data: WallKickData = wall_kick_data
        self.color: tuple[int, int, int] = color

    I = (
        TetrominoShape(
            4,
            [
                [False, False, False, False],
                [True, True, True, True],
                [False, False, False, False],
                [False, False, False, False]
            ],
        ), 5, 2, i_tetromino_wall_kick_data, (0, 255, 255)
    )
    J = (
        TetrominoShape(
            3,
            [
                [True, False, False],
                [True, True, True],
                [False, False, False],
            ],
        ), 4.5, 1.5, general_wall_kick_data, (0, 0, 255)
    )
    L = (
        TetrominoShape(
            3,
            [
                [False, False, True],
                [True, True, True],
                [False, False, False],
            ],
        ), 4.5, 1.5, general_wall_kick_data, (255, 127, 0)
    )
    O = (
        TetrominoShape(
            2,
            [
                [True, True],
                [True, True]
            ]
        ), 5, 1, general_wall_kick_data, (255, 255, 0)
    )
    S = (
        TetrominoShape(
            3,
            [
                [False, True, True],
                [True, True, False],
                [False, False, False]
            ]
        ), 4.5, 1.5, general_wall_kick_data, (0, 255, 0)
    )
    Z = (
        TetrominoShape(
            3,
            [
                [True, True, False],
                [False, True, True],
                [False, False, False]
            ]
        ), 4.5, 1.5, general_wall_kick_data, (255, 0, 0)
    )
    T = (
        TetrominoShape(
            3,
            [
                [False, True, False],
                [True, True, True],
                [False, False, False]
            ]
        ), 4.5, 1.5, general_wall_kick_data, (255, 0, 255)
    )