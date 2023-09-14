"""
CALCULATOR ACTIVITY:
1: Create a function add() that takes in two number values as parameters, adds them, and returns the outcome. Then declare a main() function and use the function. Also, print the outcome in the main() function as well. 
2: Do the same, but instead of adding, create a subtract() function. 
"""
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

"""
IF STATEMENT ACTIVITY 1:
1: Create a function “is_negative()” that takes in a number value as a parameter and returns a boolean based on if that number is negative or not. (In this case zero is positive). Then use this function in the main method. 
2: Create a function “is_even()” that takes in a number value as a parameter and returns a boolean based on if that number is even or not. Then use this function in the main method
"""
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

"""
BONUS ACTIVITY: (If you complete this I will give you candy >:) )
In the main() method, use the four functions we made in the session as follows:
- Add 10 and 16
- Subtract 36 from that number
- Check if that number is negative
    - If it is negative, check if that number is even.
        - If it is even then print that number. 
    - If it is positive then print that number. 
"""
def main():
    x = 10
    y = 16
    z = 36
    result = add(x, y)
    result2 = subtract(result, z)
    is_negative = is_negative(result2)
    if is_negative:
        is_even = is_even(is_negative)
        if is_even:
            print(is_negative)
    else:
        print(result2)
    print()

main()