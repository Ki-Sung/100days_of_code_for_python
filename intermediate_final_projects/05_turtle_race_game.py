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
from turtle import Turtle, Screen

# 객체 선언 - Screen
screen = Screen()

# 표시되는 창의 폭과 넓이를 설정 
screen.setup(width=500, height=400)

# 팝업창 띄우기 
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)


# 객체 선언 - Turtle
turtle = Turtle(shape="turtle")

# 선을 없애기 위해 펜 올리기
turtle.penup()

# x, y 좌료대로 turtle(커서) 이동 
turtle.goto(x=-230, y=-100)

# 화면 클릭시 종료
screen.exitonclick()