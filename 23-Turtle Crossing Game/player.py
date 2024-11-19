"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""player's forward distance"""
PLAYER_FORWARD_DISTANCE = 20

"""created player class"""
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.startAgain()
        self.setheading(90)

    def startAgain(self):
        self.goto(0, -260)

    def move(self):
        self.forward(PLAYER_FORWARD_DISTANCE)
