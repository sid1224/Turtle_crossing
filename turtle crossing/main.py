import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_turtle, "Up")

game_is_on = True
game_loop_counter = 0
while game_is_on:
    game_loop_counter += 1
    time.sleep(0.1)
    screen.update()

    if player.ycor() >= 280:
        player.goto(0, -280)
        car_manager.level_up()
        score.increase_level()


    car_manager.car_generator()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()