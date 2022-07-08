"""
pc.py
Sets up a dataclass to represent the player character.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class PC:
    """
    Player character.
    """

    name: str
    hp: int = 3
    max_hp: int = 3
    abilities: [Ability] = []
    items: List[Item] = []
    max_items: int = 5
