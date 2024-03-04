"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle
x = input("pencolor")
y = int(input("length?"))
# create a turtle and set the pen color
sat = turtle.Turtle()
sat.pencolor(x)


# draw the pentagon
sat.forward(y)
sat.left(72)
sat.forward(y)
sat.left(72)
sat.forward(y)
sat.left(72)
sat.forward(y)
sat.left(72)
sat.forward(y)
sat.left(72)

# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()