# 정리는 intermediate 폴더 쥬피터 노트북 파일 day22에 정리 

# 모듈 불러오기 
from turtle import Screen
from pong_game_options.paddle import Paddle

# Screen 설정
screen = Screen()     # 객체선언 
screen.setup(width=800, height=600)    # Screen 크기 설정 (800X600)
screen.bgcolor('black')                # Screen 백그라운드 설정 (블랙)
screen.title('Pong')                   # 게임 타이틀 설정 
screen.tracer(0)                       # 애니메이션 제어 설정 -> 0: 애니메이션 끄기

# Paddle 클래스로 객체 선언 
r_paddle = Paddle((350, 0))            # 오른쪽 paddle 객체선언 (paddle 생성)
l_paddle = Paddle((-350, 0))           # 왼쪽 paddle 객체선언 (paddle 생성)

#키 설정 
screen.listen()                         # 키 이벤트를 위한 설정으로 객체 선언 

# 오른쪽 paddle 키 설정 
screen.onkey(r_paddle.go_up, "Up")      # 방향키 위를 눌렀을 때 위로 20씩증가  
screen.onkey(r_paddle.go_down, "Down")  # 방향키 아래를 눌렀을 때 아래로 20씩 증가 

# 왼쪽 paddel 키 설정
screen.onkey(l_paddle.go_up, "w")       # 방향키 위를 눌렀을 때 위로 20씩증가  
screen.onkey(l_paddle.go_down, "s")     # 방향키 아래를 눌렀을 때 아래로 20씩 증가 

# game 실행을 위한 반복문 제어
game_is_on = True                  # 게임 실행중을 위한 설정 
while game_is_on:                  # 게임 실행중일 때
    screen.update()                # screen 업데이트


    
# 창 닫힘 설정
screen.exitonclick()                    # 커서를 누르면 종료
