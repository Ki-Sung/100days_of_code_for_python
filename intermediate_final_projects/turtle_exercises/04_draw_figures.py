# 한번에 삼각형, 사각형, 오각형, 육각형, 칠각형, 팔각형, 구각형, 십각형 만들기
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