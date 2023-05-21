# 정리는 intermediate 폴더 쥬피터 노트북 파일 day20, day21에 정리 

# 모듈 불러오기 
import time
from snake_game_options.snake import Snake  # 만든 Snake 함수 불러오기
from turtle import Screen, Turtle 

# Screen 설정 
screen = Screen()  # 객체 선언 
screen.setup(width=600,height=600)  # screen 크기 설정 (600 X 600)
screen.bgcolor("black")   # screen 백그라운컬러 설정 (블랙)
screen.title("Play Snake Game")  # 타이틀 설정 
screen.tracer(0)       # turtle의 애니메이션을 켜거나 끄기 위한 옵션 (여기서는 끄기) - 뱀 전체가 하나처럼 보이게하기 위함.


# 1. Snake 몸통 만들기 

# snake 객체 선언 
snake = Snake()

# 2. Snake 움직임 설정 
# 동작을 계속하게 하기 위해 while 문 작성 
game_is_on = True
while game_is_on:
    screen.update()    # 세그먼트(뱀)가 모두 만들어지면 화면 갱신
    time.sleep(0.1)      # 0.1초 지연

    # Snake 움직임을 위해 move 메소드 사용 
    snake.move()


# 창 닫힘 설정 
screen.exitonclick()   # 커서를 누르면 종료 설정