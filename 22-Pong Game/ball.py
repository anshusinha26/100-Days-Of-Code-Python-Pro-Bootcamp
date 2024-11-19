"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""created Ball class"""
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xpos = 10
        self.ypos = 10

    def move(self):
        self.newX = self.xcor() + self.xpos
        self.newY = self.ycor() + self.ypos
        self.goto(self.newX, self.newY)

    def bounceX(self):
        self.xpos *= -1

    def bounceY(self):
        self.ypos *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounceX()
