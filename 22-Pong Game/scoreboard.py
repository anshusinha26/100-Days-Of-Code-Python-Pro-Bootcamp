"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""write style"""
ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")

"""created Scoreboard class"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.rightScore = 0
        self.leftScore = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(100, 220)
        self.write(self.rightScore, align=ALIGNMENT, font=FONT)
        self.goto(-100, 220)
        self.write(self.leftScore, align=ALIGNMENT, font=FONT)

    def rightPoint(self):
        self.rightScore += 1
        self.updateScoreboard()

    def leftPoint(self):
        self.leftScore += 1
        self.updateScoreboard()
