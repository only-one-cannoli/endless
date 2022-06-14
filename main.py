import cmd
from dataclasses import dataclass, replace
import json

from typing import List, Optional


name_ok = False
while name_ok is False:
    name: str = input("What is your name? ")
    name_ok = name.isalpha() and len(name) <= 20
print("That's a good name!")

@dataclass(frozen=True)
class PC:
    """
    Player character
    """
    name: str
    health: int = 3
    max_health: int = 3
    abilities: Optional[List[str]] = []
    items: Optional[List[str]] = []
    max_items: int = 7

    def __post_init__(self):
        if len(items) > max_items:
            raise ValueError('Too many items!')

pc = PC(name=name)

# get player name
# generate location, encounter, and item decks
# display quest text
# loop:
#   select a location
#   pick item cards
#   pick encounter cards
#   display situation, ask for command
#   output results
#   draw location card(s) and, if appropriate, ask the player to select among them

