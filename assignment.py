class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def get_details(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def get_details(self):
        return f"Patron: {self.name} (ID: {self.patron_id}) | Borrowed: {len(self.borrowed_books)} books"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Error: Book with ISBN {book.isbn} already exists.")
        else:
            self.books[book.isbn] = book
            print(f"Library added: '{book.title}'")

    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print(f"Error: Patron ID {patron.patron_id} already exists.")
        else:
            self.patrons[patron.patron_id] = patron
            print(f"Library registered patron: {patron.name}")

    def borrow_book(self, patron_id, isbn):
        patron = self.patrons.get(patron_id)
        book = self.books.get(isbn)

        if not patron:
            print(f"Error: Patron ID {patron_id} not found.")
            return
        if not book:
            print(f"Error: Book ISBN {isbn} not found.")
            return

        if book.is_available:
            book.is_available = False
            patron.borrowed_books.append(book)
            print(f"Success: {patron.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry: '{book.title}' is currently checked out.")

    def return_book(self, patron_id, isbn):
        patron = self.patrons.get(patron_id)
        book = self.books.get(isbn)

        if not patron or not book:
            print("Error: Invalid patron ID or book ISBN.")
            return

        if book in patron.borrowed_books:
            book.is_available = True
            patron.borrowed_books.remove(book)
            print(f"Success: {patron.name} returned '{book.title}'.")
        else:
            print(f"Error: {patron.name} does not have '{book.title}' checked out.")

