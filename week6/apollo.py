"""
APOLLO XXI PART 1
Using this CSV data of my Album of the Week (Apollo XXI by Steve Lacy), make a function (that makes use of the csv module) that prints the tracklisting in this format:
1: Title: <song_title>, Length: <length>

For example, it would print Guide as:
5: Title: Guide, Length 2:21

The function doesn’t have to return anything.
-------------------------------------------------------------------------------
APOLLO XXI PART 2
Make a function that, using the same CSV file and csv module, returns the full length of time for the album. Then print that value in the main function in this format: 
minutes:seconds

(Hint: the answer for Apollo XXI is 42:58, but find a way to get this using Python math (so that you can use your function for any tracklisting)!
-------------------------------------------------------------------------------
USING MORE ALBUMS AS PARAMETERS
I supplied another csv file with another favorite album of mine, Atlanta Millionaires Club by Faye Webster. Try using the functions with that csv file.
(The total runtime for the Faye Webster album is 31:45)

Try using your favorite album, create a csv file and find the total time on wikipedia and use it as a parameter for your function. Creating a csv file for your function is a good way to visualize how your function is parsing the csv file.
-------------------------------------------------------------------------------
ANALYZE THE FUNCTIONS
Notice how the first four lines are the same? Manipulating files in Python follows a pattern. Every function that manipulates files has a 'skeleton':
    with open(filename) as file:            # Open file
        csv_reader = csv.reader(file)       # Use csv module to handle dirty data 
        next(csv_reader)                    # Skip first line in csv file
        for record in csv_reader:           # Iterate through file (record is a variable name)

Writing this skeleton on your cheat sheet is a good way to make sure you know how to manipulate files. For the very dedicated people, try and understand what is happening on each line. I provided some comments to help out with that.
-------------------------------------------------------------------------------
LISTEN TO MY ALBUM RECS
If you listen to the two albums I used you will 100% pass the next exam (don't quote me on this):
1. Apollo XXI by Steve Lacy
2. Atlanta Millionaires Club by Faye Webster

If you like similar music pls recommend me :P
"""
import csv

def print_tracklisting(filename):
    """Part 1"""
    with open(filename) as file:            # Open file
        csv_reader = csv.reader(file)       # Use csv module to handle dirty data
        next(csv_reader)                    # Skip first line in csv file
        
        count = 0                           # To print each track number
        for record in csv_reader:
            count += 1
            title = record[0]               # Isolate title and length (setting them to variables for clarification)
            length = record[1]              # Look at apollo.csv for more info
            print(count, ": Title: ", title, ", Length: ", length, sep = "")

def find_total_time(filename):
    """Part 2"""
    with open(filename) as file:            # Open file
        csv_reader = csv.reader(file)       # Use csv module to handle dirty data
        next(csv_reader)                    # Skip first line in csv file
        
        total_minutes = 0
        total_seconds = 0
        for record in csv_reader:
            length = record[1]                 # Length in format minutes:seconds (i.e. 3:42)
            split_length = length.split(":")   # Split to isolate minutes and seconds 
            minutes = int(split_length[0])     # When isolating you MUST cast.
            seconds = int(split_length[1])     # Files return STRINGS. The length is a STRING. So you must cast

            total_minutes += minutes           # Add times to totals
            total_seconds += seconds

        # Time math (if you just want to know how to manipulate files in Python this math is not important to you)
        total_minutes += (total_seconds // 60)
        total_seconds = total_seconds % 60

        return str(total_minutes) + ":" + str(total_seconds)

def main():
    filename1 = "apollo.csv"
    filename2 = "atlanta.csv"
    
    print("\nTRACK LISTING (PART 1):")
    print_tracklisting(filename2)

    print("\nTOTAL TIME (PART 2):")
    print(find_total_time(filename2))

if __name__ == "__main__":
    main()