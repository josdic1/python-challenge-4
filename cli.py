from __init__ import CONN, CURSOR
from lib.author import Author
from lib.book import Book
from lib.reader import Reader
from lib.borrowing import Borrowing

reader = Reader.find_by_id(1)
print(reader.books())
















