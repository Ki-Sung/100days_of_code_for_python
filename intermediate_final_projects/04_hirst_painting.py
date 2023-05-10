# 데미안 허스트의 스팟 페인팅을 turtle로 만들어보자! 

# 0. colorgram.py 패키지 설치 - pip install colorgram.py

import colorgram
import turtle as t 
import random 

# colorgram - 이미지로부터 컬러 추출 
colors = colorgram.extract('./img/spot_image.jpg', 35)  # colorgram.extract(이미지파일 경로 및 파일, 추출할 컬러 수)  

# 1. rgb 값 추출 - list = [(r,g,b tuple)]
rgb_colors = []                         # 빈 리스트 선언 
for color in colors:                    # colors 객체 수 만큼 반복문 실행 
    r = color.rgb.r                     # rgb의 red 값 추출 
    g = color.rgb.g                     # rgb의 green 값 추출 
    b = color.rgb.b                     # rgb의 blue 값 추출 
    new_color = (r, g, b)               # 추출한 값 튜플로 저장
    rgb_colors.append(new_color)        # 저장된 튜플 r,g,b 값 리스트로 저장
    
# 2. spot painting 그리기 

# RGB 값 0~255를 생성하기 위해 colormode 선언 
t.colormode(255)
# 객체 선언 
turtle = t.Turtle()
turtle.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dot = 100


for dot_count in range(1, number_of_dot + 1):
    t.dot(20, random.choice(rgb_colors))
    t.forward(50)
    
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



# turtle 화면 내 클릭시 종료 설정 
screen = t.Screen()
screen.exitonclick()