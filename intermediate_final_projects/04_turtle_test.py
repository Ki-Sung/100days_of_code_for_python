## 01. 사용법
# from turtle import Turtle    # turtle 모듈에 Turtle 클래스 불러오기 
# from turtle import Screen    # turtle 모듈에 Screen 클래스 불러오기

# # 객체 생성 Turtle()  - 생성된 객체는 하나의 화면으로 켜짐 
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")   # turtle 모양 바꾸기 - 거북이 모양
# timmy_the_turtle.color("red")      # turtle 색성 바꾸기 - 빨강
# timmy_the_turtle.forward(100)      # turtle 앞으로 이동 - 이동속도 100
# timmy_the_turtle.right(90)         # 오늘쪽으로 바라보기 - 오른쪽 방향으로 90도로 회전


# # 객채 생성 Screen() - 창을 클릭하면 종료됨.
# screen = Screen()      # 객체생성
# screen.exitonclick()   # 창을 클릭하면 종료될 메소드 선언

# 02. 정사각형 그리기 
# from turtle import Turtle, Screen

# # 객체 선언 및 각종 설정
# turtle = Turtle()       # 객체 선언 
# turtle.shape("turtle")  # turtle 모양 변경
# turtle.color("red")     # turtle 색상 변경 

# # 정사각형을 그리기 위해 똑같은 동작 4번 반복 
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# 03. 점섬 그리기 solution 1
# from turtle import Turtle, Screen
# # 객체 선언 및 각종 설정
# turtle = Turtle()       # 객체 선언 

# for _ in range(15):
#     turtle.forward(10)
#     turtle.up()
#     turtle.forward(5)
#     turtle.down()

# 03. 점섬 그리기 solution 2
# from turtle import Turtle
## 객체 선언 및 각종 설정
# turtle = Turtle()       # 객체 선언 

# for _ in range(15):
#     turtle.forward(10)   # 앞으로 10만큼 전진
#     turtle.penup()       # 펜을 위로 올리고(빈칸 생성)
#     turtle.forward(5)    # 앞으로 5번 (빈칸 기준 앞으로 5번 전진)
#     turtle.pendown()     # 펜을 아래로 내리고 (다시 선 그릴 준비)

# 04. 한번에 삼각형, 사각형, 오각형, 육각형, 칠각형, 팔각형, 구각형, 십각형 만들기
from turtle import Turtle
import random

turtle = Turtle() # 객체 선언 

# 색상 list 담기 
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# 도형을 그리기 위한 기능 함수 
def drew_shape(num_sides):
    angle = 360 / num_sides     # 각 도형의 각도를 나누는 방정식 
    for _ in range(num_sides):
        turtle.forward(100)     # 앞으로 100 
        turtle.right(angle)     # 나눈 각도 대로 오른쪽으로 전환 

# 도형 그리기 
for shape_side_n in range(3, 11):   # 삼각형에서 십각형 까지 그리기 위해 범위를 3에서 10까지 설정
    turtle.color(random.choice(colors))    # 지정한 colors 리스트를 랜덤하게 뽑기 
    drew_shape(shape_side_n)            # 도형 그리기 