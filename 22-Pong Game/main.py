"""imported Turtle and Screen class form the turtle module"""
from turtle import Turtle, Screen

"""imported time module"""
import time

"""imported Paddle class from the paddle module"""
from paddle import Paddle

"""imported Ball class from the ball module"""
from ball import Ball

"""imported Scoreboard class from the scoreboard module"""
from scoreboard import Scoreboard


"""paddle positions"""
RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

"""created screen object"""
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

"""created tim object to draw a center dashed line"""
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.color("white")
tim.setheading(90)
tim.goto(0, 275)
tim.setheading(270)
tim.pensize(10)
for i in range(14):
    tim.pendown()
    tim.forward(20)
    tim.penup()
    tim.forward(20)

"""created paddleRight object"""
paddleRight = Paddle(RIGHT_POS)

"""created paddleLeft object"""
paddleLeft = Paddle(LEFT_POS)

"""created ball object"""
ball = Ball()

"""created score object"""
score = Scoreboard()

"""paddleRight moves on pressing the up and down arrow keys"""
screen.onkey(paddleRight.up, "Up")
screen.onkey(paddleRight.down, "Down")

"""paddleLeft moves on pressing the w and s keys"""
screen.onkey(paddleLeft.up, "w")
screen.onkey(paddleLeft.down, "s")

"""variable to hold the game running condition"""
isGameOn = True

"""variable to hold the ball speed"""
speed = 0.1

"""until the game is on the loop runs"""
while isGameOn:
    """screen's animation and delay"""
    screen.update()
    time.sleep(speed)

    """ball's movement"""
    ball.move()

    """detecting collision with the walls"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    """detecting collision with the paddles"""
    if ball.distance(paddleRight) < 50 and ball.xcor() > 320 or ball.distance(paddleLeft) < 50 and ball.xcor() < -320:
        ball.bounceX()
        speed *= 0.9

    """detect if right paddle misses the ball"""
    if ball.xcor() > 400:
        ball.reset()
        score.leftPoint()
        speed = 0.1

    """detect if left paddle misses the ball"""
    if ball.xcor() < -400:
        ball.reset()
        score.rightPoint()
        speed = 0.1

"""screen will exit on click"""
screen.exitonclick()