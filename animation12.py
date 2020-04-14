import turtle
star=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
star.pencolor('yellow')
turtle.pensize(5)

for i in range(50):
    star.forward(i*20)
    star.right(144)
turtle.done()    