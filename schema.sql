
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id) 
);

CREATE TABLE IF NOT EXISTS authors(
    id INTEGER PRIMARY KEY,
    name TEXT
);


CREATE TABLE IF NOT EXISTS readers(
    id INTEGER PRIMARY KEY,
    name TEXT
);

