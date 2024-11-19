"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""paddle moving distance"""
PADDLE_DISTANCE = 40

"""created Paddle class"""
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.newYPositive = self.ycor() + PADDLE_DISTANCE
        if self.newYPositive < 250:
            self.goto(self.xcor(), self.newYPositive)

    def down(self):
        self.newYNegative = self.ycor() - PADDLE_DISTANCE
        if self.newYNegative > -250:
            self.goto(self.xcor(), self.newYNegative)
