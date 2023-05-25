from turtle import Turtle 

# 상수 선언 
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40 , 0)]     #  시작할 때 Snake 위치
MOVE_DISTANCE = 20                               # 이동할 거리 설정
UP = 90           # 위 방향 
DOWN = 270        # 아래 방향 
LEFT = 180        # 왼쪽 방향 
RIGHT = 0         # 오른쪽 방향 

# Snake 클래스 생성 
class Snake:
    # 새로운 snake 객체를 초기화할 때 무엇을 할지 결정함
    def __init__(self):
        self.segments = []             # 새로운 속성인 segments를 설정 
        self.create_snake()            # create_snake라는 메소드 지정
        self.head = self.segments[0]   # snake 머리 속성 지정  
    
    # 위에 init 함수에 지정한 create_snake() 메소드 생성 
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)     # 아라에 있는 add_segment 메소드 불러오기
    
    # 뱀의 길이가 늘어나기 위한 tutle 설정이 들어간 add_segment() 메소드 
    def add_segment(self, position):
        new_segment = Turtle(shape="square")      # turtle 모양 설정 
        new_segment.color("white")                # tuttle 색상 설정 
        new_segment.penup()                       # 선을 없애기 위해 penup 설정 
        new_segment.goto(position)                # position(위치)로 가기 
        self.segments.append(new_segment)         
    
    # 먹이를 먹을 때 뱀의 길이가 늘어나는 extend 메소드 생성
    def extend(self):
        # 새로운 snake(segment) 추가
        self.add_segment(self.segments[-1].position())    # segment 마지막에 추가 
        
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
        self.head.forward(MOVE_DISTANCE)                       # 제일 앞에 있는 세그먼트 기준으로 20씩 앞으로 움직이기
        
    # snake 움직임 컨트롤 중 방향키 위를 누르면 snake가 위로 가는 설정
    def up(self):
        if self.head.heading() != DOWN:                 # 만약 현재 머리의 방향이 아래쪽이 아닌 경우 => 현재 방향이 아래쪽이면 위로 갈수 없음
            self.head.setheading(UP)                    # 뱀 머리 기준 90도로 설정
    
    # snake 움직임 컨트롤 중 방향키 아래를 누르면 snake가 아래로 가는 설정
    def down(self):
        if self.head.heading() != UP:                   # 만약 현재 머리의 방향이 위쪽이 아닌 경우 => 현재 방향이 위쪽이면 아래로 갈수 없음
            self.head.setheading(DOWN)                  # 뱀 머리 기준 270도로 설정
    
    # snake 움직임 컨트롤 중 방향키 왼쪽을 누르면 snake가 왼쪽으로 가는 설정
    def left(self):
        if self.head.heading() != RIGHT:                # 만약 현재 머리의 방향이 오른쪽이 아닌 경우 => 현재 방향이 오른쪽이면 왼쪽으로 갈수 없음
            self.head.setheading(LEFT)                  # 뱀 머리 기준 180도로 설정
    
    # snake 움직임 컨트롤 중 방향키 오른쪽을 누르면 snake가 오른쪽으로 가는 설정
    def right(self):
        if self.head.heading() != LEFT:                 # 만약 현재 머리의 방향이 왼쪽이 아닌 경우 => 현재 방향이 왼쪽이면 오른쪽으로 갈수 없음
            self.head.setheading(RIGHT)                 # 뱀 머리 기준 0도로 설정