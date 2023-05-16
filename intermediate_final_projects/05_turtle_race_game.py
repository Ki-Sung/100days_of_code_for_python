## Turtle Race Game 
## 목표 
# 1. 어느 터틀이 우승에 내기를 걸 것인지 묻는 작은 팝업창 생성
# 2. 해당 팝업창에 색상 입력 (터틀들의 색상은 6개의 무지개색으로 되어있음)
# 3. 입력 완료 후 모든 터틀들이 출발 위치인 왼쪽 가장자리에 나란히 정렬
# 4. 오른쪽 가장자리를 향해 출발(이때 각각 임의의 거리만큼 앞으로 나아감)
# 5. 오른쪽 가장자리에 먼저 도착한 터틀 우승
# 6. 터미널에 우리가 내기가 이겼는지 졌는지, 어떤 색상의 터틀이 우승했는지 출력

## 1. Build a turtle race 

# 모듈 불러오기 
import random
from turtle import Turtle, Screen

# 객체 선언 - Screen
screen = Screen()

# 표시되는 창의 폭과 넓이를 설정 
screen.setup(width=500, height=400)

# 팝업창 띄우기 
# 파리미터 - title(팝업 제목), prompt(팝업창에 기재된 질문)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# 컬러 리스트 생성  
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# y 좌표 리스트 생성 - 각 turtle의 출발점 지정을 위한
y_position = [-70, -40, -10, 20, 50, 80]

# 빈 리스트 선언 
all_turtles = []

# 지정한 y 좌표 기준으로 6개의 turtle 출발선에 서게하기 
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")            # 객체 선언 - Turtle - 커서 모양 거북이로 설정 
    new_turtle.penup()                             # 선을 없애기 위해 펜 올리기
    new_turtle.color(colors[turtle_index])         # y 좌표리스트 순서 기준으로 turtle 컬러 생성 
    new_turtle.goto(x=-230, y=y_position[turtle_index])    #  x, y 좌표대로 turtle(커서) 이동  
    all_turtles.append(new_turtle)                 # 각각의 turtle 객체들을 빈 리스트에 담기 

# 2. start race!

# turtle 레이스를 위한 준비 
is_race_on = False

# 만약 입력창에 생상을 입력했을 경우 "is_race_on"이 True로 전환 - True로 전환되면 반복문 사용할 수 있음
if user_bet:
    is_race_on = True 

# 반복문 동작 
while is_race_on:
    # turtle 리스트의 원소들(all_turtle)을 순회하면서 반복 
    for turtle in all_turtles:
        if turtle.xcor() > 230:                  # 만약 turtled의 좌표가 230 보다 크다면 
            is_race_on = False                   # 레이스 종료 (while문 빠져나오기)
            winning_color = turtle.pencolor()    # 종료되면서 가장 먼저 도착한 turtle의 색상 저장 
            if winning_color == user_bet:        # 만약 "winning_color"와 사용자가 입력한 "user_bet"과 결과가 일치한다면
                print(f"you've won! The {winning_color} turtle is the winner")      # 이겼다고 출력 
            else:                                                                   # 그 외 결과는 
                print(f"you've lost! The {winning_color} turtle is the winner")     # 졌다고 출력 
            
        random_distance = random.randint(0, 10)      # random 모듈을 사용해서 0에서 10까지의 범위에서 임의 정수를 지정
        turtle.forward(random_distance)              # 지정단 랜덤 정수들을 바탕으로 나온 숫자 만큼 앞으로 가기 

# 화면 클릭시 종료
screen.exitonclick()