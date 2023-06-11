# 모둘 선언 
from turtle import Turtle

# 상수 설정 
STARTING_POSITION = (0, -280)   # turtle 시작점 설정 
MOVE_DISTANCE = 10              # turtle의 움직이는 거리수 
FINISH_LINE_Y = 280             # 도작점 좌표수 

# 각종 player 설정을 위한 Player 클래스 선언
class Player(Turtle):
    # 초기 설정
    def __init__(self):
        super().__init__()
        self.shape('turtle')            # Turtle 모양 설정 
        self.color('green')             # Turtle 색성 설정 
        self.penup()                    # Turtle 생성되는 선 생략 
        self.got_to_start()             # Turtle 시작점 설정 
        self.setheading(90)             # Turtle 방향 설정 
    
    # 화살표 위 방향키를 눌렀을 때, 키 이벤트를 설정 하는 메소드
    def go_up(self):
        self.forward(MOVE_DISTANCE)     # 위로 가는 움직이는 거리수 설정
        
    # 처음부터 시작점으로 되돌리기 위한 설정 메소드 
    def got_to_start(self):
        self.goto(STARTING_POSITION)    # 상수로 설정한 STARTING_POSITION로 되돌아 가기
        
    # 결승선 도착시 생성되는 이벤트 관련 설정 메소드 
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:   # 만약 y값이 도착점 좌표수(280) 보다 놓다면, 
            return True                   # True를 반환 
        else:
            return False                  # 만약 아니라면 False를 반환 
