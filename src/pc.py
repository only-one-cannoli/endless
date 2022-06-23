"""
pc.py
Sets up a dataclass to represent the player character.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class PC:
    """
    Player character.
    """

    name: str
    # pylint: disable-next=invalid-name
    hp: int = 3
    max_hp: int = 3
    abilities: Tuple[str, ...] = tuple()
    items: Tuple[str, ...] = tuple()
    max_items: int = 5

    def __post_init__(self):
        if len(self.items) > self.max_items:
            raise ValueError("Too many items!")
