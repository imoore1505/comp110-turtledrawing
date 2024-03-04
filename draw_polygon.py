"""
Module: draw_polygon

Program to draw a regular polygon based on user's input.
"""

import turtle
z = int(input("nuber of sides"))
x = int(input("length?"))
n = ((360)/z)
# create a turtle and set the pen color
duzzy = turtle.Turtle()
duzzy.pencolor("red")

# PUT YOUR NEW CODE HERE
for i in range(z) :
    duzzy.forward(x)
    duzzy.left(n)
# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()
