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
# y 좌표 생성
y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
# 객체 선언 - Turtle - 커서 모양 거북이로 설정 
    turtle = Turtle(shape="turtle")
    # 선을 없애기 위해 펜 올리기
    turtle.penup()
    turtle.color(colors[turtle_index])   
    # x, y 좌표대로 turtle(커서) 이동    
    turtle.goto(x=-230, y=y_position[turtle_index])


# 화면 클릭시 종료
screen.exitonclick()