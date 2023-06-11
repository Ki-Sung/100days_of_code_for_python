# 모둘 선언 
from turtle import Turtle

# 상수 설정 
STARTING_POSITION = (0, -280)   # turtle 시작점 설정 
MOVE_DISTANCE = 10              # turtle의 움직이는 거리수 
FINISH_LINE_Y = 280             # 도작점 좌표수 

# 클래스 선언
class Player(Turtle):
    # 초기 설정
    def __init__(self):
        super().__init__()
        self.shape('turtle')            # Turtle 모양 설정 
        self.color('green')             # Turtle 색성 설정 
        self.penup()                    # Turtle 생성되는 선 생략 
        self.goto(STARTING_POSITION)    # Turtle 시작점 설정 
        self.setheading(90)             # Turtle 방향 설정 
    
    # 화살표 위 방향키를 눌렀을 때, 키 이벤트를 설정 하는 메소드
    def go_up(self):
        self.forward(MOVE_DISTANCE)     # 위로 가는 움직이는 거리수 설정
    
    
