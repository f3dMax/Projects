#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author: Maksym Fedenko
# CIST2110-001-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:
import csv
# Project outline and requirements:

# OUTLINE - The LMS will consist of the following classes and methods:

# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. ISBN (int)
#    b. Title (string)
#    c. Author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Book:
    def __init__(self, isbn: int, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.borrowed = False
# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
#    b. checkout - sets borrowed to True and returns a message that the book has been checked out
#    c. checkin - sets borrowed to False and returns a message that the book has been checked in
#    d. isBorrowed - returns True if the book is borrowed and False if the book is not borrowed
    def __str__(self) -> str:
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"

    def checkout(self) -> str:
        self.borrowed = True
        return f"{self.title} has been checked out"

    def checkin(self) -> str:
        self.borrowed = False
        return f"{self.title} has been checked in"

    def isBorrowed(self) -> bool:
        return self.borrowed


# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. Name (string)
#    c. ID (int)
#    d. borrowedBooks (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
#    b. borrow_book - adds the book to the borrowedBooks list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
#    c. return_book - removes the book from the borrowedBooks list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)
class User:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id
        self.borrowedBooks = []

    def __str__(self) -> str:
        borrowed_books_titles = ', '.join([book.title for book in self.borrowedBooks])
        return f"Name: {self.name}, ID: {self.user_id}, Borrowed Books: {borrowed_books_titles}"

    def borrow_book(self, book: Book) -> str:
        self.borrowedBooks.append(book)
        book.checkout()
        return f"{book.title} has been checked out by {self.name}"

    def return_book(self, book: Book) -> str:
        self.borrowedBooks.remove(book)
        book.checkin()
        return f"{book.title} has been checked in by {self.name}"

# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
#    b. add_book - adds a book to the books list (should take a book as a parameter)
#    c. add_user - adds a user to the users list (should take a user as a parameter)
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def __str__(self) -> str:
        book_titles = ', '.join([book.title for book in self.books])
        user_names = ', '.join([user.name for user in self.users])
        return f"Books: {book_titles}, Users: {user_names}"

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def find_book(self, isbn: int) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_user(self, user_id: int) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def export_books_to_csv(self, filename: str):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ISBN', 'Title', 'Author', 'Borrowed'])
            writer.writeheader()
            for book in self.books:
                writer.writerow({'ISBN': book.isbn, 'Title': book.title, 'Author': book.author, 'Borrowed': book.borrowed})

    def export_users_to_csv(self, filename: str):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'ID', 'Borrowed Books'])
            writer.writeheader()
            for user in self.users:
                borrowed_books_titles = ', '.join([book.title for book in user.borrowedBooks])
                writer.writerow({'Name': user.name, 'ID': user.user_id, 'Borrowed Books': borrowed_books_titles})


def add_book(library: Library):
    # Your code to add a book
    pass

def add_user(library: Library):
    # Your code to add a user
    pass

def delete_book(library: Library):
    # Your code to delete a book
    pass

def delete_user(library: Library):
    # Your code to delete a user
    pass

def borrow_book(library: Library):
    # Your code for a user to borrow a book
    pass

def return_book(library: Library):
    # Your code for a user to return a book
    pass

def search_books(library: Library):
    # Your code to search for books
    pass

def check_book_availability(library: Library):
    # Your code to check book availability
    pass

def search_users(library: Library):
    # Your code to search for users
    pass

def export_books_to_csv(library: Library):
    # Your code to export books to CSV
    pass

def export_users_to_csv(library: Library):
    # Your code to export users to CSV
    pass

# 4. Create a menu that will allow users to:
#    a. Add books
#    b. Add users
#    c. Delete books
#    d. Delete users
#    g. Borrow books
#    h. Return books
#    i. Search books
#    j. Check if book is available
#    k. Search users
#    l. Export books to csv
#    m. Export users to csv
#    z. Exit
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Delete Book")
        print("4. Delete User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Search Books")
        print("8. Check Book Availability")
        print("9. Search Users")
        print("10. Export Books to CSV")
        print("11. Export Users to CSV")
        print("0. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                add_book(library)
            elif choice == '2':
                add_user(library)
            elif choice == '3':
                delete_book(library)
            elif choice == '4':
                delete_user(library)
            # Add remaining choices here
            elif choice == '0':
                print("Exiting the Library Management System.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

def add_book(library: Library):
    try:
        isbn = int(input("Enter ISBN: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        library.add_book(Book(isbn, title, author))
        print(f"Book '{title}' added to the library.")
    except ValueError:
        print("Invalid input. Please enter a valid ISBN.")

def add_user(library: Library):
    try:
        name = input("Enter Name: ")
        user_id = int(input("Enter User ID: "))
        library.add_user(User(name, user_id))
        print(f"User '{name}' added to the library.")
    except ValueError:
        print("Invalid input. Please enter a valid User ID.")

def delete_book(library: Library):
    try:
        isbn = int(input("Enter ISBN of the book to delete: "))
        book = library.find_book(isbn)
        if book:
            library.books.remove(book)
            print(f"Book with ISBN {isbn} deleted.")
        else:
            print("Book not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ISBN.")

def delete_user(library: Library):
    try:
        user_id = int(input("Enter User ID to delete: "))
        user = library.find_user(user_id)
        if user:
            library.users.remove(user)
            print(f"User with ID {user_id} deleted.")
        else:
            print("User not found.")
    except ValueError:
        print("Invalid input. Please enter a valid User ID.")

def borrow_book(library: Library):
    try:
        user_id = int(input("Enter your User ID: "))
        isbn = int(input("Enter ISBN of the book to borrow: "))
        user = library.find_user(user_id)
        book = library.find_book(isbn)
        if user and book and not book.isBorrowed():
            user.borrow_book(book)
            print(f"Book '{book.title}' borrowed by user '{user.name}'.")
        else:
            print("Unable to borrow book. Book may not exist or is already borrowed.")
    except ValueError:
        print("Invalid input. Please enter valid details.")

def return_book(library: Library):
    try:
        user_id = int(input("Enter your User ID: "))
        isbn = int(input("Enter ISBN of the book to return: "))
        user = library.find_user(user_id)
        book = library.find_book(isbn)
        if user and book and book in user.borrowedBooks:
            user.return_book(book)
            print(f"Book '{book.title}' returned by user '{user.name}'.")
        else:
            print("Unable to return book. Make sure the book was borrowed by you.")
    except ValueError:
        print("Invalid input. Please enter valid details.")

def search_books(library: Library):
    try:
        isbn = int(input("Enter ISBN to search: "))
        book = library.find_book(isbn)
        if book:
            print(book)
        else:
            print("Book not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ISBN.")

def check_book_availability(library: Library):
    try:
        isbn = int(input("Enter ISBN to check availability: "))
        book = library.find_book(isbn)
        if book:
            availability = "available" if not book.isBorrowed() else "currently borrowed"
            print(f"Book '{book.title}' is {availability}.")
        else:
            print("Book not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ISBN.")

def search_users(library: Library):
    try:
        user_id = int(input("Enter User ID to search: "))
        user = library.find_user(user_id)
        if user:
            print(user)
        else:
            print("User not found.")
    except ValueError:
        print("Invalid input. Please enter a valid User ID.")

def export_books_to_csv(library: Library):
    filename = input("Enter filename to export books: ")
    library.export_books_to_csv(filename)
    print(f"Books data exported to {filename}")

def export_users_to_csv(library: Library):
    filename = input("Enter filename to export users: ")
    library.export_users_to_csv(filename)
    print(f"Users data exported to {filename}")

# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 11)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.

# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?



      # Remove this line when you implement this method


if __name__ == "__main__":
    main()
