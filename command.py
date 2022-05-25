from typing import Any

class Command():
    def __init__(self, command:str, params:dict[str, type]=None) -> None:
        self.command = command
        self.params = params
    
    @property
    def num_params(self) -> int:
        return len(self.params) if self.params else 0

    def __call__(self, game_instance:'Game', *args: Any, **kwds: Any) -> Any:
        print("This is a command")