import cmd
import sys
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    List,
    TextIO,
)


@dataclass()
class CLI(cmd.Cmd):
    completekey: str = "tab"
    cmdqueue: List[str] = field(default_factory=list)
    stdin: TextIO = sys.stdin
    stdout: TextIO = sys.stdout
    intro: str = "Welcome!"

    def do_quit(self, line):
        print("\n")
        return True

    def help_quit(self):
        print("Exits the game.")
