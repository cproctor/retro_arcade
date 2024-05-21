# mine.py
# ------------
# This module defines a mine agent class. It ends the game if enter is pressed while the cursor is over it.

class Mine:
    character = ''
    revealed = True

    def __init__(self, position):
        self.position = position

    def name_me(self, named):
        '''
        Assign a name to a given mine.
        '''
        self.name = named

    def handle_keystroke(self, keystroke, game):
        '''
        This ends the game if enter is pressed while the cursor is over a mine.
        '''
        if keystroke.name in ("KEY_ENTER"):
            if game.get_agent_by_name("cursor").position == self.position:
                for i in range(10):
                    game.get_agent_by_name("mine"+str(i)).character = 'M'
                game.get_agent_by_name("cursor").character = 'M'
                game.log("You hit a mine! Game over.")
                game.end()

    def play_turn(self, game):
        '''
        Make sure the mine is hidden when the cursor is over it. This is needed to allow the cursor to move
        over a spot where a mine is.
        '''
        if (not game.is_empty(self.position)):
            self.display = False
        elif game.is_empty(self.position):
            self.display = True

    def reveal(self):
        '''
        This is called because I was calling this method based on an agent's location, but I don't need the
        mine to do anything.
        '''
        pass

    def show(self):
        '''
        This is called because I was calling this method based on an agent's location, but I don't need the
        mine to do anything.
        '''
        pass

    def hide(self):
        '''
        This is called because I was calling this method based on an agent's location, but I don't need the
        mine to do anything.
        '''
        pass

    def check_neighbors(self,game):
        '''
        This is called because I was calling this method based on an agent's location, but I don't need the
        mine to do anything.
        '''
        pass



