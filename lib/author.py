import sqlite3
from __init__ import CONN, CURSOR

class Author:
    def __init__(self, name):
        self._name = name
        self.id = None

    def __repr__(self):
        return f"AUTHOR name: {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance (value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError ("Name must contain at least 3 characters.")


    @classmethod
    def _from_db_row(cls, row):
        author = cls(row[1])
        author.id = row[0]
        return author
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM authors WHERE name = ?", (name,))
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
        
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM authors")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, name):
        existing = cls.find_by_name(name)
        if existing:
            return existing[0]
        author = cls(name)
        author.save()
        return author
    
    def update(self):
        CURSOR.execute("UPDATE authors SET name = ? WHERE id = ?", (self._name, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM authors WHERE id = ?", (self.id,))
        CONN.commit()

    def books(self):
        

    
    def save(self):
        try:
            CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self._name,))
            CONN.commit()
            self.id = CURSOR.lastrowid
        except sqlite3.IntegrityError:
            print("Error: An author with this names may already exist.")
    

    
