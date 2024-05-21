class Power:
    #▯
    character = '▮'
    position = (23,0)
    name='meter'
    def handle_keystroke(self, keystroke, game):
        x,y = self.position
        if keystroke.name in ("KEY_RIGHT", "KEY_LEFT"):
            if keystroke.name == "KEY_RIGHT":
                new_position = (x+1, y)
            else:
                new_position = (x-1, y)
            if game.on_board(new_position):
                if game.is_empty(new_position):
                    if new_position in [(23,0),(24,0),(25,0),(26,0),(27,0),(28,0),(29,0)]:
                        self.position = new_position