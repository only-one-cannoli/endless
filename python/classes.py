from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class PC:
    """
    Player character
    """

    name: str
    hp: int = 3
    max_hp: int = 3
    abilities: Optional[List[str]] = []
    items: Optional[List[str]] = []
    max_items: int = 5

    def __post_init__(self):
        if len(items) > max_items:
            raise ValueError("Too many items!")
