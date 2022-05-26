from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game

class Item(ABC):
    def __init__(self, name, description=None, is_consumable=False) -> None:
        self.name = name
        self.description = description
        self.is_consumable = is_consumable
        

    @abstractmethod
    def use(self, game_instance:'Game'):
        # raise NotImplementedError("Use of Item is an abstract method")
        ...

class Inventory:
    def __init__(self) -> None:
        self.items = {}

    def get_item(self, item_name:str):
        try:
            return self.items[item_name]
        except KeyError:
            return None

    def add_item(self, item:Item):
        self.items[item.name] = item

    def remove_item(self, item_name:str) -> Item:
        return self.items.pop(item_name, None)