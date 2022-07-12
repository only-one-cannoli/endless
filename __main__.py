"""
__main__.py
Calls and integrates materials from subfolders in the repo.
"""

from .src.cli import CLI
from .src.functions import check_name
from .src.state import PC

if __name__ == "__main__":

    name_ok: bool = False
    while name_ok is False:
        name: str = input("What is your name? ")
        name_ok, message = check_name(name)
        print(message)

    pc = PC(name=name)

    CLI().cmdloop()


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
