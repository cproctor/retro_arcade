from retro.game import Game
#from ball import Ball
from aimer import Aimer
from lineGenerator import LineGenerator
from power import Power
from numbersP import P1,P2,P3,P4,P5,P6,P7
from launch import BallLaunch

def main():
    board_size = (30, 30)
    #ship = Spaceship(board_size)
    generator=LineGenerator()
    aim=Aimer()
    power=Power()
    p1=P1()
    p2=P2()
    p3=P3()
    p4=P4()
    p5=P5()
    p6=P6()
    p7=P7()
    launch=BallLaunch()
    game = Game([generator,aim,power,p1,p2,p3,p4,p5,p6,p7,launch], {"score": 0}, board_size=board_size,framerate=15)
    game.play()
