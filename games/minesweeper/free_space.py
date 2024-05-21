# free_space.py
# ------------
# This module defines a free space agent class. It displays itself and (eventually)
# its neighbors if enter is pressed while the cursor is on it.

class FreeSpace:
    character = '*'
    display = True
    revealed = False
    neighbors = 0

    def __init__(self, position):
        self.position = position
        self.width , self.height = position

    def name_me(self, named):
        '''
        Give a free space a name.'''
        self.name = named

    def show(self):
        '''
        Used to turn display on. Necessary to be able to call upon a space based on its position.
        '''
        self.display = True

    def hide(self):
        '''
        Used to hide free spaces only if they have not already been revealed.
        '''
        if self.revealed == False:
            self.display = False

    def check_neighbors(self,game):
        '''
        Used to determine the number that should be shown when the space is revealed. Counts neighboring mines.
        '''
        names_of_mines = ["mine0","mine1","mine2","mine3","mine4","mine5","mine6","mine7","mine8","mine9"]
        if game.on_board((self.width + 1,self.height)):
            if len(game.get_agents_by_position()[(self.width + 1,self.height)]) != 0:
                if game.get_agents_by_position()[(self.width + 1,self.height)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if game.on_board((self.width - 1,self.height)):
            if len(game.get_agents_by_position()[(self.width - 1,self.height)]) != 0:
                if game.get_agents_by_position()[(self.width - 1,self.height)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if game.on_board((self.width,self.height + 1)):
            if len(game.get_agents_by_position()[(self.width,self.height + 1)]) != 0:
                if game.get_agents_by_position()[(self.width,self.height + 1)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if game.on_board((self.width,self.height - 1)):
            if len(game.get_agents_by_position()[(self.width,self.height - 1)]) != 0:
                if game.get_agents_by_position()[(self.width,self.height - 1)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if game.on_board((self.width + 1,self.height + 1)):
            if len(game.get_agents_by_position()[(self.width + 1,self.height + 1)]) != 0:
                if game.get_agents_by_position()[(self.width + 1,self.height + 1)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if game.on_board((self.width + 1,self.height - 1)):
            if len(game.get_agents_by_position()[(self.width + 1,self.height - 1)]) != 0:
                if game.get_agents_by_position()[(self.width + 1,self.height - 1)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if game.on_board((self.width - 1,self.height + 1)):
            if len(game.get_agents_by_position()[(self.width - 1,self.height + 1)]) != 0:
                if game.get_agents_by_position()[(self.width - 1,self.height + 1)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if game.on_board((self.width - 1,self.height - 1)):
            if len(game.get_agents_by_position()[(self.width - 1,self.height - 1)]) != 0:
                if game.get_agents_by_position()[(self.width - 1,self.height - 1)][0].name in names_of_mines:
                    self.neighbors = self.neighbors + 1
        if self.neighbors > 0:
            self.character = str(self.neighbors)

    def play_turn(self, game):
        '''
        Make sure a number is hidden when the cursor is over it. This is needed to allow the cursor to move
        over a spot where a number is.
        '''
        if (not game.is_empty(self.position)) and self.revealed and self.display == True:
            self.display = False
        elif game.is_empty(self.position) and self.revealed and self.neighbors > 0 and self.display == False:
            self.display = True


    def handle_keystroke(self, keystroke, game):
        '''
        When a space without a mine is selected, use a recursive algorithm defined below to reveal spaces.
        Then, check if all non-mine spaces have been revealed; if so, the game has been won.
        '''
        if keystroke.name in ("KEY_ENTER"):
            if not game.is_empty(self.position):
                if self.revealed == False:
                    board_width,board_height = game.board_size
                    for i in range(board_width):
                        for j in range(board_height):
                            try:
                                game.get_agent_by_name("freespace"+str(i)+str(j)).show()
                            except:
                                pass
                    self.reveal(game)
                    win = True
                    for i in range(board_width):
                        for j in range(board_height):
                            if len(game.get_agents_by_position()[(i,j)]) != 0:
                                if not game.get_agents_by_position()[i,j][0].revealed:
                                    win = False
                    if win == True:
                        game.log("You successfully isolated every mine! Congratulations! You've won!")
                        game.end()
                    for i in range(board_width):
                        for j in range(board_height):
                            try:
                                game.get_agent_by_name("freespace"+str(i)+str(j)).hide()
                            except:
                                pass

    def reveal(self,game):
        '''
        Recursive algorithm to reveal squares. Reveals itself and then if it has no neighboring mines,
        it asks all 8 of its neighbors (assuming none are off the map) to reveal themselves.
        '''
        self.revealed = True
        if self.neighbors == 0:
            if game.on_board((self.width + 1,self.height)):
                if len(game.get_agents_by_position()[(self.width + 1,self.height)]) != 0:
                    if not game.get_agents_by_position()[(self.width + 1,self.height)][0].revealed:
                        game.get_agents_by_position()[(self.width + 1,self.height)][0].reveal(game)
            if game.on_board((self.width - 1,self.height)):
                if len(game.get_agents_by_position()[(self.width - 1,self.height)]) != 0:
                    if not game.get_agents_by_position()[(self.width - 1,self.height)][0].revealed:
                        game.get_agents_by_position()[(self.width - 1,self.height)][0].reveal(game)
            if game.on_board((self.width,self.height + 1)):
                if len(game.get_agents_by_position()[(self.width,self.height + 1)]) != 0:
                    if not game.get_agents_by_position()[(self.width,self.height + 1)][0].revealed:
                        game.get_agents_by_position()[(self.width,self.height + 1)][0].reveal(game)
            if game.on_board((self.width,self.height - 1)):
                if len(game.get_agents_by_position()[(self.width,self.height - 1)]) != 0:
                    if not game.get_agents_by_position()[(self.width,self.height - 1)][0].revealed:
                        game.get_agents_by_position()[(self.width,self.height - 1)][0].reveal(game)
            if game.on_board((self.width + 1,self.height + 1)):
                if len(game.get_agents_by_position()[(self.width + 1,self.height + 1)]) != 0:
                    if not game.get_agents_by_position()[(self.width + 1,self.height + 1)][0].revealed:
                        game.get_agents_by_position()[(self.width + 1,self.height + 1)][0].reveal(game)
            if game.on_board((self.width + 1,self.height - 1)):
                if len(game.get_agents_by_position()[(self.width + 1,self.height - 1)]) != 0:
                    if not game.get_agents_by_position()[(self.width + 1,self.height - 1)][0].revealed:
                        game.get_agents_by_position()[(self.width + 1,self.height - 1)][0].reveal(game)
            if game.on_board((self.width - 1,self.height + 1)):
                if len(game.get_agents_by_position()[(self.width - 1,self.height + 1)]) != 0:
                    if not game.get_agents_by_position()[(self.width - 1,self.height + 1)][0].revealed:
                        game.get_agents_by_position()[(self.width - 1,self.height + 1)][0].reveal(game)
            if game.on_board((self.width - 1,self.height - 1)):
                if len(game.get_agents_by_position()[(self.width - 1,self.height - 1)]) != 0:
                    if not game.get_agents_by_position()[(self.width - 1,self.height - 1)][0].revealed:
                        game.get_agents_by_position()[(self.width - 1,self.height - 1)][0].reveal(game)
