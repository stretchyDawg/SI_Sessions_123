"""
paper was given physically

prompts are not in this specific file
"""
import arrays
import array_utils
import csv

ASCII_ARRAY = array_utils.range_array(48, 58)


def sum_of_digits(number):
    number = str(number)
    the_sum = 0
    for digit in number:
        try:
            the_sum += int(digit)
        except:
            continue
    return the_sum

def odd_array_copy(an_array):
    try:
        length = 0
        for value_index in range(len(an_array)):
            if an_array[value_index] % 2 != 0:
                length+=1
        array_copy = arrays.Array(length)
        index = 0
        for value_index in range(len(an_array)):
            if an_array[value_index] % 2 != 0:
                array_copy[index] = an_array[value_index]
                index += 1
        return array_copy
    except TypeError:
        return an_array
    
def count_comics(filename, given_creator):
    try:
        count = 0
        with open(filename) as file:
            reader = csv.reader(file)
            next(reader)
            for record in reader:
                creator_record = record[8]
                creators = creator_record.split("|")
                for creator in creators:
                    if creator == given_creator:
                        count+=1
        return count
    except FileNotFoundError:
        return None
            
def cast_to_int(a_string, index=0, multiplier=None):
    if multiplier == None:
        multiplier = 10**(len(a_string)-1)
    
    if index == len(a_string):
        return 0
    for ascii_index in range(len(ASCII_ARRAY)):
        if ord(a_string[index]) == ASCII_ARRAY[ascii_index]:
            return (ascii_index*multiplier) + cast_to_int(a_string, index+1, multiplier/10)
        
def main():
    test = cast_to_int("1234")
    print(test)

if __name__ == "__main__":
    main()