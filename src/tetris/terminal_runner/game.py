import time
from threading import Thread

from blessed import Terminal

from src.tetris import Core
from src.tetris.display_map import DisplayMap
from .event import Event, KeyEvent
from .key_map import Keymap, ControlType
from .key_type import KeyType


class Clock:
    def __init__(self):
        self.last_update_time: float = time.time()

    def tick(self) -> float:
        current_time = time.time()
        dt = current_time - self.last_update_time
        self.last_update_time = current_time
        return dt


class Game:
    def __init__(self):
        self.event_list: list[Event] = list()
        self.key_dispatch_thread: Thread | None = None
        self.keymap: Keymap = Keymap()
        self.tick_interval: float = 0.5

        self.core = Core()

    def run(self):
        self.key_dispatch_thread = Thread(target=self.key_dispatcher, daemon=True)
        self.key_dispatch_thread.start()

        clk = Clock()
        tick_timer = 0

        while True:
            time.sleep(1 / 60)
            dt = clk.tick()

            for event in self.event_list:
                if isinstance(event, KeyEvent):
                    self.keymap.event(event)


            if self.keymap[ControlType.LEFT]:
                self.core.left(1)

            if self.keymap[ControlType.RIGHT]:
                self.core.right(1)

            if self.keymap[ControlType.FAST_DROP]:
                self.core.down(1)

            if self.keymap[ControlType.HARD_DROP]:
                self.core.down(None)

            if self.keymap[ControlType.R_ROTATE]:
                self.core.rotate(True)


            if self.core.landed:
                tick_timer = 0

            if tick_timer <= 0:
                self.core.tick()
                tick_timer = self.tick_interval
            tick_timer -= dt

            if self.core.map_changed:
                display_map = DisplayMap(
                    fixed_map=self.core.fixed_map,
                    tetromino=self.core.tetromino
                )
                display_map.flush_map(4, 2, 4, 2)
                self.core.map_changed = False


            self.event_list.clear()
            self.keymap.event_clear()

    def key_dispatcher(self):
        term = Terminal()
        with term.cbreak():
            while True:
                key = term.inkey()
                event: Event | None = None

                if not key.is_sequence:
                    key_chr = str(key)
                    if key_chr == " ": event = KeyEvent(KeyType.SPACE)
                    elif key_chr == "a": event = KeyEvent(KeyType.A)
                    elif key_chr == "b": event = KeyEvent(KeyType.B)
                    elif key_chr == "c": event = KeyEvent(KeyType.C)
                    elif key_chr == "d": event = KeyEvent(KeyType.D)
                    elif key_chr == "e": event = KeyEvent(KeyType.E)
                    elif key_chr == "f": event = KeyEvent(KeyType.F)
                    elif key_chr == "g": event = KeyEvent(KeyType.G)
                    elif key_chr == "h": event = KeyEvent(KeyType.H)
                    elif key_chr == "i": event = KeyEvent(KeyType.I)
                    elif key_chr == "j": event = KeyEvent(KeyType.J)
                    elif key_chr == "k": event = KeyEvent(KeyType.K)
                    elif key_chr == "l": event = KeyEvent(KeyType.L)
                    elif key_chr == "m": event = KeyEvent(KeyType.M)
                    elif key_chr == "n": event = KeyEvent(KeyType.N)
                    elif key_chr == "o": event = KeyEvent(KeyType.O)
                    elif key_chr == "p": event = KeyEvent(KeyType.P)
                    elif key_chr == "q": event = KeyEvent(KeyType.Q)
                    elif key_chr == "r": event = KeyEvent(KeyType.R)
                    elif key_chr == "s": event = KeyEvent(KeyType.S)
                    elif key_chr == "t": event = KeyEvent(KeyType.T)
                    elif key_chr == "u": event = KeyEvent(KeyType.U)
                    elif key_chr == "v": event = KeyEvent(KeyType.V)
                    elif key_chr == "w": event = KeyEvent(KeyType.W)
                    elif key_chr == "x": event = KeyEvent(KeyType.X)
                    elif key_chr == "y": event = KeyEvent(KeyType.Y)
                    elif key_chr == "z": event = KeyEvent(KeyType.Z)

                elif key.name == "KEY_UP": event = KeyEvent(KeyType.UP)
                elif key.name == "KEY_DOWN": event = KeyEvent(KeyType.DOWN)
                elif key.name == "KEY_LEFT": event = KeyEvent(KeyType.LEFT)
                elif key.name == "KEY_RIGHT": event = KeyEvent(KeyType.RIGHT)

                self.event_list.append(event)