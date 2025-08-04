
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
            raise ValueError ("name already exists")


    @classmethod
    def _from_db_row(cls, row):
        author = cls(row[1])
        author.id = row[0]
        return author
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM authors")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []