from laser import Laser

class Player:
    name = "ship"
    character = "X"

    def __init__(self, position):
        self.position = position
    
    def handle_keystroke(self, keystroke, game):
        x, y = self.position
        if keystroke.name in ("KEY_LEFT", "KEY_RIGHT"):
            if keystroke.name == "KEY_LEFT":
                new_position = (x - 1, y)
            else:
                new_position = (x + 1, y)
            if game.on_board(new_position):
                if game.is_empty(new_position):
                    self.position = new_position
                else:
                    game.end()

        elif keystroke.name == "KEY_UP":
            laser = Laser((x, y),True)
            game.add_agent(laser)

