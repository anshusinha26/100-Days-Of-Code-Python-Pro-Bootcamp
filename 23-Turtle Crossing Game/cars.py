"""imported Turtle class from turtle module"""
import turtle
from turtle import Turtle

"""imported random module"""
import random

"""car's forward distance"""
CAR_FORWARD_DISTANCE = 20

"""car positions"""
CAR_POSITIONS = []
for i in range(240, -240, -30):
    CAR_POSITIONS.append((320, i))

"""set the color mode to 255 (rgb value)"""
turtle.colormode(255)

"""created Car class"""
class Car:

    def __init__(self):
        self.allCars = []

    def generateColor(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

    def createCar(self):
        randomChance = random.randint(1, 6)
        if randomChance == 1:
            newCar = Turtle()
            newCar.penup()
            newCar.shape("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.setheading(180)
            newCar.color(self.generateColor())
            newCar.goto(random.choice(CAR_POSITIONS))
            self.allCars.append(newCar)

    def move(self):
        for car in self.allCars:
            car.forward(CAR_FORWARD_DISTANCE)