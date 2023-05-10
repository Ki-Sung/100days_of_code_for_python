# 점섬 그리기 solution 1 
from turtle import Turtle, Screen
# 객체 선언 및 각종 설정
turtle = Turtle()       # 객체 선언 

for _ in range(15):
    turtle.forward(10)
    turtle.up()
    turtle.forward(5)
    turtle.down()

# 점섬 그리기 solution 2
# from turtle import Turtle
## 객체 선언 및 각종 설정
# turtle = Turtle()       # 객체 선언 

# for _ in range(15):
#     turtle.forward(10)   # 앞으로 10만큼 전진
#     turtle.penup()       # 펜을 위로 올리고(빈칸 생성)
#     turtle.forward(5)    # 앞으로 5번 (빈칸 기준 앞으로 5번 전진)
#     turtle.pendown()     # 펜을 아래로 내리고 (다시 선 그릴 준비)