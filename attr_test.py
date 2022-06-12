from dataclasses import dataclass
import cmd
import sys
from typing import List, TextIO

class Player(cmd.Cmd):

    def __init__(self, name, health):
        self.name: str = name
        self.health: int = health
        self.completekey: str = 'tab'
        self.cmdqueue: List[str] = []
        self.stdin: TextIO = sys.stdin
        self.stdout: TextIO = sys.stdout
        self.intro: str = 'Welcome!'

player = Player(name='Patrick', health=100)
setattr(Player, 'do_foo', sum)

player.cmdloop()
