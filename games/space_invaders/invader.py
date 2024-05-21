from random import randint

class Invader:
    character = "H"
    color = "gray"

    def __init__(self, position):
        self.position = position
    
    def move(self,game):
        x,y = self.position
        count = 0
        invaders = game.get_agents_by_position()
        if x == 0 and game.on_board((x, y+1)):
            #self.position = (x,y+1)
            for invader in invaders:
                if invader[0] == True:
                    invader[0].position = (invader[0].position[0], invader[0].position[1]+1)
            count += 1
        elif (not game.on_board((x+1, y))) and game.on_board(((x, y+1))):
            #self.position = (x, y+1)
            for invader in invaders:
                if invader[0] == True:
                    invader[0].position = (invader[0].position[0], invader[0].position[1]+1)
            count += 1
        elif count % 2 == 0:
            #self.position = (x+1, y)
            for invader in invaders:
                if invader[0] == True:
                    invader[0].position = (invader[0].position[0]+1, invader[0].position[1])
        else:
            #self.position = (x-1, y)
            for invader in invaders:
                if invader[0] == True:
                    invader[0].position = (invader[0].position[0]-1, invader[0].position[1])
        
    def play_turn(self, game):
        agents_by_position = game.get_agents_by_position()
        x,y = self.position
        #print(game.turn_number)
        #if not game.on_board((x, y+1)):
        #    game.end()
            
        if game.turn_number % 20 == 0:
            self.move(game)

        #if agents_by_position[self.position]:
        #    game.end()

    def get_agent_in_position(self, position, game):
        """Returns an agent at the position, or returns None. 
        game.get_agents_by_position always returns a list, which may
        contain zero, one, or multiple agents at the given position. 
        In the Beast game, we never allow more than one agent to be in 
        a position.
        """
        agents = game.get_agents_by_position()[position]
        if agents:
            return agents[0]

        

        
        
        

                    


        
    



