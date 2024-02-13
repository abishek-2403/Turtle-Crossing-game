from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from cars import Cars
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(fun=turtle.move, key="Up")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move_cars()

    for i in car.cars:
        if turtle.distance(i) < 20:
            score.game_over()
            is_game_on = False
    if turtle.ycor() > 280:
        turtle.player_restart()
        car.increase_speed()
        score.increase_level()

screen.exitonclick()
