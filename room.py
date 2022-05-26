from components.inventory import Inventory


class Room():
    def __init__(self, name:str, description:str, exit_names=None, short_description:str=None) -> None:
        self.name = name
        self.description = description
        self.short_description = short_description if short_description else f"This is a {name}"

        self.inventory = Inventory()

        self._exits = exit_names

    @property
    def exits(self):
        return self._exits
    
    def add_exit(self, room:str):
        if self._exits == None:
            self._exits = []

        self._exits.append(room)
        # self.exits[room.name] = room