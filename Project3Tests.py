# Import Statments
import pytest
from Project3 import Book, User, Library

#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author: Maksym Fedenko
# CIST2110-001-Project-3 Library Management System (LMS) Test Cases


import pytest
from Project3 import Book, User, Library

# Test cases for the Book class
def test_book_creation():
    book = Book(1234567890, "Test Book", "Author Name")
    assert book.title == "Test Book"
    assert book.author == "Author Name"
    assert book.isbn == 1234567890
    assert not book.borrowed

def test_book_checkout():
    book = Book(1234567890, "Test Book", "Author Name")
    book.checkout()
    assert book.borrowed

def test_book_return():
    book = Book(1234567890, "Test Book", "Author Name")
    book.checkout()
    book.checkin()
    assert not book.borrowed

# Test cases for the User class
def test_user_creation():
    user = User("John Doe", 1)
    assert user.name == "John Doe"
    assert user.user_id == 1
    assert user.borrowedBooks == []

def test_user_borrow():
    user = User("John Doe", 1)
    book = Book(1234567890, "Test Book", "Author Name")
    user.borrow_book(book)
    assert book in user.borrowedBooks
    assert book.borrowed

def test_user_return():
    user = User("John Doe", 1)
    book = Book(1234567890, "Test Book", "Author Name")
    user.borrow_book(book)
    user.return_book(book)
    assert book not in user.borrowedBooks
    assert not book.borrowed

# Test cases for the Library class
def test_library_add_book():
    library = Library()
    book = Book(1234567890, "Test Book", "Author Name")
    library.add_book(book)
    assert book in library.books

def test_library_add_user():
    library = Library()
    user = User("John Doe", 1)
    library.add_user(user)
    assert user in library.users

def test_library_find_book():
    library = Library()
    book = Book(1234567890, "Test Book", "Author Name")
    library.add_book(book)
    found = library.find_book(1234567890)
    assert found == book

def test_library_find_user():
    library = Library()
    user = User("John Doe", 1)
    library.add_user(user)
    found_user = library.find_user(1)
    assert found_user == user
