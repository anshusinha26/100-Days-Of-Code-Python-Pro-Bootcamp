"""Turtle and Screen class is imported from the turtle module"""
import turtle
from turtle import Turtle, Screen

"""random module is imported"""
import random

##### ----- #####
"""tim object is created"""
tim = Turtle()
tim.shape("turtle")
tim.hideturtle()

"""screen object is created"""
screen = Screen()

"""a method which used to make the turtle screen listen to the keyboard and mouse events"""
screen.listen()

##### ----- #####

##### ----- #####

# """function to move forward by 10 paces"""
# def timMoveForward():
#     tim.forward(10)
#
# """triggers an event on a keypress"""
# screen.onkey(key="space", fun=timMoveForward)
# screen.exitonclick()

##### ----- #####

##### ----- #####

# """function to draw a sketch"""
#
# def timMakeSketch(x, y):
#     def moveForward():
#         tim.forward(10)
#
#     def moveBackward():
#         tim.backward(10)
#
#     def turnRight():
#         tim.right(5)
#
#     def turnLeft():
#         tim.left(5)
#
#     def clearScreen():
#         tim.clear()
#         tim.penup()
#         tim.home()
#
#     screen.onkey(key="w", fun=moveForward)
#     screen.onkey(key="s", fun=moveBackward)
#     screen.onkey(key="a", fun=turnLeft)
#     screen.onkey(key="d", fun=turnRight)
#     screen.onkey(key="c", fun=clearScreen)
#
#     screen.exitonclick()
#
# """function called on click"""
# screen.onscreenclick(timMakeSketch, 1)
# turtle.mainloop()

##### ----- #####

##### ----- #####

"""setting up the screen"""
screen.setup(width=600, height=500)
"""changing the screen name"""
turtle.title("Turtle race game")

"""taking an input from the user by making a prompt to the screen and storing it in a variable"""
userInput = screen.textinput(title="Make your bet to begin the race", prompt="Which turtle will win the race? Enter a color from the rainbow: ")

"""function to create finish line"""
def timCreateFinishLine():
    tim.pensize(10)
    tim.penup()
    tim.goto(x=220, y = 210)
    tim.right(90)
    tim.pendown()
    tim.forward(410)

timCreateFinishLine()

"""function to create starting lines"""
def timMakeStartingLines():
    """initial positions"""
    xPos = -210
    yPos = 200

    tim.penup()
    tim.goto(x=xPos, y=yPos)
    tim.pensize(1)
    tim.right(0)

    for i in range(7):
        tim.pendown()
        tim.forward(30)
        tim.penup()
        tim.forward(30)

timMakeStartingLines()

"""function to create tracks"""
def timCreateTracks():
    """initial positions"""
    xPos = -210
    yPos = 155

    tim.speed("fastest")
    tim.penup()
    tim.setheading(0)

    for i in range(6):
        tim.goto(x=xPos, y=yPos)
        yPos -= 60
        for j in range(21):
            tim.pendown()
            tim.forward(10)
            tim.penup()
            tim.forward(10)

timCreateTracks()

"""list of colors"""
colors = [
    "violet",
    "indigo",
    "blue",
    "green",
    "yellow",
    "orange",
    "red",
]

"""list of turtle names"""
turtles = [
    "Shelley",
    "Franklin",
    "Leonardo",
    "Myrtle",
    "Terrance",
    "Tilly",
    "Gamera",
]

"""list to store all created turtles"""
allTurtles = []

"""initial positions"""
xPos = -230
yPos = 245

"""initiating the positions of the turtle objects"""
for i in range(7):
    newTurtle = turtles[i]
    newTurtle = Turtle()
    newTurtle.penup()
    newTurtle.shape("turtle")
    newTurtle.color(colors[i])
    yPos -= 60
    newTurtle.goto(x=xPos, y=yPos)
    allTurtles.append(newTurtle)

"""initially race is not on"""
isRaceOn = False

"""if user makes a bet, the race is on"""
if userInput:
    isRaceOn = True

"""until race is on, the turtles will run"""
while isRaceOn:
    for turtle in allTurtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winningColor = turtle.pencolor()
            if winningColor == userInput:
                print(f"You've won! The {winningColor} turtle is the winner.")
                # screen.textinput(title=f"You've won! The {winningColor} turtle is the winner", prompt="_")
                tim.goto(0, 200)
                tim.write(f"You've won! The {winningColor} turtle is the winner.", align="center", font=("Arial", 20, "bold"))
            else:
                print(f"You've lost! The {winningColor} turtle is the winner.")
                # screen.textinput(title=f"You've lost! The {winningColor} turtle is the winner", prompt="_")
                tim.goto(0, 200)
                tim.write(f"You've lost! The {winningColor} turtle is the winner.", align="center", font=("Arial", 20, "bold"))

            """loop breaks as soon as a turtle touches the finish line"""
            break

        """variable to store random distance"""
        randomDistance = random.randint(0, 10)
        """each turtle will move forward with some random pace"""
        turtle.forward(randomDistance)

"""screen will exit on click"""
screen.exitonclick()

##### ----- #####






