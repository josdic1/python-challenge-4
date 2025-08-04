import sqlite3
from __init__ import CONN, CURSOR

class Reader:
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
            raise ValueError ("name already exists")
        

    @classmethod
    def _from_db_row(cls, row):
        reader = cls(row[1])
        reader.id = row[0]
        return reader
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM readers WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM readers WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls._from_db_row(row)
        else:
            return None
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM readers")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []