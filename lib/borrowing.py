from __init__ import CONN, CURSOR
from lib.reader import Reader
from lib.book import Book

class Borrowing:

    all = []

    def __init__(self, reader_id, book_id):
        self.reader_id = reader_id
        self.book_id = book_id
        self.id = None

    def __repr__(self):
        return f"Borrowing | reader_id: {self.reader.id} book_id: {self.book.id}"
    

    