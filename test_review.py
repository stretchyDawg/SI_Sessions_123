#given a file full of numbers seperated by dash's
### example 
### 3/21/45/67/13/15
### 01/1/5/7/13/5/71/
#add every number in the file to some array
#if the file contains a value that is not castable to an int
#throw a TypeError with the message "<thing> is not an int"
#return that array
#note - thing.isdigit() will determine if a string can be an int or not
#prerequisite- there are always 100 numbers in the file

#write a recursive function that counts down from a given value and prints the number. 
#Example, given the number 10, the function would print 10 9 8 7 6 5 4 3 2 1.

import arrays
import array_utils

"""
Question 1
"""
def getNumbers(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            stripped_line = line.strip()
            split_line = stripped_line.split("/")
            for value in split_line:
                if value.isdigit() == True:
                    count += 1
        
        abe_array = arrays.Array(count)
        array_index = 0

        for line in file:
            stripped_line = line.strip()
            split_line = stripped_line.split("/")
            for value in split_line:
                if value.isdigit() == True:
                    abe_array[array_index] = split_line[value]
                    array_index += 1
                else:
                    raise TypeError(split_line[value], " is not a digit.")

    return abe_array

                
"""
Question 2:
"""
def printNums(number):
    if number > 0:
        print(number)
        printNums(number - 1)


def main():
    printNums(10)

main()