# 정리는 intermediate 폴더 쥬피터 노트북 파일 day22에 정리 

# 모듈 불러오기 
from turtle import Turtle, Screen
# from pong_game_options.pong import Pong

# Screen 설정
screen = Screen()     # 객체선언 
screen.setup(width=800, height=600)    # Screen 크기 설정 (800X600)
screen.bgcolor('black')                # Screen 백그라운드 설정 (블랙)
screen.title('Pong')                   # 게임 타이틀 설정 
screen.tracer(0)                       # 애니메이션 제어 설정 -> 0: 애니메이션 끄기

paddle = Turtle()                               # Turtle 객체 선언 
paddle.shape('square')                          # turtle 모양 설정 
paddle.color('white')                           # paddle 색상 설정 
paddle.shapesize(stretch_wid=5, stretch_len=1)  # paddle 사이즈 설정 
paddle.penup()                                  # 선 삭제 
paddle.goto(350, 0)                             # paddel 위치 설정

# 위 방향키를 눌렸을 때, 동작하는 함수 
def go_up():
    new_y = paddle.ycor() + 20          # x의 위치는 고정이니 y값만 설정
    paddle.goto(paddle.xcor(), new_y)   # x, y 값 기준으로 위치 설정
    
# 아래 방향키를 눌렀을 때, 동작하는 함수
def go_down():
    new_y = paddle.ycor() - 20          # x의 위치는 고정이니 y값만 설정
    paddle.goto(paddle.xcor(), new_y)   # x, y 값 기준으로 위치 설정

#키 설정 
screen.listen()                    # 키 이벤트를 위한 설정으로 객체 선언 
screen.onkey(go_up, "Up")          # 방향키 위를 눌렀을 때 위로 20씩증가  
screen.onkey(go_down, "Down")      # 방향키 아래를 눌렀을 때 아래로 20씩 증가 

# game 실행을 위한 반복문 제어
game_is_on = True                  # 게임 실행중을 위한 설정 
while game_is_on:                  # 게임 실행중일 때
    screen.update()                # screen 업데이트


    
# 창 닫힘 설정
screen.exitonclick()                    # 커서를 누르면 종료
