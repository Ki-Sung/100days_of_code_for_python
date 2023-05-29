from turtle import Turtle

# Ball 클래스 생성 
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')       # ball 색상 설정 
        self.shape('circle')      # ball 모양 설정 
        self.penup()              # 선 없애기 
        
    def move(self):
        new_x = self.xcor() + 10  # ball x 좌표설정 
        new_y = self.ycor() + 10  # ball y 좌표설정 
        self.goto(new_x, new_y)   # 설정한 x, y 좌표로 이동 