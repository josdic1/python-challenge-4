
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