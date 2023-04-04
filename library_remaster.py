"""
Library Activity REMASTERED in class syntax!!!
@ChristianMorgado
"""

class Book():
    """
    1: Create a Book class. A book should at least have a title, author, genre and price.
    """
    title = ""
    author = ""
    genre = ""
    price = 0.0
    unique_id = 0

def hash_book(book):
    """
    2: Program a hash function for the book! (We wont actually implement the hash function, 
       but it is a good way to see how hash functions are used in relation to classes and 
       data structures)!
    """
    hash_code = 0
    for char_index in range(len(book.title)):
        hash_code += ((ord(book.title[char_index]) * (31**(len(book.title)-(char_index-1)))) / book.unique_id) + book.price
    
    return hash_code

class Shelf():
    """
    3: Create a Shelf class. Shelves are organized by genre, and can only hold 10 books each. They can hold duplicate books.
    """
    shelf = []
    shelf_genre = ""
    length = 0

def add_to_shelf(shelf, book):
    if book.genre == shelf.shelf_genre and shelf.length < 10:
        shelf.shelf.append(book)
    shelf.length += 1

def remove_from_shelf(shelf, index):
    try:
        shelf.shelf.pop(index)
        shelf.length -= 1
    except:
        print("Invalid Index")
    

class Library():
    """
    4: Create a library class. Libraries are a collection of shelves. We will discuss the parameters and data structures used!

    In this case, a library is a dictionary: {Key=Shelf_Genre : Value=List_Of_Shelves}
    """
    shelves = dict()

def add_shelf(library, shelf):
    if shelf.shelf_genre in library.shelves:
        for book in shelf:
            library.shelves.append(book)
    else:
        library.shelves[shelf.shelf_genre] = shelf




def main():
    book1 = Book
    print(book1.title)
    book1.title = "poop"
    book1.unique_id = 1872
    book1.price = 2.24
    print(book1.title)
    print(hash_book(book1))

    book2 = book1
    book2.unique_id = 1873
    print(book2.title)
    print(hash_book(book2))

    shelf1 = Shelf
    print(shelf1.shelf)
    print("Genre:", shelf1.shelf_genre)
    add_to_shelf(shelf1, book1)
    add_to_shelf(shelf1, book2)
    print(shelf1.shelf)
    print("Genre:", shelf1.shelf_genre)

    book3 = book2
    book3.genre = "fart"
    add_to_shelf(shelf1, book3)
    print(shelf1.shelf)
    remove_from_shelf(shelf1, 0)
    print(shelf1.shelf)
    remove_from_shelf(shelf1, 3)
    print(shelf1.shelf)




main()