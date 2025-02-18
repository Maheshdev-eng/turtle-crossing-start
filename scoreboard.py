from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_scoreboard()


    def update_scoreboard(self):

        self.clear()
        self.write(f"level={self.score}", font=FONT)



    def incrrease_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"game over",align="center",font=FONT)