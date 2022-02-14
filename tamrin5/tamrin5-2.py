
import turtle
colors=['black']
t=turtle.Pen()
t.speed()
turtle.bgcolor('white')
t.right(90)
for j in range(3, 20):
    t.shape('turtle')
    t.shapesize(0.25) 
    t.penup()
    t.goto(-7*j, 0)
    t.width(j/50)
    for i in range(j):
        t.pendown()
        t.forward(40+j)
        t.left(360/j)


















