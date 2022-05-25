from command import Command
from game import Game

class MoveCommand(Command):
    def __call__(self, game_instance:Game, args):
        target = args[0]

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
