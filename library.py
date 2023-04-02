"""
Library SI Session Assignment: Makes use of consideration of lists, tuples, sets and dictionaries.
@ChristianMorgado Spring Sem 23'
"""

def make_book(name, author, genre, price):
    """
    1: Make a function make_book() that creates a data structure representation of a book. 
    We will discuss the parameters and data structures used! (For the purpose of this 
    assignment there should be a genre and price for the book).
    """
    return (name, author, genre, price)

def make_shelf(book):
    """
    2: Make a function make_shelf() that makes a collection (shelf) of book. Each book in 
    the shelf MUST have the same genre. It can contain repeats. We will discuss the parameters 
    and data structures used! (For the purpose of this assignment you need 1 book when making 
    a shelf).
    """
    return [book]

def add_book(shelf, book):
    """
    2.1: Make a function add_book() that adds a book to a shelf. If the genre is different then
    do nothing. 
    """
    genre = book[2]
    shelf_genre = shelf[0][2]
    if genre == shelf_genre:
        shelf.append(book)

def remove_book(shelf, index):
    """
    2.2: Make a function remove_book() that removes a book from a shelf using an index. 
    """
    try:
        shelf.pop(index)
    except:
        print("ERROR: Invalid index.")

def library(shelf1, shelf2, shelf3):
    """
    3: Make a function library() that creates a library. A library is a collection of shelves. 
    We will discuss the parameters and data structures used! (For the purpose of this assignment
    you need at least 3 shelves when making a book).

    In this case, a library is a dictionary: {Key=Shelf_Genre : Value=List_Of_Shelves}
    """
    library = dict()
    shelves = [shelf1, shelf2, shelf3]
    for shelf in shelves:
        shelf_genre = shelf[0][2]
        if shelf_genre in library:
            library[shelf_genre].append(shelf)
        else:
            library[shelf_genre] = [shelf]

    return library

def search_book(library, given_book):
    """
    4: Make a function search_book(library, book) that returns a boolean representing 
    if the book is in the library or not. Find the most efficient way to search for the 
    book. 
    """
    genre = given_book[2]
    if genre in library:
        shelves = library[genre]
        for shelf in shelves:
            for book in shelf:
                if given_book == book:
                    return True
    return False

def make_customer(name, money_balance):
    """
    5: Make a function make_customer() that creates a data structure representation of a 
    customer. A customer should have a wallet and a cart to be able to buy a certain amount 
    of books, that cart can only hold at max 5 unique books.
    """
    cart = set()
    return [name, money_balance, cart]

def add_money(customer, money):
    """
    5.1: Make two functions, add_money() and subtract_money() that add and subtract the money of a given user. 
    """
    customer[1] += money

def remove_money(customer, money):
    """
    5.1: Make two functions, add_money() and subtract_money() that add and subtract the money of a given user. 
    """
    customer[1] += money
    if customer[1] < 0:
        customer[1] = 0




def main():
    # Books
    book1 = make_book("poop", "me", "Fiction", 2.99)
    book2 = make_book("poop2", "me", "Fiction", 2.99)
    book3 = make_book("poop3: Rodrick Rules", "me", "Fiction", 2.99)
    book4 = make_book("pee", "you", "Non-Fiction", 3.99)
    print(book1, end = "\n\n")

    # Shelves
    fiction_shelf = make_shelf(book1)
    print(fiction_shelf)
    add_book(fiction_shelf, book2)
    add_book(fiction_shelf, book3)
    print(fiction_shelf)
    add_book(fiction_shelf, book4)
    print(fiction_shelf, end = "\n\n")

    # Libraries
    fiction_shelf2 = make_shelf(book2)
    add_book(fiction_shelf2, book2)
    non_fiction_shelf = make_shelf(book4)
    add_book(non_fiction_shelf, book4)

    library1 = library(fiction_shelf, fiction_shelf2, non_fiction_shelf)
    for key in library1:
        print("Genre: ", key, "\nBooks: ", library1[key], sep = "", end = "\n\n")

    # Search function
    book5 = make_book("poop4: Dog Days", "me", "Fiction", 2.99)
    print("Book 4:", search_book(library1, book4))
    print("Book 5:", search_book(library1, book5), end = "\n\n")






    





main()


