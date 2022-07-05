"""
cli.py
Uses the `cmd` package to set up a command-line interface for the game.
"""

import cmd
import sys
from dataclasses import dataclass, field
from typing import List, TextIO

# pylint: disable=unnecessary-pass


@dataclass()
class CLI(cmd.Cmd):
    """
    Sets up our command-line interface.
    """

    completekey: str = "tab"
    cmdqueue: List[str] = field(default_factory=list)
    stdin: TextIO = sys.stdin
    stdout: TextIO = sys.stdout
    intro: str = "Welcome!"

    # pylint: disable-next=unused-argument
    def do_quit(self, line):
        """
        Creates a `quit` command.
        """
        print("\n")
        return True

    def help_quit(self):
        """
        Provides help for the `quit` command.
        """
        print("Exits the game.")

    def do_fight(self, line):
        """
        Creates a `fight` command.
        """
        pass

    def help_fight(self):
        """
        Provides help for the `fight` command.
        """
        print(
            "Attack any hostile creatures present.  Supply the name of an item card in your hand to\
            use that item in your attack."
        )

    def do_run(self, line):
        """
        Creates a `run` command.
        """
        pass

    def help_run(self):
        """
        Provides help for the `run` command.
        """
        print("Escape from the current location to another.")

    def do_bribe(self, line):
        """
        Creates a `bribe` command.
        """
        pass

    def help_bribe(self):
        """
        Provides help for the `bribe` command.
        """
        print(
            "Offer an item in your possession to one hostile creature so that it will not attack\
            you."
        )

    def do_move(self, line):
        """
        Creates a `move` command.
        """
        pass

    def help_move(self):
        """
        Provides help for the `move` command.
        """
        print(
            "Move from your current location to another.  Cannot be used if hostile creatures are\
            present."
        )

    def do_get(self, line):
        """
        Creates a `get` command.
        """
        pass

    def help_get(self):
        """
        Provides help for the `get` command.
        """
        print("Pick up an item.  Cannot be used if hostile creatures are present.")
