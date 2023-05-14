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

#turtle 모듈의 색상 모드를 255로 변경 
t.colormode(255)

# 객체 선언 
turtle = t.Turtle()

# 기본 옵션
turtle.speed("fastest")                 # turtle 속도 지정 - 가장 빠르게 
t.penup()                               # 점과 점사이 선 제거 (펜을 들어올려 선을 그리지 않도록 할 수 있는 설정 )
t.hideturtle()                          # turtle(즉 커서) 숨기기 - 모든 spot painting이 끝나면 마지막 화살표 숨기기 위한 설정

# 시작점 설정 
t.setheading(225)                       # 방향 설정 (a 방향으로 회전함.) 여기서 시작점은 270에서 180 사이의 값인 225로 지정
t.forward(300)                          # 방향설정 후 300걸음 앞으로 이동
t.setheading(0)                         # 시작점 위치에 오른쪽 방향으로 진행
number_of_dot = 100                     # 우리가 그리고자 하는 점의 개수 지정 - 100개 

# spot painting 그리기
for dot_count in range(1, number_of_dot + 1):
    # 시작점을 기점으로 점 그리기 
    t.dot(20, random.choice(rgb_colors))    # 위에서 구한 rgb 값을 랜덤하게 사용하여 색상을 다양하게 지정, dot 메소드를 사용하여 점 찍기 
    t.forward(50)                           # 앞으로 50씩 전진
    
    # 다음 위로 점을 그리기 위한 동작 
    if dot_count % 10 == 0:
        t.setheading(90)                    # 방향 설정, 여기서 다음 줄로 가기 위해 위쪽 방향으로 돌림 (90도))
        t.forward(50)                       # 앞으로 50걸음 이동 
        t.setheading(180)                   # 다시 왼쪽으로 회전 (180도)
        t.forward(500)                      # 그리고 앞으로 500걸음씩 이동 (다음 시작점까지 이동)
        t.setheading(0)                     # 다음 시작점에서 다시 오른쪽으로 방향을 향하도록 함. (0도)



# turtle 화면 내 클릭시 종료 설정 
screen = t.Screen()
screen.exitonclick()