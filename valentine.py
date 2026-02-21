import turtle
import time

# Set up the canvas
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1a1a2e")
screen.title("For You")

# Set up the drawing pen
pen = turtle.Turtle()
pen.color("#e94560")
pen.fillcolor("#e94560")
pen.pensize(3)
pen.speed(4)

def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
    pen.forward(112)
    pen.end_fill()

# Move into position and draw
pen.penup()
pen.goto(0, -50)
pen.pendown()
draw_heart()

# Add the anniversary message
pen.penup()
pen.goto(0, -120)
pen.color("white")
# You can change the message below!
pen.write("Happy Anniversary!", align="center", font=("Arial", 24, "bold"))
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
