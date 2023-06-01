from turtle import Turtle

# Ball 클래스 생성 
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')       # ball 색상 설정 
        self.shape('circle')      # ball 모양 설정 
        self.penup()              # 선 없애기 
        self.x_move = 10          # ball x 좌표 
        self.y_move = 10          # ball y 좌표 
        self.move_speed = 0.1     # ball speed 설정 
        
    def move(self):
        new_x = self.xcor() + self.x_move  # ball x 좌표설정 
        new_y = self.ycor() + self.y_move  # ball y 좌표설정 
        self.goto(new_x, new_y)            # 설정한 x, y 좌표로 이동 
    
    # 위, 아래 벽과 충돌 감지 설정 메소드     
    def bounce_y(self):
        # 공이 툉겨나갈 때 원래 방향에서 반대 방향으로 바뀌어야 한다.
        # 원래 +10이 었으면 반대인 -10으로 바꿔주고, 원래 -10이 었으면 +10으로 바꿔준다
        # 그래서 아래와 같이 -1을 곱해준다.
        self.y_move *= -1
    
    # paddle과 충돌 감지 설정 메소드    
    def bounce_x(self):
        # 공이 툉겨나갈 때 원래 방향에서 반대 방향으로 바뀌어야 한다.
        # 원래 +10이 었으면 반대인 -10으로 바꿔주고, 원래 -10이 었으면 +10으로 바꿔준다
        # 그래서 아래와 같이 -1을 곱해준다.
        self.x_move *= -1
        self.move_speed *= 0.9           # 패들에 공이 튕길 때 마다 속도가 올라가는 설정 
    
    # 공을 놓쳤을 경우 공의 위치를 다시 reset 시키는 설정의 메소드     
    def reset_postion(self):
        self.goto(0, 0)          # 공을 가운데 위치로 이동
        self.move_speed = 0.1    # 공을 놓쳤을때 공 속도 초기회 
        self.bounce_x()          # 놓친 패들의 방향에 따라 위치가 반대가 되야히기에 위의 bounce_x 메소드를 부름