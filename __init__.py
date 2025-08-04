import sqlite3

CONN = sqlite3.connect('database.py')
CURSOR = CONN.cursor()