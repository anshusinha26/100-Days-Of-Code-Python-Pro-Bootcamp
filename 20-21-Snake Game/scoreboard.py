"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""Constants"""
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

"""Scoreboard class is created"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.updateScoreBoard()


    def updateScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.updateScoreBoard()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()






