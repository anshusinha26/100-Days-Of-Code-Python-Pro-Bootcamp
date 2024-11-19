import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = 1  # Ball movement in x direction
ball.dy = 1  # Ball movement in y direction

# Bricks
bricks = []
colors = ["blue", "green", "orange", "yellow"]

for y in range(250, 150, -30):  # Rows of bricks
    for x in range(-250, 251, 50):  # Columns of bricks
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(colors))
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# Paddle movement functions
def paddle_left():
    x = paddle.xcor()
    x -= 30
    if x < -250:
        x = -250
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 30
    if x > 250:
        x = 250
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collisions
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bottom collision - game over
    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dy *= -1

    # Paddle collision
    if (ball.dy < 0) and (ball.ycor() > -240 and ball.ycor() < -230) and \
       (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Brick collisions
    for brick in bricks:
        if ball.distance(brick) < 25:
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move brick off-screen
            bricks.remove(brick)  # Remove brick from list
            break  # Only break one brick per collision

    # Check for game win
    if not bricks:
        ball.goto(0, 0)
        ball.write("You Win!", align="center", font=("Courier", 24, "normal"))
        break
