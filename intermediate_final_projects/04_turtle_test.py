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

# # 04. 한번에 삼각형, 사각형, 오각형, 육각형, 칠각형, 팔각형, 구각형, 십각형 만들기
# from turtle import Turtle
# import random

# turtle = Turtle() # 객체 선언 

# # 색상 list 담기 
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# # 도형을 그리기 위한 기능 함수 
# def drew_shape(num_sides):
#     angle = 360 / num_sides     # 각 도형의 각도를 나누는 방정식 
#     for _ in range(num_sides):
#         turtle.forward(100)     # 앞으로 100 
#         turtle.right(angle)     # 나눈 각도 대로 오른쪽으로 전환 

# # 도형 그리기 
# for shape_side_n in range(3, 11):   # 삼각형에서 십각형 까지 그리기 위해 범위를 3에서 10까지 설정
#     turtle.color(random.choice(colors))    # 지정한 colors 리스트를 랜덤하게 뽑기 
#     drew_shape(shape_side_n)            # 도형 그리기 
    
# 05. 무작위 행보 
import random 
import turtle as t

# 객체 생성 
turtle = t.Turtle()
# RGB 값 0~255를 생성하기 위해 colormode 선언 
t.colormode(255)

# 랜덤 컬러 함수 설정 
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# 랜덤으로 색상을 구현하기 위한 색상 리스트 
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# 각종 설정 
turtle.pensize(15)   # 선 굵기 설정 
turtle.speed("normal")   # turtle 속도 설정
directions = [0, 90, 180, 270]  # 방향 설정 

# 무작위 행보 실행 
for _ in range(150):
    turtle.color(random_color())              # 색상 리스트 랜덤으로 호출
    turtle.setheading(random.choice(directions))    # turtle이 바라보는 방향(directions)을 각도 만큼 변경
    turtle.forward(30)      # 30만큼 앞으로 이동