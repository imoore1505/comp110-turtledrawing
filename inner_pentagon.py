"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle and set the pen color
sat = turtle.Turtle()
sat.pencolor("red")

# draw the pentagon
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)

#color change to green
sat.pencolor("green")
sat.up()
#starting point
sat.goto (15, 15)
sat.down()
sat.forward (25)
sat.left(72)
sat.forward (25)
sat.left(72)
sat.forward (25)
sat.left(72) 
sat.forward (25)
sat.left(72)
sat.forward (25)



turtle_window = turtle.Screen()
turtle_window.exitonclick()
