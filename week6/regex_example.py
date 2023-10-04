import csv
import re
def zip_check(filename):
    with open(filename) as my_file:
        reader = csv.reader(my_file)
        next(reader)

        for record in reader:
            name = record[0]
            address = record[1]
            if re.findall("", address):
                print(name, address)
                
