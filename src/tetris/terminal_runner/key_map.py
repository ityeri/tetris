from enum import Enum, auto

from .event import KeyEvent
from .key_type import KeyType


class ControlType(Enum):
    R_ROTATE = auto()
    FAST_DROP = auto()
    HARD_DROP = auto()
    LEFT = auto()
    RIGHT = auto()


class Keymap:
    def __init__(self):
        self.control_keymap: dict[ControlType, set[KeyType]] = {
            ControlType.R_ROTATE: {
                KeyType.UP,
                KeyType.W,
                KeyType.K,
            },
            ControlType.FAST_DROP: {
                KeyType.DOWN,
                KeyType.S,
                KeyType.J,
            },
            ControlType.HARD_DROP: {
                KeyType.SPACE
            },
            ControlType.LEFT: {
                KeyType.LEFT,
                KeyType.A,
                KeyType.H
            },
            ControlType.RIGHT: {
                KeyType.RIGHT,
                KeyType.D,
                KeyType.L
            },
        }

        self.control_event: dict[ControlType, bool] = {
            ctrl_type: False for ctrl_type in ControlType
        }

    def event(self, event: KeyEvent):
        for ctrl_type, key_binds in self.control_keymap.items():
            if event.key in key_binds:
                self.control_event[ctrl_type] = True

    def event_clear(self):
        self.control_event: dict[ControlType, bool] = {
            ctrl_type: False for ctrl_type in ControlType
        }

    def __getitem__(self, ctrl_type: ControlType):
        return self.control_event[ctrl_type]