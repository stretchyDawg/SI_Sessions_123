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