from abc import ABC
from dataclasses import dataclass

from .key_type import KeyType


@dataclass
class Event(ABC): ...

@dataclass
class KeyEvent(Event):
    key: KeyType