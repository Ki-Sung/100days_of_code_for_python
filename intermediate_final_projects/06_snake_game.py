# 정리는 intermediate 폴더 쥬피터 노트북 파일 day20, day21에 정리 

# 모듈 불러오기 
from turtle import Screen, Turtle 

# Screen 설정 
screen = Screen()  # 객체 선언 
screen.setup(width=600,height=600)  # screen 크기 설정 (600 X 600)
screen.bgcolor("black")   # screen 백그라운컬러 설정 (블랙)
screen.title("Play Snake Game")  # 타이틀 설정 

# 1. Snake 몸통 만들기 
starting_position = [(0, 0), (-20, 0), (-40 , 0)]

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)




# 창 닫힘 설정 
screen.exitonclick()   # 커서를 누르면 종료 설정