# 스피로그래프 그리기 
import random 
import turtle as t

# 객체 선언 
turtle = t.Turtle()
# RGB 값 0~255를 생성하기 위해 colormode 선언 
t.colormode(255)

# turtle 속도 설정
turtle.speed("fastest") 

# 랜덤 컬러 함수 설정 
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# 스피로 그래프 동작 

# solution 1
# for _ in range(36):
#     turtle.color(random_color())
#     turtle.circle(100)
#     turtle.left(10)

# solution 2
# for _ in range(100):
#     # 그림 좌표 위치를 보기위한 출력 
#     # print(turtle.heading())
#     turtle.color(random_color())         
#     turtle.circle(100)                   
#     current_heading = turtle.heading()       # 현재 좌표 
#     turtle.setheading(current_heading + 10)  # 현재 좌표 + 10 (0.0 + 10)

# solution 3 
# 스피로그래프 그리기 함수 설정 
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):    # 원하는 각도 만큼 반복 range()안에는 정수만 인식하므로 int()로 지정 -> 360도 / 간격 = 원하는 각도
        turtle.color(random_color())         
        turtle.circle(100)                   
        current_heading = turtle.heading()       # 현재 좌표 
        turtle.setheading(current_heading + size_of_gap)  # 현재 좌표 + 10 (0.0 + 10)

# 스피로 그래프 동작 
draw_spirograph(5)

    
# turtle 화면 내 클릭시 종료 설정 
screen = t.Screen()
screen.exitonclick()