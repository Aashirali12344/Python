import turtle


screen = turtle.Screen()
screen.bgcolor("lightgrey")
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

def draw_polygon(sides, length, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.fillcolor(color)
    t.begin_fill()
    
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
        
    t.end_fill()


draw_polygon(3, 100, "skyblue", -150, 0)


draw_polygon(6, 70, "lightgreen", 50, 0)


t.penup()
t.goto(-50, -150)
t.pendown()
t.fillcolor("salmon")
t.begin_fill()
for _ in range(2):
    t.forward(150) 
    t.left(90)
    t.forward(80)  
    t.left(90)
t.end_fill()

t.hideturtle()
screen.mainloop()