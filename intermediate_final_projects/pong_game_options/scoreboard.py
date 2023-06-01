from turtle import Turtle

# Scoreboard 클래스 선언 
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")        # 점수판 색상 설정 
        self.penup()               # 선 없애기 설정 
        self.hideturtle()          # 가운데 turtle 숨기기 설정 
        self.l_score = 0           # 왼쪽 패들 초기 점수 값 
        self.r_score = 0           # 오른쪽 패들 초기 점수 값 
        self.update_scoreboard()   # 초기화할 때, 점수가 났을 때 호출 
    
    # 점수판 업데이트 관련 기능의 메소드
    def update_scoreboard(self):
        self.clear()                # 점수가 올라갈 때 마다 중복된 숫자를 제거하기 위한 설정 
        self.goto(-100, 200)        # 왼쪽 점수판 위치 설정 
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))  # 왼쪽 점수판 각종 설정들
        self.goto(100, 200)         # 오른쪽 점수판 위치 설정 
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))  # 오른쪽 점수판 각종 설정들 
    
    # 왼쪽 점수판 점수 설정의 메소드 
    def l_point(self):
        self.l_score += 1            # 점수 1점씩 증가 
        self.update_scoreboard()     # update_scoreboard 메소드 호출 
        
    # 오른쪽 점수판 점수 설정의 메소드    
    def r_point(self):
        self.r_score += 1            # 점수 1점씩 증가 
        self.update_scoreboard()     # update_scoreboard 메소드 호출 