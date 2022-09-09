"""
SI Session Notes for the second session of the second week
"""

import turtle as t

#Turtle Commands:
# t.forward() #Takes in int or float values and moves it forward that many pixels
# t.up()
# t.down()
# t.left() #Degree number
# t.right()
# t.goto() #x and y value
# t.xcord() #returns x value
# t.ycord() #return y value
# t.setheading()
# t.fillcolor()
# t.begin_fill()
# t.end_fill()
# t.circle()

def square(x, y, side, fill_color):
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.down()
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.end_fill()
    t.up()
    t.setheading(0)

def equilateral_triangle(x, y, base_side, fill_color):
    t.up()
    t.goto(x,y)
    t.setheading(0)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.down()
    t.forward(base_side)
    t.left(120)
    t.forward(base_side)
    t.left(120)
    t.forward(base_side)
    t.end_fill()
    t.up()
    t.setheading(0)

def circle(x, y, radius, fill_color):
    t.up()
    t.goto(x,y)
    t.setheading(0)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.down()
    t.circle(radius)
    t.end_fill()
    t.up()
    t.setheading(0)

def abe_shape(x, y, ):

def main():
    equilateral_triangle(0, 0, 100, "orange")
    square(0, 0, 100, "orange")
    circle(0, 0, 100, "Blue")
    input("Press enter to end: ")

main()    



