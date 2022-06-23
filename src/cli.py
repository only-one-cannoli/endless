"""
cli.py
Uses the `cmd` package to set up a command-line interface for the game.
"""

import cmd
import sys
from dataclasses import dataclass, field
from typing import List, TextIO


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
