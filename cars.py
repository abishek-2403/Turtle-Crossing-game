from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.current_speed = 0
        self.current_speed = self.current_speed + STARTING_MOVE_DISTANCE

    def move_cars(self):

        for car in self.cars:
            car.forward(self.current_speed)

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            random_y = random.randint(-260, 280)
            car.goto(300, random_y)
            self.cars.append(car)

    def increase_speed(self):
        self.current_speed = self.current_speed + MOVE_INCREMENT
