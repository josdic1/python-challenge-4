from __init__ import CONN, CURSOR

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.id = None

    def __repr__(self):
        return f"BOOK title: {self.title} | author: {self.author}"
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance (value, str) and len(value) >= 2:
            self._title = value
        else:
            raise ValueError ("title already exists")
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance (value, str) and value.strip():
            self._author = value
        else:
            raise ValueError ("author already exists")
        
    @classmethod
    def _from_db_row(cls, row):
        book = cls(row[1], row[2])
        book.id = row[0]
        return book
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM books WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return row
    
    @classmethod
    def find_by_title(cls, title):
        CURSOR.execute("SELECT * FROM books WHERE title = ?", (title,))
        rows = CURSOR.fetchall()
        return rows
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM books")
        rows = CURSOR.lastrowid
        return rows
    


