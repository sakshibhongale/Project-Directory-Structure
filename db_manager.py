import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_books_table)
    except sqlite3.Error as e:
        print(e)

def add_book(conn, title, author, year):
    sql = ''' INSERT INTO books(title, author, year)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, (title, author, year))
        conn.commit()
        print(f"Book '{title}' added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")

def search_books(conn, title):
    sql = ''' SELECT * FROM books WHERE title=? '''
    cur = conn.cursor()
    cur.execute(sql, (title,))
    rows = cur.fetchall()
    return rows
