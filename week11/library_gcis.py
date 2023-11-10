class Book():
    __slots__ = ["title", "author"]

    def __init__(self, title, author):
        self.title = title
        self.author = author

class Patron():
    __slots__ = ["id", "name", "want_list", "checked_out_books"]

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.want_list = set()
        self.checked_out_books = set()

class CardCatalog():
    __slots__ = ["books_by_title", "books_by_catalog"]

    def __init__(self):
        self.books_by_author = dict()
        self.books_by_title = dict()

class Library():
    __slots__ = ["shelves", "patrons", "card_catalog"]

    def __init__(self):
        self.shelves = dict()
        self.patrons = dict()
        self.card_catalog = CardCatalog()

def find_by_author(library, author):
    card_catalog = library.card_catalog
    books_by_author = card_catalog.books_by_author
    if author in books_by_author:
        return books_by_author[author]
    else:
        return set()

def find_by_title(library, title):
    card_catalog = library.card_catalog
    books_by_title = card_catalog.books_by_title
    if title in books_by_title:
        return books_by_title[title]
    else:
        return set()

def check_out_book(library, patron_id, book):
    copies = library.shelves[book]
    patron = library.patrons[patron_id]
    if copies > 0:
        copies -= 1
        library.shelves[book] = copies
        patron.checked_out.add(book)
    else:
        patron.want_list.add(book)

def main():
    pass

if __name__ == "__main__":
    main()

