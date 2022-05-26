from command import Command

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game
    from room import Room

def move_command_method(game_instance:'Game', target:'Room') -> None:
        if target_room := game_instance.get_room_by_name(target):
            source_room = game_instance.current_room
            target_room = target_room["room"]
            
            if path := game_instance.get_path(source_room.name, target_room.name):
                if path["state"] == "open":
                    game_instance.change_room(target_room)
                else:
                    print(f"The path to {target} is blocked")
            else:
                print(f"No path to {target}")
        else:
            print(f"No path to {target}")

def move_command_parser(args:str) -> list:
    return args.split()[:1]

move_command = Command('move', move_command_method, move_command_parser)

def exit_command_method(game_instance:'Game') -> None:
    game_instance.exit()

def exit_command_parser(args:str) -> list:
    return []

exit_command = Command('exit', exit_command_method, exit_command_parser)

def take_command_method(game_instance:'Game', item_name) -> None:
    item = game_instance.current_room.inventory.remove_item(item_name)
    if item:
        game_instance.player.inventory.add_item(item)
        print(f"You take {item_name}")
    else:
        print(f"There is no {item_name} to take")

def take_command_parser(args:str) -> list:
    return args.split()[:1]

take_command = Command('take', take_command_method, take_command_parser)

def drop_command_method(game_instance:'Game', item_name) -> None:
    item = game_instance.player.inventory.remove_item(item_name)
    if item:
        game_instance.current_room.inventory.add_item(item)
        print(f"You dropped {item_name}")
    else:
        print(f"You don't have any {item_name}")

def drop_command_parser(args:str) -> list:
    return args.split()[:1]

drop_command = Command('drop', drop_command_method, drop_command_parser)

def use_item_command_method(game_instance:'Game', item_name) -> None:
    #TODO: Use items in rooms
    item = game_instance.player.inventory.get_item(item_name)
    if item:
        item.use(game_instance)
        if item.is_consumable:
            game_instance.player.inventory.remove_item(item_name)
    else:
        print(f"You don't have any {item_name}")

def use_item_command_parser(args:str) -> list:
    return args.split()[:1]

use_item_command = Command('use', use_item_command_method, use_item_command_parser)