from turtle import Turtle 

# 상수 선언 - 시작할 때 Snake 위치, 이동할 거리 설정
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40 , 0)]
MOVE_DISTANCE = 20

# Snake 클래스 생성 
class Snake:
    # 새로운 snake 객체를 초기화할 때 무엇을 할지 결정함
    def __init__(self):
        self.segments = []        # 새로운 속성인 segments를 설정 
        self.create_snake()       # create_snake라는 메소드 지정
    
    # 위에 init 함수에 지정한 create_snake() 메소드 생성 
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    # snake의 움직임 설정인 move 메소드 생성     
    def move(self):
        # 뱀의 방향 전환을 위한 컨트롤 
        # 마지막(세 번째) 세그먼트(뱀)를 두 번째 세그먼트 자리로 옮기고, 
        # 두 번째의 것을 첫 번째 자리로 옮긴 다음 
        # 첫 번째 세그먼트를 앞으로 20 픽셀을 옮김 
        for seg_num in range(len(self.segments) -1, 0, -1):    # 범위 2 부터 0까지 역순으로 -1씩 차감 
            new_x = self.segments[seg_num - 1].xcor()          # 역순으로 seg_num의 x축 값 추출 
            new_y = self.segments[seg_num - 1].ycor()          # 역순으로 seg_num의 y축 값 추출 
            self.segments[seg_num].goto(new_x, new_y)          # 추출한 x, y 좌표 기준으로 위치 설정
        self.segments[0].forward(MOVE_DISTANCE)                # 제일 앞에 있는 세그먼트 기준으로 20씩 앞으로 움직이기