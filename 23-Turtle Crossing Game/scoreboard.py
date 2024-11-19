"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""font constants"""
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

"""created Scoreboard class"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.level = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)


