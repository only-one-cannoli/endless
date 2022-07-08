"""
state.py
Sets up a dataclass to represent the game state (everything but the player character).
"""

from dataclasses import dataclass
from typing import List


@dataclass
class State:
    """
    Game state.
    """

    location: Location
    location_draw_pile: List[Location]
    location_discard_pile: [List[Location]]
    monsters: List[Monster]
    monster_draw_pile: List[Monster]
    monster_discard_pile: List[Monster]
    item_draw_pile: List[Item]
    item_discard_pile: List[Item]
