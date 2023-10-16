import arrays

"""
GCIS-123 SI Recursion Activities
Created: February 2023
Last updated: October 2023 (occurances question)

By: Christian Morgado
"""

"""
FACTORIAL:
Create a function that computes the factorial of a non-negative integer using recursion. 

The factorial of a number is the product of all positive integers from 1 to that number. For instance, if the user enters '4,' your program should find the factorial of 4, which is 24 (4 x 3 x 2 x 1)
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

"""
FIBONACCI:
Create a function that calculates the nth number in the Fibonacci sequence using recursion. 

The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers. For example, if the user enters '5,' your program should find the 5th number in the sequence, which is 3 (0, 1, 1, 2, 3)
"""
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # The nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

"""
SUM OF DIGITS:
Develop a program that calculates the sum of the digits of a positive integer using recursion. Note: this involves a bit of math
BTW this one is REALLY hard.

For example, if the user enters '12345,' your program should add the digits together: 1 + 2 + 3 + 4 + 5, and return the sum, which is 15.
"""
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_of_digits(remaining_digits)
    
"""
OCCURANCES
Develop a program that uses recursion to find the amount of occurances of a target value in a given array.

For example, if the array is [1, 3, 6, 2, 3, 3, 5, 3] and the target value is 3 it would return 4.
"""
def occur(array, target, index=0, occurances=0):
    if index >= len(array):
        return occurances
    else:
        value = array[index]
        if value == target:
            return occur(array, target, index+1, occurances+1)
        elif value != target:                                
            return occur(array, target, index+1, occurances)

def main():
    # This main function uses f-strings. You aren't taught this in GCIS-123 but it just makes it easier when visualizing code.
    # For f-string Python info go here: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/#
    #
    # Based on your CAs, they may or may not allow you to use them. If you want to then ask them. 

    result = factorial(4)   # Calculate 4!
    print(result)           # Output: 24

    n = 10                  # Calculate the 10th Fibonacci number
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is {result}")

    number = 12345          # Replace with any positive integer
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {result}")
    
    array = arrays.Array(5, 0)
    array[0] = 3
    array[1] = 2
    array[2] = 1
    array[3] = 3
    array[4] = 5
    target = 3              # Find how many times 3 is in the array
    occurances = occur(array, 3)
    print(f"The target value {target} is in the array {occurances} time(s)")
if __name__ == "__main__":
    main()