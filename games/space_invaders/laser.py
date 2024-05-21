class Laser:
    character = "|"
    color = "aqua"

    def __init__(self, position, going_up):
        self.position = position
        self.going_up = going_up

    def play_turn(self, game):
        x,y = self.position
        gx, gy = game.board_size
        agents_by_position = game.get_agents_by_position()
        if self.should_move(game.turn_number):
            if self.going_up and y==0:
                game.remove_agent(self)
            elif not self.going_up and y==gy - 1:
                game.remove_agent(self)
            elif self.going_up:
                new_position = (x, y - 1)
                if agents_by_position[new_position]:
                    game.remove_agent(self)
                    for agent in agents_by_position[new_position]:
                        game.remove_agent(agent)
                else: 
                    self.position = new_position
            else:
                new_position = (x, y+1)
                player = game.get_agent_by_name(player)
                if player.position == new_position:
                    game.end()
                else:
                    self.position = new_position

    def should_move(self, turn_number):
        return True