import json
from dataclasses import dataclass
from typing import Protocol


class Card(Protocol):

    name: str

    def from_json(self):
        pass


@dataclass(frozen=True)
class Location:

    name: str


@dataclass(frozen=True)
class Creature:

    name: str


@dataclass(frozen=True)
class Item:

    name: str
