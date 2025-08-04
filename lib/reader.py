from __init__ import CONN, CURSOR

class Reader:
    def __init__(self, name):
        self._name = name
        self.id = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance (value, str) and 0 < len(value) <= 15:
            self._name = value
        else:
            raise ValueError ("name already exists")