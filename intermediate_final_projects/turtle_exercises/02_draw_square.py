# 정사각형 그리기 
from turtle import Turtle, Screen

# 객체 선언 및 각종 설정
turtle = Turtle()       # 객체 선언 
turtle.shape("turtle")  # turtle 모양 변경
turtle.color("red")     # turtle 색상 변경 

# 정사각형을 그리기 위해 똑같은 동작 4번 반복 
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)