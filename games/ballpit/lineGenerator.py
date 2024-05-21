import random
from linePiece import LinePiece7,LinePiece5,LinePiece3,LinePiece1,LinePieceX
class LineGenerator:
    display = False
    #def __init__(self):
        #length:points
    check=-1   
    def play_turn(self, game):
        if game.state['score']!=self.check:
            if game.state['score']!=0:
                for i in range(30):
                    game.remove_agent_by_name(str(i))
            self.check=game.state['score']
            choosefrom=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
            choices=[]
            for i in [1,3,5,8]:
                tlist=[]
                for k in range(i):
                    hold=random.choice(choosefrom)
                    choosefrom.remove(hold)
                    tlist.append(hold)
                choices.append(tlist)
            all=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
            c =choices
            for line in c:
                if len(line)==8:
                    for i in line:
                        a=LinePiece7(i)
                        a.name=str(i)
                        game.add_agent(a)
                elif len(line)==5:
                    for i in line:
                        a=LinePiece5(i)
                        a.name=str(i)
                        game.add_agent(a)
                elif len(line)==3:
                    for i in line:
                        a=LinePiece3(i)
                        a.name=str(i)
                        game.add_agent(a)
                elif len(line)==1:
                    for i in line:
                        a=LinePiece1(i)
                        a.name=str(i)
                        game.add_agent(a)
                for ele in line:
                    all.remove(ele)
            for i in all:
                a=LinePieceX(i)
                a.name=str(i)
                game.add_agent(a)