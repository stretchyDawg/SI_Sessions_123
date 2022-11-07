"""
1.
Given a csv file containing the following header:
index,name,url,street_address,city,state,zip_code,country,hours,latitude,longitude

Return a list of tuples containing only the street_address, latitude, and longitude.
"""
import csv
def quesh_1(filename):
    tup_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            csv_tup = (record[3], record[9], record[10])
            tup_list.append(csv_tup)
    return tup_list


"""
2. 
Given the same csv file:

Create and return a dictionary that uses the index as the key and the zipcode as the value. Then in the main, print out all of zipcodes.
"""
def quesh_2(filename):
    csv_dict = dict()
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            index = record[0]
            zip_code = record[6]
            csv_dict[index] = zip_code
    return csv_dict

def main_2():
    csv_dict = quesh_2("funny_file.csv")
    for index in csv_dict:
        print(index, ":", csv_dict[index], sep = "")


"""
3.
Given two filenames:
Return all of the words that are in both files as whatever data structure you feel is most appropriate.
"""
def quesh_3(filename1, filename2):
    file1_words = []
    file2_words = []
    word_tuple = (file1_words, file2_words)
    with open(filename1) as my_file:
        for line in my_file:
            line = line.split(" ")
            for word in line:
                file1_words.append(word)
    with open(filename2) as my_file:
        for line in my_file:
            for word in line:
                file2_words.append(word)
    return word_tuple


        




        











