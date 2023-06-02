import time
from turtle import Screen
from turtle_cross_game_options.player import Player
from turtle_cross_game_options.car_manager import CarManager
from turtle_cross_game_options.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
