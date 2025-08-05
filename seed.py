from lib.author import Author
from lib.book import Book
from lib.reader import Reader

# Authors
josh = Author.add_new("Josh")
maya = Author.add_new("Maya")

# Books
b1 = Book.add_new("Python Power", josh.id)
b2 = Book.add_new("Terminal Tactics", josh.id)
b3 = Book.add_new("Dream Data", maya.id)

# Readers
r1 = Reader.add_new("Dolby")
r2 = Reader.add_new("Sam")

