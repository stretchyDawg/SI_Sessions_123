import csv

def names_and_addresses(csv_filename):
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_file:
            print(record[0]) # <-- fields here

def main():
    pass