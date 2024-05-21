from invader import Invader

class InvaderSpawner:
    display = False
   
    def play_turn(self,game):
        for i in range(5,35):
            for j in range(0, 4):
                invader = Invader((i,j))
                game.add_agent(invader)