from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class PC:
    """
    Player character.
    """

    name: str
    hp: int = 3
    max_hp: int = 3
    abilities: Optional[Tuple[str, ...]] = tuple()
    items: Optional[Tuple[str, ...]] = tuple()
    max_items: int = 5

    def __post_init__(self):
        if len(self.items) > self.max_items:
            raise ValueError("Too many items!")
