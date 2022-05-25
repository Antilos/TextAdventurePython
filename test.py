from igraph import Graph

from game import Game
from room import Room
from command import Command
from custom_commands import MoveCommand

if __name__ == '__main__':
    cmd = Command("test")
    move = MoveCommand("move")

    cmds = [
        cmd,
        move,
    ]

    room1 = Room("test_room", "This is a test room")
    room2 = Room("room2", "This is a second room")

    rooms = [
        (room1, [room2]),
        (room2, []),
    ]

    room_graph = Graph(
        n = len(rooms),
    )

    for i, vs in enumerate(room_graph.vs):
        vs["name"] = rooms[i][0].name
        vs["room"] = rooms[i][0]
    
    for room, exits in rooms:
        for exit in exits:
            room_graph.add_edge(room.name, exit.name, state="open")

    print(room_graph)

    game = Game(cmds, room_graph, room, input_parser=lambda x : (x.split()[0], x.split()[1:]) if x else None, welcome_message="Hello to the test game")

    game.start()