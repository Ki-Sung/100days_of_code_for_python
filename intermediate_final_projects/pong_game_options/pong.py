from turtle import Turtle

# pong 클래스 생성 
class Pong:
    def __init__(self):
        self.right_paddle()
    
    def right_paddle(self):
        right = Turtle(shape='square')
        right.color('white')
        right.penup()
        x_pos = 350
        y_pos = 0
        right.goto(x_pos, y_pos)