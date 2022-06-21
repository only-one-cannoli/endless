import cmd

from .python.classes import PC
from .python.functions import check_name

if __name__ == "__main__":

    name_ok = False
    while name_ok is False:
        name: str = input("What is your name? ")
        name_ok = check_name(name)
    print("That's a good name!")

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
