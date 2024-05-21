# cursor.py
# ------------
# This module defines a cursor agent class.

class Cursor:
    name = "cursor"
    character = 'O'
    revealed = True

    def __init__(self, position):
        self.position = position

    def handle_keystroke(self, keystroke, game):
        '''
        Move the cursor using arrow keys.
        '''
        x, y = self.position
        if keystroke.name in ("KEY_LEFT", "KEY_RIGHT", "KEY_UP", "KEY_DOWN"):
            if keystroke.name == "KEY_LEFT": 
                new_position = (x - 1, y)
            elif keystroke.name == "KEY_RIGHT": 
                new_position = (x + 1, y)
            elif keystroke.name == "KEY_UP":
                new_position = (x, y - 1)
            else:
                new_position = (x, y + 1)
            if game.on_board(new_position):
                if game.is_empty(new_position):
                    self.position = new_position

    def hide(self):
        '''
        This is called because I was calling this method based on an agent's location, but I don't need the
        cursor to do anything.
        '''
        pass
