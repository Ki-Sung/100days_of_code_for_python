from turtle import Turtle

# pong 클래스 생성 
class Paddle(Turtle):
    def __init__(self, position):                        # position을 지정하는 인자 지정
        super().__init__()
        self.shape('square')                             # turtle 모양 설정 
        self.color('white')                              # paddle 색상 설정 
        self.shapesize(stretch_wid=5, stretch_len=1)     # paddle 사이즈 설정 
        self.penup()                                     # 선 삭제
        self.goto(position)                              # paddle 위치 설정
    
    # 위 방향키를 눌렀을 때, 동작하는 기능의 메소드
    def go_up(self):
        new_y = self.ycor() + 20            # x의 위치는 고정이니 y값만 설정
        self.goto(self.xcor(), new_y)       # x, y 값 기준으로 위치 설정
        
    # 아래 방향키를 눌렀을 때, 동작하는 기능의 메소드
    def go_down(self):
        new_y = self.ycor() - 20            # x의 위치는 고정이니 y값만 설정
        self.goto(self.xcor(), new_y)       # x, y 값 기준으로 위치 설정