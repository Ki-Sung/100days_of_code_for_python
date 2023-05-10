# 무작위 행보 
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
    