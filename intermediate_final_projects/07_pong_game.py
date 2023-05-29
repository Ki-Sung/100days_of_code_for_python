# 정리는 intermediate 폴더 쥬피터 노트북 파일 day22에 정리 

# 모듈 불러오기 
import time
from turtle import Screen
from pong_game_options.paddle import Paddle
from pong_game_options.ball import Ball

# Screen 설정
screen = Screen()                      # 객체선언 
screen.setup(width=800, height=600)    # Screen 크기 설정 (800X600)
screen.bgcolor('black')                # Screen 백그라운드 설정 (블랙)
screen.title('Pong')                   # 게임 타이틀 설정 
screen.tracer(0)                       # 애니메이션 제어 설정 -> 0: 애니메이션 끄기

# Paddle 클래스로 객체 선언 
r_paddle = Paddle((350, 0))            # 오른쪽 paddle 객체선언 (paddle 생성)
l_paddle = Paddle((-350, 0))           # 왼쪽 paddle 객체선언 (paddle 생성)

# Ball 클래스로 객체 선언 
ball = Ball()

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
    time.sleep(0.1)                # 반복문 돌 때마다 0.1초씩 정지(ball speed 설정)
    ball.move()                    # ball 움직임 실행
    
    # 벽과의 충돌 감지 이벤트 
    if ball.ycor() > 280 or ball.ycor() < -280:    # 만약 위치가 공의 y축이 280보다 크거나 공의 y축이 -280 보다 작다면
        # 공을 튕기는 옵션 (벽으로 부터)
        ball.bounce_y()
        
    # 패들과 충돌 감지 
    # 만약 오른쪽 paddle과 ball의 거리가 50 보다 가깝고(작고), ball의 위치가 320 보다 크거거나 왼쪽 paddle과 ball의 거리가 50 보다 가깝고(작고), ball의 위치가 -320 보다 작으면 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # 공을 튕겨내기 (paddle로 부터)
        ball.bounce_x()
        
    # 오른쪽 패들이 공을 놓칠 경우 
    # 만약 ball의 x좌표가 380보다 크다면,
    if ball.xcor() > 380:
        ball.reset_postion()
    
    # 왼쪽 패들이 공을 놓칠 경우 
    # 만약 ball의 x좌표가 -380보다 작다면,
    if ball.xcor() < -380:
        ball.reset_postion()
        
    
# 창 닫힘 설정
screen.exitonclick()                    # 커서를 누르면 종료
