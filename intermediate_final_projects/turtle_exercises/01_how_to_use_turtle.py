# turtle basic 사용법
from turtle import Turtle    # turtle 모듈에 Turtle 클래스 불러오기 
from turtle import Screen    # turtle 모듈에 Screen 클래스 불러오기

# 객체 생성 Turtle()  - 생성된 객체는 하나의 화면으로 켜짐 
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")   # turtle 모양 바꾸기 - 거북이 모양
timmy_the_turtle.color("red")      # turtle 색성 바꾸기 - 빨강
timmy_the_turtle.forward(100)      # turtle 앞으로 이동 - 이동속도 100
timmy_the_turtle.right(90)         # 오늘쪽으로 바라보기 - 오른쪽 방향으로 90도로 회전


# 객채 생성 Screen() - 창을 클릭하면 종료됨.
screen = Screen()      # 객체생성
screen.exitonclick()   # 창을 클릭하면 종료될 메소드 선언