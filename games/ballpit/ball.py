class Ball:
    character = 'O'
    a=0
    acc=1
    samecount=0
    last=(0,0)
    def __init__(self, height,a):
        self.position = (0,height)
        self.a=a
    def play_turn(self, game):
        self.acc+=.5
        x=int(self.acc)
        if game.on_board((x,int(self.mather(self.acc,game.get_agent_by_name('arrow').position[1],self.a)))):
            self.position = ((x,int(self.mather(self.acc,game.get_agent_by_name('arrow').position[1],self.a))))
        game.log(self.position)
        if self.position==self.last:
            self.samecount+=1
        else:
            self.last=self.position
            self.samecount=0
        if self.samecount>4:
            posx=self.position[0]
            game.remove_agent_by_name('theball')
            a=(posx,29)
            char=game.get_agents_by_position()[a][0].character
            if char=="X":
                game.end()
            else:
                game.state['score']+=int(char)
            
            
            #game.log(game.get_agents_by_position(a))
        '''if len(game.get_agents_by_position()[self.position])==2:
            b=game.get_agents_by_position()[self.position].copy()
            game.log(b)
            
            b.remove('theball')
            n=game.get_agent_by_name(b[0])
            log(n)
        '''
    #y=(1/(4a))x^2)
    def mather(self,x,y,a):
        return int(round(y+(1/(a/2))*(x/2.8)**2))