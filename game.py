from re import split
from typing import Callable, Optional, Any
from igraph import Graph

from room import Room
from command import Command


class Game():
    def __init__(self,
            commands:list[Command],
            room_graph:Graph,
            starting_room:Room,
            input_parser:Callable[[str], tuple[str, str]],

            components:Optional[dict[str, Any]]=None,
            welcome_message:Optional[str] = None,
            unknown_cmd_msg:str = "Unknown Command",
            room_description_on_enter:str = 'long'
        ) -> None:

        self.commands = {cmd.command:cmd for cmd in commands}
        self.room_graph = room_graph
        self.input_parser = input_parser
        self.welcome_message = welcome_message

        self.current_room = starting_room

        self.unknown_cmd_msg = unknown_cmd_msg
        self.room_description_on_enter = room_description_on_enter

        if components != None:
            for component_name, component in components.items():
                setattr(self, component_name, component)

    @property
    def current_room(self) -> Room:
        return self._current_room

    @current_room.setter
    def current_room(self, value : Room):
        assert(isinstance(value, Room))
        self._current_room = value

    def change_room(self, room):
        self.current_room = room
        if self.room_description_on_enter == 'long':
            print(room.description)
        elif self.room_description_on_enter == 'short':
            print(room.short_description)

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

    def get_command(self) -> tuple[Command, str]:
        player_input = input(">")
        return self.input_parser(player_input)

    def exit(self):
        print("[GAME] Exiting. Good Bye!")
        exit()

    def run(self) -> None:
        while True:
            if tmp := self.get_command():
                cmd_name, args = tmp
                try:
                    cmd = self.commands[cmd_name]
                    cmd(self, args)
                except KeyError:
                    print(self.unknown_cmd_msg)
                except ValueError:
                    print(f"[DEBUG] wrong number of params. {self.unknown_cmd_msg}")
            else:
                print(self.unknown_cmd_msg)

    def start(self) -> None:
        if self.welcome_message:
            print(self.welcome_message)
        try:
            self.run()
        except KeyboardInterrupt:
            self.exit()
