from retro.game import Game
from random import randint
from agents.path_agent import Path
from agents.airport_agent import Airport

class Plane:
    
    def __init__(self, char, Color, pos, direction, spawner):
        self.character = char
        self.saved_color = Color
        self.color = Color
        self.selected = False
        self.position = pos
        self.future_positions = []
        self.paths = []
        self.direction = direction
        self.spawner = spawner
        self.z = 1
        
    
    def handle_keystroke(self, keystroke, game):
            if self.selected == False:
                if keystroke == self.character:
                    self.selected = True
                    self.color = "white"
            elif self.selected == True:
                if keystroke.name == "KEY_LEFT":
                    if len(self.future_positions) == 0:
                        self.direction = 2
                        new_position = (self.position[0] - 1, self.position[1])
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path("<", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                    else:
                        self.direction = 2
                        new_position = (self.future_positions[-1][0]- 1, self.future_positions[-1][1])
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path("<", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                elif keystroke.name == "KEY_RIGHT":
                    if len(self.future_positions) == 0:
                        self.direction = 1
                        new_position = (self.position[0] + 1, self.position[1])
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path(">", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                    else:
                        self.direction = 1
                        new_position = (self.future_positions[-1][0] + 1, self.future_positions[-1][1])
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path(">", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                elif keystroke.name == "KEY_UP":
                    if len(self.future_positions) == 0:
                        self.direction = 4
                        new_position = (self.position[0], self.position[1] - 1)
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path("^", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                    else:
                        self.direction = 4
                        new_position = (self.future_positions[-1][0], self.future_positions[-1][1] - 1)
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path("^", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                elif keystroke.name == "KEY_DOWN":
                    if len(self.future_positions) == 0:
                        self.direction = 3
                        new_position = (self.position[0], self.position[1] + 1)
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path("v", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                    else:
                        self.direction = 3
                        new_position = (self.future_positions[-1][0], self.future_positions[-1][1] + 1)
                        if game.on_board(new_position):
                            self.future_positions.append(new_position)
                            path = Path("v", self.saved_color, new_position, self)
                            self.paths.append(path)
                            game.add_agent(path)
                elif keystroke == self.character:
                    self.selected = False
                    self.color = self.saved_color
                elif keystroke.name == "KEY_BACKSPACE":
                    self.future_positions = []
                    for path in self.paths:
                        game.remove_agent(path)
                    self.paths = []
                else: 
                    self.selected = False
                    self.color = self.saved_color
    def play_turn(self, game):
        if game.turn_number % 12 == 0:
            x,y = self.position
            if len(self.future_positions) == 0:
                if self.direction == 1:
                    self.position = (x + 1, y)
                if self.direction == 2:
                    self.position = (x - 1, y)
                if self.direction == 3:
                    self.position = (x, y + 1)
                if self.direction == 4:
                    self.position = (x, y - 1)
            else:
                new_position = self.future_positions.pop(0)
                self.position = new_position
            new_x,new_y = self.position
            agents = game.get_agents_by_position()
            agents_at_pos = agents.get((new_x, new_y))
            for agent in agents_at_pos:
                if type(agent) == Path and agent.plane == self:
                    self.paths.remove(agent)
                if type(agent) == Plane and agent != self:
                    agent.character = "*"
                    agent.color = "red"
                    self.character = "*"
                    self.color = "red"
                    for path in agent.paths:
                        game.remove_agent(path)
                    for path in self.paths:
                        game.remove_agent(path)
                    game.end()
                elif type(agent) == Airport:
                    if agent.color == self.saved_color:
                        game.remove_agent(self)
                        game.state["Planes Landed"] += 1
                        self.spawner.characters.append(self.character)
                        for path in self.paths:
                            game.remove_agent(path)
                    else:
                        agent.character = "*"
                        agent.color = "red"
                        game.end()
            if new_x == -1 or new_x == 64:
                self.character = "*"
                self.color = "red"
                game.end()
            if new_y == -1 or new_y == 32:
                self.character = "*"
                self.color = "red"
                game.end()
    
    