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


"""
SHAPE ACTIVITY 2:
Create a function that prompts a user for the edge of a dodecahedron. Using that edge, calculate the surface area of a dodecahedron and print it to the console. Here is the formula for the surface area of a dodecahedron with ‘a’ being the edge and ‘A’ being the surface area:
"""
def dodeca_area():
    edge = float(input("Enter an edge: "))
    area = (3)*(25+10*(5**0.5))**0.5
    area = area*(edge**2)
    print("Area:", area)



"""
CAFE SHOP ACTIVITY 
As the owner of a coffee shop, you wanted a program that quickly calculates the total cost of someone’s order. Write a function (or multiple functions if you want) that will prompt for the number of iced coffees, bagels, and MATCHA (i love matcha)! Then, calculate the total cost of the order. Also, there is a sales tax of 6% for every order, so make sure that the sales tax is in the final price!

These are the prices of each item on the menu:
Iced Coffee: $4.00
Bagels: $1.75
MATCHA: $5.00

Then, print out the final cost of the order!
"""
def cafe_shop():
    iced_coffee = 4.00
    bagels = 1.75
    matcha = 5.00

    amount_of_iced_coffee = float(input("How much iced coffees do you want? "))
    amount_of_bagels = float(input("How much bagels do you want? "))
    amount_of_matcha = float(input("How much matchas do you want? "))

    total_cost = ((amount_of_bagels)*bagels) + ((amount_of_iced_coffee)*iced_coffee) + ((amount_of_matcha)*matcha)
    sales_tax = total_cost*.06
    print("This is the total cost:", total_cost+sales_tax) 

cafe_shop()


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

