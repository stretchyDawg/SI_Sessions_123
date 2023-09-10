"""
SHAPE ACTIVITY 1:
Create a function that prompts a user for a radius of a circle. Using that radius calculate the area of a circle and print it to the console. Here is the formula for the area of a circle with ‘r’ as the radius:
Area = pi(r)^2

The name of the function and variables are up to you!
"""
def circle_area():
    radius = input("Enter a radius: ")
    radius = float(radius)
    area = 3.14*((radius)**2.0)
    print("Area:", area)

circle_area()

"""
SHAPE ACTIVITY 2:
Create a function that prompts a user for the edge of a dodecahedron. Using that edge, calculate the surface area of a dodecahedron and print it to the console. Here is the formula for the surface area of a dodecahedron with ‘a’ being the edge and ‘A’ being the surface area:
"""
def dodeca_area():
    edge = float(input("Enter an edge: "))
    area = (3)*(25+10*(5**0.5))**0.5
    area = area*(edge**2)
    print("Area:", area)

dodeca_area()

"""
CALCULATOR ACTIVITY (Part 1):
Create a function that takes two numbers as input and print the result of doing these operations with them (formatting the print statements is not necessary):
Adding them
Subtracting them
Multiplying them
Dividing them
Floor dividing them
Using them as exponents (x^y)
Print the square root of both of them

(This is very similar to what was done in class but involves more expressions!)
Part 2 will continue next unit when we learn a new topic (which is a secret for now)!
"""
def calc():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print("x+y:",x+y)
    print("x-y:",x-y)
    print("x*y:",x*y)
    print("x/y:",x/y)
    print("x**y:",x**y)
    print("x//y:",x//y)
    print("x%y:",x//y)
    print("sqrt(x):",x**0.5)
    print("sqrt(y):",y**0.5)

calc()

