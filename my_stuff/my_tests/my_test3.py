import csv

def union(set1, set2):
    """
    SET THEORY - UNION
    Given two sets, write a function that returns the union of
    those two sets.
    """
    return_set = set()
    for val in set1:
        return_set.add(val)
    for val in set2:
        return_set.add(val)
    return return_set
def intersection(set1, set2):
    """
    SET THEORY - INTERSECTION
    Given two sets, write a function that returns the intersection of
    those two sets.
    """
    return_set = set()
    for val1 in set1:
        for val2 in set2:
            if val1 == val2:
                return_set.add(val1)
                break
    return return_set

def highest_grade(grades):
    """
    HIGHEST GRADE
    Write a Python function that takes in a list of tuples, 
    where each tuple represents a student's name and their 
    final grade in a course. The function should return the 
    name of the student with the highest grade. 

    For example, if the input list is: 
    [('Abe', 85), ('Alice', 92), ('Christian', 77)], the 
    function should return 'Alice'.
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
    BOOK GENRE SEARCH
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
    '''
    WORD DICTIONARY
    Given a filename to a text file, return a dictionary of each 
    word and its word count in this key/value form:
    {Word : Word Count}

    The words are NOT case sensitive (i.e. 'The' and 'the' are the
    same thing.)
    '''
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
    COMMUNE SKILL ASSIGNMENT
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
    COMMUNE JOB ASSIGNMENT 
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

def words_by_letter(str):
    """
    WORDS BY THE LETTER 
    Create a function words_by_the_letter(a_string) that takes in a string. 
    Return a dictionary that, given a letter as a key, returns some 
    collection of the words in the string that BEGIN with that letter. 
    """
    letter_dict = dict()
    if len(str) == 0:
        return letter_dict
    split_string = str.split(" ")
    for word in split_string:
        if word[0].lower() in letter_dict:
            letter_dict[word[0].lower()].add(word)
        else:
            letter_dict[word[0].lower()] = set()
            letter_dict[word[0].lower()].add(word)
    return letter_dict


def main():
    set1 = {1, 2, 3, 4, 5, 6, 7}
    set2 = {2, 4, 6, 8, 10, 12, 14}
    print("union:", union(set1, set2))
    print("intersection:", intersection(set1, set2))
    
    a_string = "SI stands for Supplemental Instruction"
    print(words_by_letter(a_string))

    
if __name__ == "__main__":
    main()