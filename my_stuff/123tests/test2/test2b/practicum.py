"""
Practicum File
@ChristianMorgado
"""
import csv
import arrays


"""
Question 1:
"""
def count_letters(str1, str2):
    count = 0
    string1 = str1.lower()
    string2 = str2.lower()

    for letter in string1:
        value1 = letter
        for letters in string2:
            value2 = letters
            if value1 == value2:
                count += 1
    return count


"""
Question 2:
"""
def count_comics(filename, creator):
    count = 0
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            creators = record[8].split("|")
            for author in creators:
                if author == creator:
                    count += 1
    return count


"""
Question 3:
"""
def make_array():
    size = input("Enter a size: ")
    array = arrays.Array(int(size))
    length = len(array)
    index = 0

    while index <= length - 1:
        value = input("Enter value: ")
        try:
            array_value = float(value)
        except:
            print(value, " is not a numeric value. Try again.", sep = "")
            continue
        if array_value != None:     
            int_array_value = int(array_value)
            if int_array_value == array_value:
                array[index] = int_array_value
                index += 1
            else:
                array[index] = array_value
                index += 1
    
    return array


"""
Question 4:
"""
def array_sum(array, start, end):
    mid = (start + end) // 2
    
    if start > end:
        return 0
    elif start == end:
        return array[start]
    else:
        return array_sum(array, start, mid) + array_sum(array, mid+1, end)


def main():
    # Question 1:
    vowel = "aeiou"
    abe = "Abraham Lincoln"
    num = count_letters(vowel, abe)
    print(num)

    # Question 3:
    poop = make_array()
    print(poop)

    # Question 2:
    fart = count_comics("data/comics.csv", "Gene Colan")
    print(fart)




if __name__ == "__main__":
    main()