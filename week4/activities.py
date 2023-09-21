import random
import example

def is_negative(x):
    if x >= 0:
        return False
    else:
        return True

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
"""write unit tests for the stuff above"""


"""
ROLL THE DICE ACTIVITY Part 1
Create a function that simulates rolling a dice. Make a parameter that simulates the amount of sides that dice has. Return an int representing the outcome of the roll. 

ROLL THE DICE ACTIVITY Part 2
Create a function that simulates dice mechanics in Monopoly. You can use the function you created before as a helper function. In case you don’t know the rules:
You roll 2 dice. If they both are the same value, then roll again and return the sum of all outcomes. If not, then return the sum. 
If you roll again for a third time, then you go to jail (in Monopoly). To simulate this in Python, return a zero.
"""

def roll_dice(sides):
    return random.randint(1, sides)

def monopoly_roll():
    one = roll_dice(6)
    two = roll_dice(6)
    if one == two:
        three = roll_dice(6)
        four = roll_dice(6)
        if three == four:
            return 0
        return (one + two + three + four)
    return (one + two)

def error_example(x, y):
    z = example.subtract_numbers(x, y)
    return z

def main():
    x = 5
    y = 6
    z = error_example(x, y)
    print(z)
    
if __name__ == "__main__":
    main()



