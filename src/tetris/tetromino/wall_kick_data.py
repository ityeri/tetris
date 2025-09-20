from dataclasses import dataclass


@dataclass
class WallKickData:
    zero_to_right: list[tuple[int, int]]
    right_to_zero: list[tuple[int, int]]

    right_to_second: list[tuple[int, int]]
    second_to_right: list[tuple[int, int]]

    second_to_left: list[tuple[int, int]]
    left_to_second: list[tuple[int, int]]

    left_to_zero: list[tuple[int, int]]
    zero_to_left: list[tuple[int, int]]

    def __getitem__(self, angle: tuple[int, int]) -> list[tuple[int, int]]:
        angle = (angle[0] % 4, angle[1] % 4)
        if angle == (0, 1):
            return self.zero_to_right
        elif angle == (1, 0):
            return self.right_to_zero
        elif angle == (1, 2):
            return self.right_to_second
        elif angle == (2, 1):
            return self.second_to_right
        elif angle == (2, 3):
            return self.second_to_left
        elif angle == (3, 2):
            return self.left_to_second
        elif angle == (3, 0):
            return self.left_to_zero
        elif angle == (0, 3):
            return self.zero_to_left
        else:
            print(angle)
            raise KeyError()


general_wall_kick_data = WallKickData(
    [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
    [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],

    [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)],
    [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],

    [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
    [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],

    [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)],
    [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
)

i_tetromino_wall_kick_data = WallKickData(
    [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],
    [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],

    [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)],
    [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],

    [(0, 0), (2, 0), (-1, 0), (2, -1), (-1, 2)],
    [(0, 0), (-2, 0), (1, 0), (-2, 1), (1, -2)],

    [(0, 0), (1, 0), (-2, 0), (1, 2), (-2, -1)],
    [(0, 0), (-1, 0), (2, 0), (-1, -2), (2, 1)]
)