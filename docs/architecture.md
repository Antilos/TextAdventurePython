# Text Adventure Game Library
This file contains a short overview of the high level architecture of the Text Adventure Game library

## Game
An object that holds all rooms in the game and processes commands.
The object is extensible through components that commands may use.

### Loop
1. Read user input
2. Pass the input through Input Parser, which extracts a command and its arguments
3. Invoke a Command, passing it arguments

### Room Graph
The game keeps a graph of rooms, signifying adjacency.

## Commands
Command is a callable object. When the command is called, it recieves an instance of Game, which it is supposed to modify, and a list of arguments. It passes the arguments through an argument parser, receiving a new list, then executes it