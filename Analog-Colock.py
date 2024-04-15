import turtle
import time

wn = turtle.Screen()
wn.bgcolor("purple")
wn.setup(width=600, height=600)
wn.title("Analog Clock | CodeZone")
wn.tracer(0)


# Create Our Drawing Pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()


# ============= Drawing The Clock ==============
def draw_clock(h, m, s):
    global pen

    # Draw The Outer Circle
    pen.penup()
    pen.pensize(15)
    pen.setposition(0, 210)
    pen.setheading(180)  # Control the direction of the Turtle (CCW)
    pen.color("#142164", "#F6F6F6")
    pen.pendown()
    pen.begin_fill()
    pen.circle(210)
    pen.end_fill()

    # Draw Lines for Hours
    pen.penup()
    pen.setposition(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.forward(210)
        pen.pendown()
        pen.backward(20)
        pen.penup()
        pen.setposition(0, 0)
        pen.right(360 / 12)

    # Draw Hour hand
    pen.color("#D92531")
    pen.pensize(12)
    pen.penup()
    pen.setposition(0, 0)
    # h = 9
    angle = (h / 12) * 360
    pen.setheading(90)
    pen.right(angle)  # angle: CW
    pen.pendown()
    pen.forward(100)

    # Draw Minute hand
    pen.color("#4A9609")
    pen.pensize(10)
    pen.penup()
    pen.setposition(0, 0)
    # m = 10
    angle = (m / 60) * 360
    pen.setheading(90)
    pen.right(angle)  # angle: CW
    pen.pendown()
    pen.forward(150)

    # Draw Second hand
    pen.color("#142164")
    pen.pensize(4)
    pen.penup()
    pen.setposition(0, 0)
    # s = 30
    angle = (s / 60) * 360
    pen.setheading(90)
    pen.right(angle)  # angle: CW
    pen.pendown()
    pen.forward(170)


while True:
    h = int(time.strftime("%I"))  # gives us the Hours from 0 -to- 12
    m = int(time.strftime("%M"))  # gives us the Minutes
    s = int(time.strftime("%S"))  # gives us the Seconds

    # clear all drawings for this pen
    pen.clear()
    time.sleep(1)
    draw_clock(h, m, s)
    wn.update()  # if you use tracer(0) => you should use update()

# Don't close the window automatically
wn.mainloop()
