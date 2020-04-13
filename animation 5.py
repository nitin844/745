
import turtle 
loadWindow = turtle.Screen() 
turtle.speed(12) 
turtle.pencolor("blue")

for i in range(360): 
	turtle.circle(5*i) 
	turtle.circle(-5*i) 
	turtle.left(i) 

turtle.exitonclick() 
