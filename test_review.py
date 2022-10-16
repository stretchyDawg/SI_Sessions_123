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
                
"""
Question 2:
"""