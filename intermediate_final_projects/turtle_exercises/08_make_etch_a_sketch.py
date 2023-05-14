# Etch-a-Sketch
# "W"를 누르면 앞으로 이동(forwards), "S"를 누르면 뒤로 이동(backwards)
# "A"를 누르면 시계반대방향으로 회전(counter-clockwise), D"를 누르면 시계방향인 오른쪽으로 회전(clockwise)
# "C"를 누르면 그림 모두 삭제 (Clear Drawing) 및 turtle(커서)가 중앙으로 다시 와야함.

# 모듈 불러오기 
from turtle import Turtle, Screen

# 객체 선언 
turtle = Turtle()
screen = Screen()

# listen 선언
screen.listen()

# 앞으로 가기 - 10씩 이동 
def move_forwards():
    turtle.forward(10)
    
# 뒤로 가기 - 10씩 이동
def move_backwards():
    turtle.backward(10)

# 왼쪽 회전 - 10씩 기울기
def turn_left():
    new_heading = turtle.heading() + 10    # or turtle.left(10)    
    turtle.setheading(new_heading)

# 오른쪽 회전 - 10씩 기울기 
def turn_right():
    new_heading = turtle.heading() - 10    # or turtle.right(10) 
    turtle.setheading(new_heading)
    
# 화면 clear 
def clear():
    turtle.clear()      # 화면에 모든 그림 없애기 
    turtle.penup()      # 펜 올리기 (선을 안 긋기 위함)
    turtle.home()       # 화살표(turtle)중앙에 배치 
    turtle.pendown()    # 펜 내리기 (선을 그리기 위한)
    
# 키보드 이벤트 바인딩 
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

# 화면 클릭시 종료
screen.exitonclick()