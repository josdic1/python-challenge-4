import sqlite3
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
            raise ValueError ("Title must be a string and at least 2 characters long.")
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance (value, str) and value.strip():
            self._author = value
        else:
            raise ValueError ("Author must be a non-empty string.")
        
    @classmethod
    def _from_db_row(cls, row):
        book = cls(row[1], row[2])
        book.id = row[0]
        return book
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM books WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def find_by_title(cls, title):
        CURSOR.execute("SELECT * FROM books WHERE title = ?", (title,))
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM books")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, title, author):
        existing = cls.find_by_title(title)
        if existing:
            return existing[0]
        book = cls(title, author)
        book.save()
        return book
    
    def update(self):
        CURSOR.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (self._title, self._author, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM books WHERE id = ?", (self.id,))
        CONN.commit()

    def save(self):
        try:
            CURSOR.execute("INSERT INTO books (title, author) VALUES (?,?)", (self._title, self._author))
            CONN.commit()
            self.id = CURSOR.lastrowid
        except sqlite3.IntegrityError:
            print("Error: A book with this title may already exist.")


    


