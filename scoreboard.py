from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()

    def score_card(self):
        self.goto(-20, 265)
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        with open("data.txt", mode="w") as datas:
            datas.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.score_card()

    def count(self):
        self.score += 1
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
