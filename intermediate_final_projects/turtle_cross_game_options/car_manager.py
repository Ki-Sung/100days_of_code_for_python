# 모둘 선언 
import random
from turtle import Turtle

# 상수 설정 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]    # 자동차 색상 설정 
STARTING_MOVE_DISTANCE = 5       # 자동차 움직임의 수 
MOVE_INCREMENT = 10              # 자동차 움직임 증가 수

# 자동차(장애물) 설정을 위한 CarManager 클래스 선언 
class CarManager:
    # 초기 설정 
    def __init__(self):
        self.all_cars = []                          # 자동차(장애물) 정보를 담을 빈 리스트 생성 
        self.car_speed = STARTING_MOVE_DISTANCE     # 자동차(장애물) 속도를 올리기 위해 움직임수 설정 
    
    # 자동차(장애물)생성을 위한 메소드 
    def create_car(self):
        random_chance = random.randint(1, 6)                    # 1과 6사이 랜덤하게 숫자 생성 (6번에 1번확률을 갖게하는) -> 새로고침이 0.1초마다 될 때, 차 생성시 속도를 낮추기 위해 설정 
        if random_chance == 1:                                  # 만약 random_chance가 1과 같을 경우, 자동차(장애물) 생성
            new_car = Turtle('square')                          # 자동차(장애물)모양 설정 
            new_car.shapesize(stretch_wid=1, stretch_len=2)     # 자동차(장애물) 사이즈 (40X20)
            new_car.penup()                                     # 자동차(장애물) 선그리기 없애기 설정 
            new_car.color(random.choice(COLORS))                # 자동차(장애물) 색상 설정 (지정된 상수로 랜덤하게 생성)
            random_y = random.randint(-250, 250)                # 자동차(장애물)이 생성되는 범위 설정 
            new_car.goto(300, random_y)                         # 자동차(장애물) 생성 
            self.all_cars.append(new_car)                       # 생성된 자동차(장애물)정보 초기 설정 메소드 빈 리스트에 저장
        
    # 자동차(장애물)을 움직이게 하기 위한 메소드
    def move_cars(self):
        for car in self.all_cars:                               # 저장된 자동차(장애물) 정보들을 반복문으로 사용 
            car.backward(self.car_speed)                        # 해당 자동차(장애물)를 거리수 5만큼 움직이게 설정
            
    # Turtle이 결승점에 통과후 레벨 즉 자동차(장애물) 속도를 올리기 위한 설정 메소드 
    def level_up(self):
        self.car_speed += MOVE_INCREMENT       # 자동차(장애물) 속도 10씩 증가