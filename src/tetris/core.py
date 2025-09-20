from .fixed_map import FixedMap
from .tetromino import Tetromino
from .tetromino import TetrominoQue


class Core:
    def __init__(self, que_length: int=5):
        self.fixed_map: FixedMap = FixedMap()

        self.tetromino: Tetromino | None = None
        self.tetromino_y_controlled: bool = False

        self.que: TetrominoQue = TetrominoQue()
        self.que_length: int = que_length

        self.landed: bool = False
        self.map_changed: bool = False

    def init(self):
        for i in range(4):
            self.que.extend()

    def left(self, distance: int) -> bool:
        for i in range(distance):
            self.tetromino.x -= 1

            if self.fixed_map.is_collision(self.tetromino):
                self.tetromino.x += 1
                if i == 0: return False
                break

        self.map_changed = True
        return True

    def right(self, distance: int) -> bool:
        for i in range(distance):
            self.tetromino.x += 1

            if self.fixed_map.is_collision(self.tetromino):
                self.tetromino.x -= 1
                if i == 0: return False
                break

        self.map_changed = True
        return True

    def down(self, distance: int | None) -> bool:
        if distance is not None:
            for i in range(distance):
                self.tetromino.y += 1

                if self.fixed_map.is_collision(self.tetromino):
                    self.tetromino.y -= 1
                    self.landed = True
                    if i == 0: return False
                    else: self.tetromino_y_controlled = True
                    break

        else:
            self.landed = True
            loops = 0
            while True:
                self.tetromino.y += 1

                if self.fixed_map.is_collision(self.tetromino):
                    self.tetromino.y -= 1
                    if loops == 0: return False
                    else: self.tetromino_y_controlled = True
                    break

        self.map_changed = True
        return True

    def rotate(self, direction: bool) -> bool:
        if direction: angle = 1
        else: angle = -1

        self.tetromino.angle += angle
        is_success = False

        for offset in self.tetromino.type.wall_kick_data[self.tetromino.angle - 1, self.tetromino.angle]:
            self.tetromino.x += offset[0]
            self.tetromino.y += offset[1]

            if self.fixed_map.is_collision(self.tetromino):
                self.tetromino.x -= offset[0]
                self.tetromino.y -= offset[1]
            else:
                is_success = True
                break

        if is_success: self.map_changed = True
        return is_success


    def tick(self):
        if not self.tetromino_y_controlled:
            self.tetromino.y += 1

        if self.fixed_map.is_collision(self.tetromino):
            self.tetromino.y -= 1

            for y in range(self.tetromino.top, self.tetromino.bottom):
                for x in range(self.tetromino.left, self.tetromino.right):
                    try:
                        if self.tetromino.get_at(x, y):
                            self.fixed_map.set_at(x, y, self.tetromino.type)
                    except IndexError:
                        pass

            self.remove_filled_line()

            self.que.extend()
            t_type = self.que.pop()
            self.tetromino = Tetromino(t_type.spawn_x, t_type.spawn_y, t_type)

        self.map_changed = True

    def remove_filled_line(self):
        for y in range(self.fixed_map.height):
            is_filled = True
            for x in range(self.fixed_map.width):
                if not self.fixed_map.is_collisional(x, y):
                    is_filled = False

            if is_filled:
                for modifying_y in range(y - 1, -1, -1):
                    for modifying_x in range(self.fixed_map.width):
                        self.fixed_map.set_at(
                            modifying_x, modifying_y + 1,
                            self.fixed_map.get_at(modifying_x, modifying_y)
                        )