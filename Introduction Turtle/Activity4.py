import turtle 
# Creating canvas
turtle.Screen().bgcolor("Chocolate")
sc = turtle.Screen()
sc.setup(400, 300)
turtle.title("Welcome to the turtle window")
# Turtle object creation
board = turtle.Turtle()
# Creating a square
for i in range(2):
    board.forward(50)
    board.left(90)
    board.forward(100)
    board.left(90)