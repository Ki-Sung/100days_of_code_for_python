import time                                                     # tutle 화면 갱신을 위해 time 모듈 뷸러오기 
from turtle import Screen                                       # turtle 화면 설정을 위해 turtle 모듈의 Screen 클래스 불러오기 
from turtle_cross_game_options.player import Player             # palyer 설정을 위해 생성한 Player 클래스 불러오기 
from turtle_cross_game_options.car_manager import CarManager    # 자동차 컨트롤을 위해 생성한 CarManager 클래스 불러오기 
from turtle_cross_game_options.scoreboard import Scoreboard     # 점수 및 레벨 설정을 위해 생성한 Scoreboard 클래스 불러오기

# 객체 선언 
screen = Screen()                      # Screen 객체 선언 

# 화면 사이즈 설정 
screen.setup(width=600, height=600)    # 600 x 600 사이즈로 화면 설정 
screen.title('Turtle Cross Game')
screen.tracer(0)                       # 화면 자동 갱신 기능 Off 설정 

player = Player()

# 게임 실행중 
game_is_on = True   
while game_is_on:     
    time.sleep(0.1)                    # 화면 갱신 시간 설정 0.1초 
    screen.update()                    # update를 이용하여 갱신 

# 창 닫힘 설정 
screen.exitonclick()