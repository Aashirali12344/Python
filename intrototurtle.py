import turtle
turtle.Screen().bgcolor("Orange")

sc =  turtle.Screen()
sc.setup(400,400)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1


turtle.Screen().bgcolor("Green")
board1 = turtle.Turtle()

board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)





s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
s.bgcolor('black')
turtle.speed('fastest')
turtle.hideturtle()
while True:
    for x in range(200):
        turtle.pencolor(colors[x%len(colors)])
        turtle.width(x/100 + 1)
        turtle.forward(x)
        turtle.left(59)
    turtle.right(239)
    for x in range(200, 0, -1):
        turtle.pencolor('black')
        turtle.width(x/100 +7)
        turtle.forward(x)
        turtle.right(59)


