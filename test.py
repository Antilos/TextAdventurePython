from igraph import Graph
from components.items import CoinItem
from components.player import Player

from game import Game
from room import Room
from command import Command
from custom_commands import MoveCommand

from built_in_commands import move_command, exit_command, take_command, drop_command, use_item_command

def create_room_graph(rooms:list[tuple[Room, list[Room]]]):
    room_graph = Graph(
        n = len(rooms),
    )

    for i, vs in enumerate(room_graph.vs):
        vs["name"] = rooms[i][0].name
        vs["room"] = rooms[i][0]
    
    for room, exits in rooms:
        for exit in exits:
            room_graph.add_edge(room.name, exit.name, state="open")

    return room_graph

if __name__ == '__main__':
    test_cmd_method = lambda game_instance, y: print(f"Test Command {y}")
    test_cmd_parser = lambda s : s
    cmd = Command("test", method=test_cmd_method, parser=test_cmd_parser)
    move = move_command

    cmds = [
        cmd,
        move,
        exit_command,
        take_command,
        drop_command,
        use_item_command
    ]

    room1 = Room("test_room", "This is a test room")
    room2 = Room("room2", "This is a second room")

    room1.inventory.add_item(CoinItem())

    rooms = [
        (room1, [room2]),
        (room2, []),
    ]

    room_graph = create_room_graph(rooms)

    components = {
        'player':Player()
    }

    input_parser = lambda x : (x.split()[0], " ".join(x.split()[1:])) if x else None

    game = Game(
        commands=cmds,
        room_graph=room_graph,
        starting_room=room1,
        components=components,
        input_parser=input_parser,
        welcome_message="Hello to the test game"
    )

    game.start()