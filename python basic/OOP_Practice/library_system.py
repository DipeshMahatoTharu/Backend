"""
Practice Project: Library System
================================
Requirements:
1. Create a `Book` class:
   - Attributes: `title` (str), `author` (str), `isbn` (str), `is_borrowed` (bool, default False).
   - Methods: `__str__` returning a formatted string representation of the book.
2. Create a `Library` class:
   - Attributes: `name` (str), `books` (list of Book objects).
   - Methods:
     - `add_book(book)`: Adds a Book object to the library catalog.
     - `remove_book(isbn)`: Removes a Book object from the library catalog using its ISBN.
     - `find_books_by_title(title)`: Returns a list of Book objects matching the search title.
     - `borrow_book(isbn)`: Marks the book with the matching ISBN as borrowed if it is available.
     - `return_book(isbn)`: Marks the book with the matching ISBN as returned.
     - `display_catalog()`: Prints all books in the catalog and their current status (Available / Borrowed).

Write your code below and test it by running this file.
"""

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        # TODO: Initialize book attributes
        pass

    def __str__(self) -> str:
        # TODO: Return formatted string representation of book
        return ""


class Library:
    def __init__(self, name: str):
        # TODO: Initialize library attributes
        pass

    def add_book(self, book: Book):
        # TODO: Add book to library
        pass

    def remove_book(self, isbn: str) -> bool:
        # TODO: Remove book from library catalog
        pass

    def find_books_by_title(self, title: str) -> list:
        # TODO: Find books matching the title
        return []

    def borrow_book(self, isbn: str) -> bool:
        # TODO: Borrow a book by ISBN
        pass

    def return_book(self, isbn: str) -> bool:
        # TODO: Return a borrowed book by ISBN
        pass

    def display_catalog(self):
        # TODO: Print catalog list
        pass


# =====================================================================
# TEST SUITE (Run this file to verify your implementation)
# =====================================================================
if __name__ == "__main__":
    print("Testing Library System Class...")
    
    # Try testing your code here:
    # my_lib = Library("Kathmandu Central Library")
    # b1 = Book("Python Crash Course", "Eric Matthes", "9781593279288")
    # my_lib.add_book(b1)
    # ...
    
    print("\nComplete the class implementation to pass the test cases!")
