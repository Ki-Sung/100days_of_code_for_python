# 정리는 intermediate 폴더 쥬피터 노트북 파일 day20, day21에 정리 

# 모듈 불러오기 
import time
from snake_game_options.snake import Snake  # 만든 Snake 클래스 불러오기
from snake_game_options.food import Food    # 만든 Food 클래스 불러오기 
from turtle import Screen 

# Screen 설정 
screen = Screen()  # 객체 선언 
screen.setup(width=600,height=600)  # screen 크기 설정 (600 X 600)
screen.bgcolor("black")   # screen 백그라운컬러 설정 (블랙)
screen.title("Play Snake Game")  # 타이틀 설정 
screen.tracer(0)       # turtle의 애니메이션을 켜거나 끄기 위한 옵션 (여기서는 끄기) - 뱀 전체가 하나처럼 보이게하기 위함.


# 1. Snake 몸통 만들기 

# snake 객체 선언 
snake = Snake()
food = Food()

# 3. snake 움직임 컨트롤을 위한 설정 
screen.listen()
screen.onkey(snake.up, "Up")          # 움직이는 방향을 위한 메소드, 키 설정 - 여기서 키는 키보드 버튼
screen.onkey(snake.down, "Down")      # 움직이는 방향을 위한 메소드, 키 설정 - 여기서 키는 키보드 버튼
screen.onkey(snake.left, "Left")      # 움직이는 방향을 위한 메소드, 키 설정 - 여기서 키는 키보드 버튼
screen.onkey(snake.right, "Right")    # 움직이는 방향을 위한 메소드, 키 설정 - 여기서 키는 키보드 버튼

# 2. Snake 움직임 설정 
# 동작을 계속하게 하기 위해 while 문 작성 
game_is_on = True
while game_is_on:
    screen.update()    # 세그먼트(뱀)가 모두 만들어지면 화면 갱신
    time.sleep(0.1)      # 0.1초 지연
    # Snake 움직임을 위해 move 메소드 사용 
    snake.move()
    
    # snake food와 충돌 감지 (이벤트 생성)
    if snake.head.distance(food) < 15:     # snake의 머리가 15 픽셀 이내 혹은 그보다 더 가까운 거리에 있다면
        food.refresh()                     # food의 refresh 메소드 불러오기 

# 창 닫힘 설정 
screen.exitonclick()   # 커서를 누르면 종료 설정