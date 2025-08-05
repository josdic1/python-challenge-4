import sqlite3
from __init__ import CONN, CURSOR

class Reader:

    all = []

    def __init__(self, name):
        self._name = name
        self.id = None

    def __repr__(self):
        return f"READER name: {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance (value, str) and 0 < len(value) <= 15:
            self._name = value
        else:
            raise ValueError ("Reader name cannot be blank and cannot exceed 15 characters")
        

    @classmethod
    def _from_db_row(cls, row):
        reader = cls(row[1])
        reader.id = row[0]
        return reader
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM readers WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM readers WHERE name = ?", (name,))
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM readers")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, name):
        existing = cls.find_by_name(name)
        if existing:
            return existing[0]
        reader = cls(name)
        reader.save()
        return reader
    
    def books(self):
        from lib.book import Book
        CURSOR.execute("SELECT * FROM borrowings WHERE reader_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        book_list = [row[2] for row in rows]
        return [Book.find_by_id(book_id) for book_id in book_list]

    def update(self):
        CURSOR.execute("UPDATE readers SET name = ? WHERE id = ?", (self._name, self.id,))
        CONN.commit()


    def delete(self):
        CURSOR.execute("DELETE FROM readers WHERE id = ?", (self.id,))
        CONN.commit()

    
    def save(self):
        try:
            CURSOR.execute("INSERT INTO readers (name) VALUES (?)", (self._name,))
            CONN.commit()
            self.id = CURSOR.lastrowid
        except sqlite3.IntegrityError:
            print ("Error: A reader with this name may already exist.")
