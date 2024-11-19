"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""starting positions"""
STARTINGPOSITIONS = [(0, 0), (-20, 0), (-40, 0)]

"""snake directions"""
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"""forward distance"""
DISTANCE = 10

"""created the Snake class"""
class Snake:

    def __init__(self):
        self.bodies = []
        self.createSnake()
        self.head = self.bodies[0]

    def createSnake(self):
        for position in STARTINGPOSITIONS:
           self.addBodies(position)

    def addBodies(self, position):
        newBody = Turtle()
        newBody.shape("square")
        newBody.color("black")
        newBody.penup()
        newBody.goto(position)
        self.bodies.append(newBody)

    def extendBody(self):
        self.addBodies(self.bodies[-1].position())

    def moveSnake(self):
        for body in range(len(self.bodies) - 1, 0, -1):
            newX = self.bodies[body - 1].xcor()
            newY = self.bodies[body - 1].ycor()
            self.bodies[body].goto(newX, newY)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for body in self.bodies:
            body.goto(1000, 1000)
        self.bodies.clear()
        self.createSnake()
        self.head = self.bodies[0]
