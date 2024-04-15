import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("purple")
screen.setup(width=830, height=600)
screen.tracer(0)

# Create paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")

ball.penup()
ball.goto(0, 0)

ball.dx = 2  # Increase the ball's speed in the x dimension
ball.dy = 2  # Increase the ball's speed in the y dimension

# Create scoreboard

score_a = turtle.Turtle()
score_a.speed(0)
score_a.color("white")
score_a.penup()
score_a.goto(-370, 260)
score_a.write("A: 0", align="center", font=("Courier", 24, "normal"))
score_b = turtle.Turtle()
score_b.speed(0)
score_b.color("white")
score_b.penup()
score_b.goto(370, 260)
score_b.write("B: 0", align="center", font=("Courier", 24, "normal"))

# Set up keyboard controls
screen.listen()
screen.onkeypress(lambda: paddle_a.sety(paddle_a.ycor() + 30), "w") #Move the player A top
screen.onkeypress(lambda: paddle_a.sety(paddle_a.ycor() - 30), "s")  # Move the player A bottom
screen.onkeypress(lambda: paddle_b.sety(paddle_b.ycor() + 30), "Up") #Move the player B top
screen.onkeypress(lambda: paddle_b.sety(paddle_b.ycor() - 30), "Down")   # Move the player B bottom

# Main game loop
score_a_value = 0
score_b_value = 0

while True:
    # Update the screen
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check if the ball hits the top or bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.dy *= -1

    # Check if any of the paddles hit the ball
    if (ball.dx > 0 and (ball.xcor() > 320 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40))):
        ball.dx *= -1
        ball.color("blue")
    elif (ball.dx < 0 and (ball.xcor() < -320 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40))):
        ball.dx *= -1
        ball.color("red")

    # Check if the ball goes past a paddle
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a_value += 1
        score_a.clear()
        score_a.write("A: {}".format(score_a_value), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b_value += 1
        score_b.clear()
        score_b.write("B: {}".format(score_b_value), align="center", font=("Courier", 24, "normal"))

    # Check if the ball goes past the paddle
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
