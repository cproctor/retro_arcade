# minesweeper_game.py
# ------------
# This class implements a simple minesweeper game on a 9x9 grid with 10 mines.

from retro.game import Game
from spawner import Spawner

def main():
    board_size = (9, 9)
    spawner = Spawner(board_size)
    game = Game([spawner], {"score": 0}, board_size=board_size,debug=True) # debug is on so you can see the instructions :)
    game.play()
