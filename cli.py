from __init__ import CONN, CURSOR
from lib.author import Author
from lib.book import Book
from lib.reader import Reader
from lib.borrowing import Borrowing


book = Book.find_by_id(1)
print(book.readers())

















