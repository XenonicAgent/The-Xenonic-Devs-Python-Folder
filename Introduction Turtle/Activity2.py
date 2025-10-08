import turtle

turtle.Screen().bgcolor("Darkorange")
board = turtle.Turtle()

# First triangle for star
board.forward(100) # draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# Second traingle for star
board.pendown()
board.right(90)
board.forward(90)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.bye