class Boks:
    """Book information"""

    def __init__(self, author, year, title):
        self.author = author
        self.year = year
        self.title = title

    def get_info(self):
        return f"author: {self.author}, year: {self.year}, title: {self.title}"

    def is_old(self):
        current_year = 2024
        return (current_year - self.year) > 1997
class User:
    """User information"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"name: {self.name}, email: {self.email}"

class Library:
    """Library management"""
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, title, user_email):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{user_email} Brrowen '{title}'")
                return
        print(f"Book '{title}' is Not available.")

    def return_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' hs  a rned to the library.")

# Example usage:
library = Library()
book1 = Boks("Red", 1858, "Festival")
book2 = Boks("Farnam", 1893, "How life Rich")

library.add_book(book1)
library.add_book(book2)

user1 = User("createR", "creator6985@gmail.com")
library.register_user(user1)

library.borrow_book("Festiv", user1.email)
library.return_book(book2)