import random
from turtle import Turtle

# Food 클래스 선언 -Turtle 클래스를 상속 받음 
class Food(Turtle):
    # 초기화 메소드 
    def __init__(self):
        super().__init__() 
        self.shape('circle')           # turtle 모양 설정
        self.penup()                   # 선 나오지 않게 설정 
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # turtle 크기 설정
        self.color("blue")             # turtle 색상 설정
        self.speed('fastest')          # turtle 속도 설정
        self.refresh()                 # refresh 메소드 불러오기 
        
    def refresh(self):
        random_x = random.randint(-280, 280)  # turtle 위치 X축 - 랜덤으로 
        random_y = random.randint(-280, 280)  # turtle 위치 Y축 - 랜덤으로 
        self.goto(random_x, random_y)         # 지정한 x, y 축 기준 표시 