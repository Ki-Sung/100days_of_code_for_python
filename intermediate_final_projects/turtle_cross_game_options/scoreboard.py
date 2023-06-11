# 모둘 선언 
from turtle import Turtle

# 상수 설정 
FONT = ("Courier", 24, "normal")    # 점수판 글꼴 및 크기 설정 

# 점수판 설정 Scoreboard 클래스 선언
class Scoreboard(Turtle):
    # 초기 설정 
    def __init__(self):
        super().__init__()
        self.level = 1                 # 초기 레벨 설정 
        self.hideturtle()              # Turtle 가리기 설정 
        self.penup()                   # Turtle 생성되는 선 생략
        self.goto(-280, 250)           # level scoreborad 위치 설정 
        self.update_scoreboard()       # level scoreborad 사항 설정 (밑에 update_scoreboard 메소드 불러오기) 
    
    # level scoreborad 설정을 위한 메소드 
    def update_scoreboard(self):
        self.clear()                                                    # level scoreborad 겹치기 방지를 위한 clear 설정 
        self.write(f"Level: {self.level}", align='left', font=FONT)     # level scoreborad 폰트 및 위치, 문구 설정 
        
    # 레벨업 문구 설정 메소드
    def increase_level(self):
        self.level += 1             # 레벨 1씩 증가 
        self.update_scoreboard()    # update_scoreboard 메소드 불러오기
    
    # game over 문구 설정 메소드
    def game_over(self):
        self.goto(0, 0)                                         # game over 문구 위치 설정 
        self.write(f"Game Over", align='center', font=FONT)     # game over 문구, 위치 설정
