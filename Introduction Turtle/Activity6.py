import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("Darkorange")
pen = turtle.Turtle()
pen.speed(5)  # Adjust speed (1-10 or 0 for fastest)

# Draw an octadecagon (18 sides)
sides = 18
angle = 360 / sides
length = 50  # Length of each side

for _ in range(sides):
    pen.forward(length)
    pen.right(angle)

# Finish
pen.hideturtle()
turtle.done()
