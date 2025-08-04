from __init__ import CONN, CURSOR

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.id = None
    
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
