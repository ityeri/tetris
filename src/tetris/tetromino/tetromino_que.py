import random

from .tetromino_type import TetrominoType


class TetrominoQue:
    def __init__(self):
        self.que: list[TetrominoType] = list()
        self.deck: list[TetrominoType] = list()

    def extend(self):
        if not self.deck:
            self.deck = list(TetrominoType)
            random.shuffle(self.deck)

        self.que.append(self.deck.pop())

    def pop(self) -> TetrominoType:
        return self.que.pop(0)