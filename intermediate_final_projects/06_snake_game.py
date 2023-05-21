# 정리는 intermediate 폴더 쥬피터 노트북 파일 day20, day21에 정리 

# 모듈 불러오기 
import time
from turtle import Screen, Turtle 

# Screen 설정 
screen = Screen()  # 객체 선언 
screen.setup(width=600,height=600)  # screen 크기 설정 (600 X 600)
screen.bgcolor("black")   # screen 백그라운컬러 설정 (블랙)
screen.title("Play Snake Game")  # 타이틀 설정 
screen.tracer(0)       # turtle의 애니메이션을 켜거나 끄기 위한 옵션 (여기서는 끄기) - 뱀 전체가 하나처럼 보이게하기 위함.



# 1. Snake 몸통 만들기 
starting_position = [(0, 0), (-20, 0), (-40 , 0)]


segments = []        # 세그먼트 설정을 위해 빈 리스트 선언 

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# 동작을 계속하게 하기 위해 while 문 작성 
game_is_on = True
while game_is_on:
    screen.update()    # 세그먼트(뱀)가 모두 만들어지면 화면 갱신
    time.sleep(0.1)      # 0.1초 지연

    # 뱀의 방향 전환을 위한 컨트롤 
    # 마지막(세 번째) 세그먼트(뱀)를 두 번째 세그먼트 자리로 옮기고, 
    # 두 번째의 것을 첫 번째 자리로 옮긴 다음 
    # 첫 번째 세그먼트를 앞으로 20 픽셀을 옮김 
    for seg_num in range(len(segments) -1, 0, -1):    # 범위 2 부터 0까지 역순으로 -1씩 차감 
        new_x = segments[seg_num - 1].xcor()          # 역순으로 seg_num의 x축 값 추출 
        new_y = segments[seg_num - 1].ycor()          # 역순으로 seg_num의 y축 값 추출 
        segments[seg_num].goto(new_x, new_y)          # 추출한 x, y 좌표 기준으로 위치 설정
    segments[0].forward(20)                           # 제일 앞에 있는 세그먼트 기준으로 20씩 앞으로 움직이기
    segments[0].left(90)


# 창 닫힘 설정 
screen.exitonclick()   # 커서를 누르면 종료 설정