from turtle import Turtle

FONT = ("Courier", 15, "normal")
G_OVER_FONT = ("Courier", 26, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.write_score()

    def write_score(self):
        self.goto(-240, 260)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.current_level += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=G_OVER_FONT)
