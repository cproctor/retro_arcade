class Aimer:
    character = '⟶'
    name='arrow'
    position = (0,1)
    def handle_keystroke(self, keystroke, game):
        x,y = self.position
        if keystroke.name in ("KEY_UP", "KEY_DOWN"):
            if keystroke.name == "KEY_UP":
                new_position = (x, y-1)
            else:
                new_position = (x, y+1)
            if game.on_board(new_position) and new_position!=(0,0):
                if game.is_empty(new_position):
                    self.position = new_position    