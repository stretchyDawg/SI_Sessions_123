import array_utils

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
                    except:
                        print("Error: ZERO DIVISION")
                else:
                    print("Error: ", operator, " is an INVALID OPERATOR.", sep = "")
            except:
                print("Error: INVALID DATA TYPES.")
    
def main():
    array = array_utils.range_array(1, 11)
    print(array)
    print(array_sum(array))

    print_file_uppercase("data/alice.txt")
    
main()