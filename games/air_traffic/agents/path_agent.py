class Path:

    def __init__(self, direction_char, color, pos, plane):
        self.character = direction_char
        self.color = color
        self.position = pos
        self.plane = plane

    def play_turn(self, game):
        if self.plane.position == self.position:
            game.remove_agent(self)