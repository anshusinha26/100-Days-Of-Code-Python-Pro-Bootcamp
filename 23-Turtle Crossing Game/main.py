"""imported Screen class from the turtle module"""
from turtle import Screen

"""imported time module"""
import time

"""imported Player class from the player module"""
from player import Player

"""imported Scoreboard class from the scoreboard module"""
from scoreboard import Scoreboard

"""imported Car class from the cars module"""
from cars import Car

"""created screen object"""
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

"""created player object"""
player = Player()

"""created score object"""
score = Scoreboard()

"""created car object"""
car = Car()

"""turtle moves forward on up key press"""
screen.onkey(player.move, "Up")

"""variable to hold the game's running condition"""
isGameOn = True

"""variable to increase the game's speed"""
speed = 0.5

"""until the game is on, the loop will run"""
while isGameOn:
    time.sleep(speed)
    screen.update()

    """car is created"""
    car.createCar()
    """car moves forward"""
    car.move()

    """detect if player has reached the end line"""
    if player.ycor() > 260:
        """player reaches the starting line"""
        player.startAgain()
        """level is increased"""
        score.updateScoreboard()
        """speed is increased"""
        speed *= 0.9

    """detect if player collides up with any of the car"""
    for i in car.allCars:
        if i.distance(player) < 20:
            score.gameOver()
            isGameOn = False


"""screen will exit on click"""
screen.exitonclick()
