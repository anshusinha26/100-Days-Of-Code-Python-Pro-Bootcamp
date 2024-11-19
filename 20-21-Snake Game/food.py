"""Turtle class is imported from the turtle module"""
from turtle import Turtle

"""random module is imported"""
import random

"""Food class is created which inherits Turtle class"""
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.moveFood()

    def moveFood(self):
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)
        self.goto(randomX, randomY)
