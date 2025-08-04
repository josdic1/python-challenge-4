import sqlite3
import os

DB_NAME = 'database.db'
SCHEMA_FILE = 'schema.sql'

def setup_database():
    """Initializes the database by creating tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        with open(SCHEMA_FILE, 'r') as file:
            sql_script = file.read()
            cursor.executescript(sql_script)
        print("Database tables created successfully!")
    except FileNotFoundError:
        print(f"Error: '{SCHEMA_FILE}' file not found. Database not set up.")
    finally:
        conn.commit()
        conn.close()


if not os.path.exists('databse.py'):
    setup_database()
    

CONN = sqlite3.connect('databse.py')
CURSOR = CONN.cursor()