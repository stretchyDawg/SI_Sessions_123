import arrays

def print_values(an_array):
    for index in range(len(an_array)):
        print("Value at index", index, ":", an_array[index])
        
def main():
    an_array = arrays.Array(10)     # Making array
    an_array[2] = "Hello"           # Changing third index
    print_values(an_array)


    # print(an_array)                 # Printing array
    # print("Length:", len(an_array)) # Printing array length

if __name__ == "__main__":
    main()

