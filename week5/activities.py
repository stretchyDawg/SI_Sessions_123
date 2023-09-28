"""
LAST NAME:
Declare a string with your full (only first and last) name. Find a way to loop over and print every char ONLY in your last name. (You can do this in a main() function).
"""
def print_last_name(name):
    split_name = name.split(" ")
    for char in split_name[1]:
        print(char)

"""
CHAR COUNTER:
Y’know how when writing a document in Google Docs it says the amount of characters at the bottom? Today we will be programming that in Python.
Declare a function that takes in a string. Return the amount of CHARS (whitespace does NOT count) in the string.
For example, the string “I LOVE GOING TO MY SI SESSIONS” would return 24, rather than the length of the actual string (which is 30).
"""
def count_char(a_string):
    words = a_string.split(" ")
    count = 0
    for word in words:
        for letter in word:
            count+=1
    return count

"""
RANGE SUM:
Create a function that takes a start, stop and step. Using those 3 values, create a range using a range() function and return the sum of that range.
"""
def range_sum(start, stop, step=1):
    range_sum = 0
    for value in range(start, stop, step):
        range_sum+=value
    return range_sum

def main():
    name = "Christian Morgado"
    print_last_name(name)
    
    si_string = "I LOVE GOING TO MY SI SESSIONS"
    print("Length:", len(si_string))
    print("Chars:", count_char(si_string))
    r_sum = range_sum(10, 20)
    print("\nRange Sum:", r_sum)

if __name__ == "__main__":
    main()
