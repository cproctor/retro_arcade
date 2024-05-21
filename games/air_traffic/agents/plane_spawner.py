from agents.plane_agent import Plane
from random import randint

class AirplaneSpawner:

    def __init__(self):
        self.display = False
        self.characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.colors = ["cyan", "magenta", "green"]

    def play_turn(self, game):
        if self.should_spawn_plane(game.state["Planes Landed"]):
            if len(self.characters) != 0:
                char_index = randint(0, len(self.characters) - 1)
                color_index = randint(0, len(self.colors) - 1)
                character = self.characters.pop(char_index)
                color = self.colors[color_index]
                side = randint(1,4)
                x = randint(8,55)
                y = randint(7, 20)
                if side == 1:
                    plane = Plane(character, color, (1, y), side, self)
                if side == 2:
                    plane = Plane(character, color, (63, y), side, self)
                if side == 3:
                    plane = Plane(character, color, (x, 1), side, self)
                if side == 4:
                    plane = Plane(character, color, (x, 31), side, self)
                game.add_agent(plane)
    
    def should_spawn_plane(self, score):
        if len(self.characters) == 10:
            return True
        if score < 5:
            return randint(0,10000) > 9980
        elif score < 10:
            return randint(0,10000) > 9960
        elif score < 20:
            return randint(0,10000) > 9900
        elif score < 30:
            return randint(0,10000) > 9850
        elif score < 40:
            return randint(0,10000) > 9800
        else:
            return randint(0,10000) > 9700