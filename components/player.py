from .inventory import Inventory

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game

class Player:
    def __init__(self) -> None:
        self.inventory = Inventory()