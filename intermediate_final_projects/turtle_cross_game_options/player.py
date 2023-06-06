# 상수 설정 
STARTING_POSITION = (0, -280)   # turtle 시작점 설정 
MOVE_DISTANCE = 10              # turtle의 움직이는 거리수 
FINISH_LINE_Y = 280             # 도작점 좌표수 

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
    
    
