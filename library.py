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
    you need 3 shelves when making a library).

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
    books = []
    return [name, money_balance, cart, books]

def add_money(customer, money):
    """
    5.1: Make two functions, add_money() and subtract_money() that add and subtract the money of a given user. 
    """
    customer[1] += money

def remove_money(customer, money):
    """
    5.1: Make two functions, add_money() and subtract_money() that add and subtract the money of a given user. 
    """
    customer[1] -= money
    if customer[1] < 0:
        customer[1] = 0

def add_book_to_cart(library, customer, book):
    """
    6: Make an add_book_to_cart() function that adds a book to a cart from a library. Search the library for a book, add it 
    to the cart and remove it from the library. If the book is not found then print the problem.
    """
    found_book = search_book(library, book)
    if(found_book == True):
        genre = book[2]
        for shelf in library[genre]:
            for index in range(len(shelf)):
                item = shelf[index]
                if book == item:
                    customer[2].add(book)
                    shelf.pop(index)
                    break
    else:
        print("Book not found in library.")

def check_out(customer):
    """
    7: Make a buy_cart() that buys all books in a cart and empties the cart. If the user can not afford the 
    cart then print a message stating the problem.
    """
    balance = customer[1]
    cart = customer[2]
    cost = 0.0

    for book in cart:
        cost += book[3]

    if balance < cost:
        print("ERROR: Not enough money!")
    else:
        for book in cart:
            customer[3].append(book)
            customer[2] = set()
            remove_money(customer, cost)
        print("Successfully bought books!")

def print_customer(customer):
    print("Name:", customer[0])
    print("Balance:", customer[1])
    print("Cart:")
    for book in customer[2]:
        print("\t", book)
    print("Books:")
    for book in customer[3]:
        print("\t", book)
        




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

    # Customer data type
    christian = make_customer("Christian", 100.00)
    print_customer(christian)
    print()
    add_money(christian, 20.25)
    print_customer(christian)
    print()
    remove_money(christian, 15.5)
    print_customer(christian)
    print()

    # Add book to cart function
    print("Library before:", library1, end = "\n\n")
    add_book_to_cart(library1, christian, book4)
    add_book_to_cart(library1, christian, book2)
    add_book_to_cart(library1, christian, book2)
    print_customer(christian)
    print("\nLibrary after:", library1)

    # Buy cart function
    remove_money(christian, 134)
    print()
    print_customer(christian)
    check_out(christian) #ERROR: Not enough money
    print()
    add_money(christian, 1434.43)
    check_out(christian)
    print_customer(christian)
    print()
    add_book_to_cart(library1, christian, book3)
    print_customer(christian)
    print()







    





main()


