import csv

def union(set1, set2):
    """
    1.1: SET THEORY - UNION
    Given two sets, write a function that returns the union of
    those two sets.
    """
    set3 = set()
    for val in set1:
        set3.add(val)
    for val in set2:
        set3.add(val)
    return set3
def intersection(set1, set2):
    """
    1.2: SET THEORY - INTERSECTION
    Given two sets, write a function that returns the intersection of
    those two sets.
    """
    set3 = set()
    for val1 in set1:
        for val2 in set2:
            if val1 == val2:
                set3.add(val1)
                break
    return set3

def highest_grade(grades):
    """
    2: HIGHEST GRADE
    Write a Python function that takes in a list of tuples, 
    where each tuple represents a student's name and their 
    final grade in a course. The function should return the 
    name of the student with the highest grade. 

    For example, if the input list is: 
    [('Alice', 85), ('Bob', 92), ('Charlie', 77)], the function should return 'Bob'.
    """
    highest_grade = 0
    highest_name = ""
    
    for student in grades:
        name = student[0]
        grade = student[1]
        if grade > highest_grade:
            highest_grade = grade
            highest_name = name
            
    return highest_name

def genre_search(booklist, genre):
    """
    3: BOOK GENRE SEARCH
    Write a Python function that takes in a list of tuples 
    representing books in this form: 
    (name, author, genre)

    Given a genre, the function should return a collection of 
    unique books of that genre (which is passed to the function 
    as a parameter).
    """
    found_books = set()

    for book in booklist:
        book_genre = book[2]
        if book_genre == genre:
            found_books.add(book)

    return found_books

def word_dictionary(filename):
    with open(filename) as my_file:
        word_dict = dict()
        for line in my_file:
            split_line = line.split(" ")
            for word in split_line:
                word = word.lower()
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 0 

def skill_assignment(filename):
    """
    5.1: COMMUNE SKILL ASSIGNMENT
    Iterate through a CSV file of workers in this form:
    name, age, skill1, skill2, skill3, proficiency

    Return a collection of tuples of workers in this form:
    (name, age, proficiency, collection of skills)
    MUST BE EXACTLY IN THIS FORM ^
    """
    with open(filename) as my_file:
        csv_reader = csv.reader(my_file)
        workers = []
        
        next(csv_reader)
        for record in csv_reader:
            name = record[0]
            age = record[1]
            skill1 = record[2]
            skill2 = record[3]
            skill3 = record[4]
            proficiency = record[5]
            workers.append((name, age, proficiency, {skill1, skill2, skill3}))

        return workers
def job_assignment(workers):
    """
    5.2: COMMUNE JOB ASSIGNMENT 
    Given this collection of tuples, return a dictionary
    representing workers in this form:
    {proficiency : collection of workers (as tuples)}
    """
    job_dict = dict()

    for worker in workers:
        proficiency = worker[2]
        if proficiency in job_dict:
            job_dict[proficiency].add(worker)
        else:
            job_dict[proficiency] = set()
            job_dict[proficiency].add(worker)

    return job_dict

def main():
    set1 = {1, 2, 3, 4, 5, 6, 7}
    set2 = {2, 4, 6, 8, 10, 12, 14}
    print("union:", union(set1, set2))
    print("intersection:", intersection(set1, set2))
if __name__ == "__main__":
    main()