# spawner.py
# ------------
# This module defines a spawner agent class. It spawns mines and then fills the remaining spots with free spaces

from random import randint
from mine import Mine
from free_space import FreeSpace
from cursor import Cursor

class Spawner:
    display = False

    def __init__(self, board_size):
        width, height = board_size
        self.board_width, self.board_height = width, height

    def play_turn(self, game):
        '''
        Creates all other agents and prints instructions when the game begins.
        '''
        if game.turn_number == 1:
            # First spawn 10 mines
            for i in range(10):
                mine = Mine(((randint(0, self.board_width - 1)),(randint(0, self.board_height - 1))))
                mine.name_me("mine"+str(i))
                while not game.is_empty(mine.position): # Ensure mines are not in the same location
                    mine = Mine(((randint(0, self.board_width - 1)),(randint(0, self.board_height - 1))))
                    mine.name_me("mine"+str(i))
                game.add_agent(mine)
            # Then spawn free spaces everywhere there is not a mine.
            for i in range(self.board_width):
                for j in range(self.board_height):
                    if game.is_empty((i,j)):
                        free_space = FreeSpace((i,j))
                        free_space.name_me("freespace"+str(i)+str(j))
                        game.add_agent(free_space)
            # Now ask all free spaces to keep track of their neighbors that are mines and hide themselves.
            for i in range(self.board_width):
                for j in range(self.board_height):
                    if len(game.get_agents_by_position()[(i,j)]) != 0:
                        game.get_agents_by_position()[(i,j)][0].check_neighbors(game)
                        game.get_agents_by_position()[(i,j)][0].hide()
            # Now create a cursor.
            cursor = Cursor((self.board_width - 1, self.board_height - 1))
            game.add_agent(cursor)   
            # Print instructions.
            game.log("To move, use the arrow keys. You may have to")
            game.log("press an arrow key more than once to move.")
            game.log("Please make sure the cursor is where you want it")
            game.log("before selecting a space. To select a space, ")
            game.log("press return. The game is over when all spots")
            game.log("with mines are surrounded by numbers.")
