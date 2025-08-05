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
    
    @property
    def reader_id(self):
        return self._reader_id
    
    @reader_id.setter
    def reader_id(self, value):
        if isinstance (value, int) and value > 0:
            self._reader_id = value
        else:
            raise ValueError("Input is missing or not an integer")
    
    @property
    def book_id(self):
        return self._book_id
    
    @book_id.setter
    def book_id(self, value):
        if isinstance (value, int) and value > 0:
            self._book_id = value
        else:
            raise ValueError("Input is missing or not an integer")
    
    @classmethod
    def find_by_reader_id(cls, reader_id):
        CURSOR.execute("SELECT * FROM borrowings WHERE reader_id =?", (reader_id,))
        rows = CURSOR.fetchall()
        return rows if rows else []
    
    @classmethod
    def find_by_book_id(cls, book_id):
        CURSOR.execute("SELECT * FROM boorrowings WHERE book_id = ?", (book_id,))
        rows = CURSOR.fetchall()
        return rows if rows else []
        
    @classmethod
    def add_new(cls, reader_id, book_id):
        CURSOR.execute("INSERT INTO borrowings (reader_id, book_id) VALUES (?,?)", (reader_id, book_id,))
        CONN.commit()

    

        
    

