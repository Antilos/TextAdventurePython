from .inventory import Item

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game

class CoinItem(Item):
    def __init__(self, name='coin', description='This is a copper coin.', is_consumable=False) -> None:
        super().__init__(name, description, is_consumable)

    def use(self, game_instance:'Game'):
        print(f"You bite the coin. It tastes like metal.")