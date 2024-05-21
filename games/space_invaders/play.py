from retro.game import Game
from player import Player
from invader import Invader
#from invaderSpawner import InvaderSpawner

WIDTH = 40
HEIGHT = 40

def main():
    player = Player((WIDTH//2,HEIGHT - 1))
    #spawner = InvaderSpawner() 
    state = {}
    game = Game([player], state, board_size=(WIDTH, HEIGHT))
    for i in range(5,35):
                for j in range(0, 4):
                    invader = Invader((i,j))
                    game.add_agent(invader)
    game.play()
