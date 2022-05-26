from typing import Any, Callable, Protocol
from inspect import signature

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game

class CommandMethod(Protocol):
    def __call__(self, game_instance:'Game', *args: Any) -> None: ...

class Command():
    def __init__(self, command:str, method:CommandMethod, parser:Callable[[str], list]) -> None:
        self.command = command
        self.method = method
        self.parser = parser
        self._num_params = len(signature(method).parameters) - 1 # The first parameter is the game instance
    
    @property
    def num_params(self) -> int:
        return self._num_params

    def __call__(self, game_instance, args:str) -> None:
        params = self.parser(args)
        if params != None:
            if num_parser_params := len(params) == self.num_params:
                self.method(game_instance, *params)
            else:
                raise ValueError(f"""
                Number of parameters returned by parser ({num_parser_params}) doesn't match the number of parameters of the command ({self.num_params}).
                This may be cause by incorrect user input, or by incorrect implementation of the parser method itself.
                """)
        else:
            raise ValueError(f"""The command parser was unable to parse the command arguments into anything meaningfull""")

class CommandFactory():
    ...