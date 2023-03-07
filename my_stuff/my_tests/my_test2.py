import array_utils
import arrays
import csv

# MAKE UPPERCASE ANSWER:
def print_file_uppercase(filename):
    with open(filename) as my_file:
        for line in my_file:
            print(line.upper())
            
# ARRAY SUM ANSWER:
def array_sum(array, index=0):
    if(index == len(array)-1):
        return array[index]
    else:
        return array[index] + array_sum(array, index+1)

# CSV CALC ANSWER:
def csv_calc(filename):
    try:
        with open(filename) as my_file:
            next(my_file)
            for line in my_file:
                split_line = line.split(",")
                operator = split_line[0]
                try:
                    value1 = float(split_line[1])
                    value2 = float(split_line[2])

                    if operator == "+":
                        print("Sum:", value1 + value2)
                    elif operator == "-":
                        print("Subtraction:", value1 - value2)
                    elif operator == "*":
                        print("Product:", value1 * value2)
                    elif operator == "/":
                        try:
                            print("Quotient:", value1 / value2)
                        except ZeroDivisionError:
                            print("Error: ZERO DIVISION")
                    else:
                        print("Error: ", operator, " is an INVALID OPERATOR.", sep = "")
                except:
                    print("Error: INVALID DATA TYPES.")
    except FileNotFoundError as fe:
        print("Error: File \'", filename ,"\' not found.", sep = "")

def array_of_data(filename, test_num):
    array = arrays.Array(10)
    index = 0
    
    with open(filename) as my_file:
        next(my_file)
        csv_reader = csv.reader(my_file)
        for record in csv_reader:
            test = record[test_num]
            if test == "true":
                array[index] = record[0]
                index += 1

    return array
            
def binary_search(array, target, start=None, end=None):
    try: 
        # Input Validation: 
        if start is None:
            start = 0 
            end = len(array)-1
        if start > end:
            return None

        midpoint = (start + end) // 2
        value = array[midpoint]

        if value == target:
            return midpoint
        elif value < target:
            start = midpoint + 1
            return binary_search(array, target, start, end)
        elif value > target:
            end = midpoint - 1
            return binary_search(array, target, start, end)
    except TypeError:
        return None

    
def main():
    array = array_utils.range_array(1, 11)
    print(array)
    print(array_sum(array))

    print_file_uppercase("data/christian.txt")
    
main()