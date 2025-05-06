import sqlite3

def setup_database():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Create table with image column
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        image TEXT
    )
    ''')

    # Clear table to avoid duplicates
    cursor.execute("DELETE FROM books")

    books_data = [
        ("As Long as the Lemon Trees Grow", "Zoulfa Katouh", "Historical Fiction", "lemon_trees.jpg"),
        ("A House Without Windows", "Nadia Hashimi", "Domestic Fiction", "house_without_windows.jpg"),
        ("Days at the Morisaki Bookshop", "Satoshi Yagisawa", "Fiction", "morisaki.jpg"),
        ("The Stationary Shop of Tehran", "Marjan Kamali", "Historical Fiction", "stationary_shop.jpg"),
        ("A Thousand Splendid Suns", "Khaled Hosseini", "Fiction", "splendid_suns.jpg"),
        ("Main Anmol", "Nemrah Ahmed", "Self help", "main_anmol.jpg"),
        ("Peer-e-Kamil", "Umaira Ahmed", "Spirituality", "peer_e_kamil.jpg"),
        ("Secrets of Divine Love", "A.Helwa", "Spirituality", "secrets_of_divine_love.jpg"),
        ("The Pearl that Broke its Shell", "Nadia Hashimi", "Domestic Fiction", "pearl_shell.jpg")
    ]
    cursor.executemany("INSERT INTO books (title, author, genre, image) VALUES (?, ?, ?, ?)", books_data)

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect("books.db")

