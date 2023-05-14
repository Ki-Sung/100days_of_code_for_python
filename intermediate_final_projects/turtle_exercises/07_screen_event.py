# 기본 사용법

# 모듈 불러오기 
from turtle import Turtle, Screen

# 객체 생성 
turtle = Turtle()
screen = Screen()

# 앞으로 10씩 전진하는 함수 선언 
def move_forwards():
    turtle.forward(10)

# listen 선언
screen.listen()

# 키보드 이벤트 바인딩 
screen.onkey(key="space", fun=move_forwards)    # 스페이스를 누르면, 10만큼 전진!
screen.exitonclick()                            # 스크린 클릭시 종료 