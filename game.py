from re import split
from typing import Callable, Optional
from igraph import Graph

from room import Room
from command import Command


class Game():
    def __init__(self,
            commands:list[Command],
            room_graph:Graph,
            starting_room:Room,
            input_parser:Callable[[str], tuple[str, list[str]]],
            welcome_message = None,
            starting_room_index = 0
        ) -> None:

        self.commands = {cmd.command:cmd for cmd in commands}
        self.room_graph = room_graph
        self.input_parser = input_parser
        self.welcome_message = welcome_message

        self.current_room = starting_room

        self.unknown_cmd_msg = "Unknown Command"

    @property
    def current_room(self) -> Room:
        return self._current_room

    @current_room.setter
    def current_room(self, value : Room):
        assert(isinstance(value, Room))
        self._current_room = value

    def change_room(self, room):
        self.current_room = room

    def get_room_by_name(self, room_name):
        try:
            return self.room_graph.vs.find(room_name)
        except ValueError:
            return None

    def get_path(self, source_room_name, target_room_name):
        try:
            return self.room_graph.es.find(_source=source_room_name, _target=target_room_name)
        except ValueError:
            return None

    def get_command(self) -> tuple[Command, list]:
        player_input = input(">")
        return self.input_parser(player_input)

    def run(self) -> None:
        while True:
            if tmp := self.get_command():
                cmd_name, args = tmp
                try:
                    cmd = self.commands[cmd_name]
                    cmd(self, args)
                except KeyError:
                    print(self.unknown_cmd_msg)
            else:
                print(self.unknown_cmd_msg)

    def start(self) -> None:
        if self.welcome_message:
            print(self.welcome_message)
        try:
            self.run()
        except KeyboardInterrupt:
            print("[GAME] Exiting. Good Bye!")

def test_input_parser(in_str:str):
    ...

if __name__ == '__main__':
    cmd = Command("test")

    cmds = [
        cmd,
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
