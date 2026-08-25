"""
============================================================
DAY 20 PROJECT — INCREMENTAL LIBRARY MANAGEMENT SYSTEM
============================================================







------------------------------------------------------------
VERSION 8: Validation and @property
------------------------------------------------------------
Add validation:
1. Member names must not be empty.
2. Members cannot borrow more than 3 books at a time.
Use `@property` setters to enforce these conditions.

------------------------------------------------------------
VERSION 9: Custom Exceptions
------------------------------------------------------------
Instead of using prints to indicate failures, define and raise custom exceptions:
- `BookUnavailableError`
- `BorrowLimitExceededError`
Catch these exceptions during execution.

============================================================
MY APPROACH & VERSION LOG:
============================================================
Describe your design details here:

____________________________________________________
____________________________________________________


============================================================
MY CODE:
============================================================
Write your incremental classes here:

____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
"""
# Create a class `Book` with attributes: `title`, `author`, and `is_borrowed` (default: False).
# Include a `__str__` method that returns: "'Title' by Author (Available/Borrowed)".
# ------------------------------------------------------------
# VERSION 2: The Library Class (Empty)
# ------------------------------------------------------------
# Create a class `Library` that initializes with a list of `books` (start with an empty list).


# VERSION 3: Add Books
# ------------------------------------------------------------
# Implement an `add_book(book)` method in the `Library` class that appends a `Book` object to the library's catalog.
# ------------------------------------------------------------
# VERSION 4: Borrow a Book
# ------------------------------------------------------------
# Implement a `borrow_book(title)` method in `Library` that searches for a book by title. 
# If found and available, set `is_borrowed` to True and print a success message. 
# If already borrowed or not found, print a corresponding warning.

# ------------------------------------------------------------
# VERSION 5: Return a Book
# ------------------------------------------------------------
# Implement a `return_book(title)` method in `Library` that sets `is_borrowed` to False when returned.


    # ------------------------------------------------------------
    # VERSION 6: Manage Multiple Copies
    # ------------------------------------------------------------
    # What happens if there are two copies of the same book? Refactor your logic 
    # so that you search for books using a unique identifier (like `isbn`), rather than just matching title text.


# ------------------------------------------------------------
# VERSION 7: Library Members
# ------------------------------------------------------------
# Create a `Member` class with attributes: `name`, `member_id`, and `borrowed_books` (a list of Book objects). 
# Update `Library.borrow_book(isbn, member)` so it registers the book in the member's list.

class Book:
    def __init__(self, title: str, author: str, isbn: str, is_borrowd: bool = False):
        self.title = title
        self.author = author
        self.is_borrowd = is_borrowd
        self.isbn = isbn

    def __str__(self):
        if self.is_borrowd == False:
            status = "Avaiable"
            return f"'{self.title}' by {self.author} ({status})"
        else:
            status = "Borrowed"  
            return f"'{self.title}' by {self.author} ({status})" 


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def __str__(self):
        return f"Member : {self.name} (id : {self.member_id}) Books borrowed : {len(self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, books_name):
        self.books.append(books_name)
    
    def borrow_book(self, isbn, member):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowd == True:
                    print(f"Book '{book.title}' (ISBN: {isbn}) is already borrowed!")
                else:
                    book.is_borrowd = True
                    member.borrowed_books.append(book)
                    print(f"Book '{book.title}' (ISBN: {isbn}) borrowed successfully by {member.name}!")
                return

        print(f"Book with ISBN {isbn} is not found, sorry.")
        
    def return_book(self, isbn, member):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowd == True:
                    book.is_borrowd = False
                    member.borrowed_books.remove(book)
                    print(f"Book '{book.title}' is successfully returned by {member.name}!")
                else:
                    print(f"Book was not currently borrowed.")
                return
        print(f"Book with ISBN {isbn} is not found, sorry.")


# 1. CREATE YOUR OBJECTS FIRST (Top of execution)
book1 = Book("Harry pottery", "harry", "DFW1", False)
member1 = Member("Dipesh", "M001")
mylibaray = Library()

# 2. NOW USE THEM DOWN HERE
mylibaray.add_book(book1) 
print("Library inventory count:", len(mylibaray.books))
print("First book in library:", mylibaray.books[0])

print("\n--- Testing Borrow ---")
mylibaray.borrow_book("DFW1", member1)
print(book1)
print(member1)

print("\n--- Testing Return ---")
mylibaray.return_book("DFW1", member1)
print(book1)
print(member1)

