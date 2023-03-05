import turtle

""" 
For this question, draw a simple clock using turtle. The clock should
have and hour hand and a minute hand. Each component of the clock should be
in its own function.

A sample of what the finished drawing should look like is provided in Clock.png.
"""

DEGREES_IN_CIRCLE = 360
MINUTES_ON_CLOCK = 60
HOURS_ON_CLOCK = 12
NORTH_HEADING = 90

""" Write any helper functions in here """

def clock_circle(radius, face_color):
    turtle.down()
    turtle.fillcolor(face_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()

def minute_hand(minutes, minute_hand_color, radius):
    turtle.up()
    turtle.goto(0,0)
    turtle.setheading(90 - (6 * int(minutes)))
    turtle.pencolor(minute_hand_color)
    turtle.down()
    turtle.forward(.6 * radius)
    turtle.up()
    turtle.goto(0,0)
    turtle.pencolor("Black")

def hour_hand(hours, hour_hand_color, radius):
    turtle.up()
    turtle.goto(0,0)
    turtle.setheading(90 - (30 * int(hours)))
    turtle.pencolor(hour_hand_color)
    turtle.down()
    turtle.forward(.4 * radius)
    turtle.up()
    turtle.goto(0,0)
    turtle.pencolor("Black")

def draw_clock(x,y,hours,minutes,radius,face_color,hour_hand_color,minute_hand_color):
    """ Your clock code goes in here """
    if int(hours) < 1 or int(hours) > 12:
        print("ERROR: Please enter an hour from 1-12.")
        return
    if minutes != "00":
        if int(minutes) < 1 or int(minutes) > 59:
            print("ERROR: Please enter a minute from 1-59, or 00.")
            return
    if minutes == "00":
        minutes = 60
    
    turtle.up()
    turtle.goto(x, (y-radius))
    clock_circle(radius, face_color)
    minute_hand(minutes, minute_hand_color, radius)
    hour_hand(hours, hour_hand_color, radius)


def main():
    draw_clock(0,0,"12","00",100,"yellow","red","blue")
    turtle.hideturtle()
    input("Press Enter to continue...")

main()
