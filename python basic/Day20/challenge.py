"""
============================================================
DAY 20 PROJECT — INCREMENTAL LIBRARY MANAGEMENT SYSTEM
============================================================




------------------------------------------------------------
VERSION 6: Manage Multiple Copies
------------------------------------------------------------
What happens if there are two copies of the same book? Refactor your logic 
so that you search for books using a unique identifier (like `isbn`), rather than just matching title text.

------------------------------------------------------------
VERSION 7: Library Members
------------------------------------------------------------
Create a `Member` class with attributes: `name`, `member_id`, and `borrowed_books` (a list of Book objects). 
Update `Library.borrow_book(isbn, member)` so it registers the book in the member's list.

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

class Book:
    def __init__(self,title:str,author:str,is_borrowd:bool=False):
        self.title=title
        self.author=author
        self.is_borrowd=is_borrowd
    def __str__(self):
        if self.is_borrowd == False:
            status="Avaiable"
            return f"'{self.title}' by {self.author} ({status})"
        else:
            status ="Borrowed"  
            return f"'{self.title}' by {self.author} ({status})" 



book1=Book("Harry pottery","harry",False)
print(book1)

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,books_name):
        self.books.append(books_name)
    def borrow_book(self,title):
        self.title=title
        for book in self.books:
           if book.title == title:
               if book.is_borrowd == True:
                   print(f"sorry {title} is already borrowed  ")
               else:
                   book.is_borrowd = True
                   print(f"Book is avaiable {title} borrowd  successfully ")
               return

        print(f"{title} is not found sorry ")
    def return_book(self,title):
        for book in self.books:
            if book.title == title:
             if book.is_borrowd==True:
                book.is_borrowd=False
                print(f"{title} is successfully return ")
            return
    
mylibaray=Library()
print(mylibaray.books)
mylibaray.add_book(book1)
print(mylibaray.books[0])


mylibaray.borrow_book("Harry pottery")
print(book1)

mylibaray.return_book("Harry pottery")
print(book1)

