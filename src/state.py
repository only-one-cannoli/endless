"""
state.py
Sets up dataclasses to represent the player character and the world (everything
else).
"""

from dataclasses import dataclass
from typing import List

from .cards import (
    Creature,
    Item,
    Location,
)


@dataclass
class PC:
    """
    Player character.
    """

    name: str
    hp: int = 3
    max_hp: int = 3
    items: List[Item] = []
    max_items: int = 5


@dataclass
class World:
    """
    All non-player-character-related game-state variables.
    """

    location: Location
    location_draw_pile: List[Location]
    location_discard_pile: List[Location]
    monsters: List[Creature]
    monster_draw_pile: List[Creature]
    monster_discard_pile: List[Creature]
    item_draw_pile: List[Item]
    item_discard_pile: List[Item]
