import turtle
# Creating canvas
turtle.Screen().bgcolor("Crimson")
sc = turtle.Screen()
sc.setup(2383, 345)
turtle.title("Welcome to the Python turtle Window canvas")
# Turtle object creation
board = turtle.Turtle()
# Creating a polygon
for i in range(6):
    board.forward(100)
    board.left(60)

turtle.done()