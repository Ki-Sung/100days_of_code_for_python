from turtle import Turtle

# 상수선언 
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

# 스코어 제어 클래스 
class Scoreboard(Turtle):
    # 초기화 메소드 
    def __init__(self):
        super().__init__()
        self.score = 0          # 초기 점수 
        with open("snake_game_options/data.txt") as data:
            self.high_score = int(data.read())    # 최고 점수판을 위한 초기 점수 지정
        self.color("white")     # 점수판 색상 설정 
        self.penup()            # 선 나오지 않게 설정 
        self.goto(0, 270)       # 지정한 위치에 점수판 위치 설정   
        self.hideturtle()       # 점수판에 나오는 turtle 숨기기 설정 
        self.update_scoreborad()  # update_scoreboard 메소드 불러오기 
    
    # 점수판 설정 메소드
    def update_scoreborad(self):
        self.clear()                           # 점수가 겹쳐 보이기 때문에, 증가할 때마다 새로운 점수 갱신 
        self.write(
                arg=f'Score: {self.score} Hight Score: {self.high_score}',    # Turtle 화면에 문자 출력 
                move=False,                                                   # 움직임 설정 
                align=ALIGNMENT,                                              # 가운데 정렬 
                font=FONT)                                                    # 폰트 설정
        
    # 게임 종료 후 점수판에 최고 점수를 기록하기 위한 설정 메소드 
    def reset(self):
        # 1. 최고 점수 업데이트
        if self.score > self.high_score:   # 만약에 현재 점수가 현 최고 점수보다 높다면,
            self.high_score = self.score   # high_score에 현재 높은 점수 저장
            with open("snake_game_options/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        
        # 2. 점수 재설정 
        self.score = 0                     # 그 다음 시작할 점수 재설정 
        self.update_scoreborad()           # 점수 업데이트
    
    # # 게임 종료 표시 메소드 
    # def game_over(self):
    #     self.goto(0, 0)                        # 종료 표시 위치 설정 
    #     self.write(
    #             arg='Game Over',               # Turtle 화면에 문자 출력 
    #             move=False,                    # 움직임 설정 
    #             align=ALIGNMENT,               # 가운데 정렬 
    #             font=FONT)                     # 폰트 설정
    
    
    # 점수판 점수 증가 메소드     
    def increase_score(self):
        self.score += 1           # 점수 1씩 증가 (만약 먹이가 닿으면)
        self.update_scoreborad()  # update_scoreboard 메소드 불러오기 