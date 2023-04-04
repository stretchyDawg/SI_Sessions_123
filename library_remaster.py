"""
Library Activity REMASTERED in class syntax!!!
@ChristianMorgado
"""

class Book():
    title = ""
    author = ""
    genre = ""
    price = 0.0
    unique_id = 0

def hash_book(book):
    hash_code = 0
    for char_index in len(book.title):
        hash_code += (ord(book.title[char_index]) * (31**(len(book.title)-(char_index-1)))) - book.unique_id

def main():
    book1 = Book
    print(book1.title)
    book1.title = "poop"
    print(book1.title)

main()