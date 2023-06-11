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

# Player 클래스 객체 선언
player = Player()   

# CarManager 클래스 객체 선언 
car_manager = CarManager()                  

# 화면에 이벤트들 생성하기 위한 설정 
screen.listen()
# 화면 내 키 이벤트 설정
screen.onkey(player.go_up, 'Up')      # 위 화살표 키를 누르면 앞으로 전진하는 기능을 하는 메소드 설정 

# 게임 실행중 
game_is_on = True   
while game_is_on:     
    time.sleep(0.1)                    # 화면 갱신 시간 설정 0.1초 
    screen.update()                    # update를 이용하여 갱신 
    
    car_manager.create_car()           # 자동차 생성 메소드 불러오기 - 6번에 1번 꼴로 새 자동차가 만들어지도록 설정
    car_manager.move_cars()            # 자동차 움직임 설정 메소들 불러오기
    
    # 자동차(장애물) 충돌 감지 영역 
    for car in car_manager.all_cars:           # 모은 자동차 정보로 반복문 생성 
        if car.distance(player) < 20:          # 만약 자동차와 Turtle의 거리가 20 미만이면 (자동차(장애물)와 Turtle 객체까지의 거리가 20 이하인지 탐지)
            game_is_on = False                 # 게임 종료 
            
# 창 닫힘 설정 
screen.exitonclick()