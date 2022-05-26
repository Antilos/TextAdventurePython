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