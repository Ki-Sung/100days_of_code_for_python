# 정리는 intermediate 폴더 쥬피터 노트북 파일 day22에 정리 

# 모듈 불러오기 
from turtle import Turtle, Screen

# Screen 설정
screen = Screen()     # 객체선언 
screen.setup(width=800, height=600)    # Screen 크기 설정 (800X600)
screen.bgcolor('black')                # Screen 백그라운드 설정 (블랙)
screen.title('Pong')                   # 게임 타이틀 설정 



# 창 닫힘 설정
screen.exitonclick()                    # 커서를 누르면 종료
