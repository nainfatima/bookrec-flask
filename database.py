import sqlite3

# Connect to SQLite (it creates books.db if it doesn't exist)
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create a books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL
)
''')

# Insert book records (run once to populate)
books_data = [
    ("As Long as the Lemon Trees Grow", "Zoulfa Katouh", "Historical Fiction"),
    ("A House Without Windows", "Nadia Hashimi", "Domestic Fiction"),
    ("Days at the Morisaki Bookshop", "Satoshi Yagisawa", "Fiction"),
    ("The Stationary Shop of Tehran", "Marjan Kamali", "Historical Fiction"),
    ("A Thousand Splendid Suns", "Khaled Hosseini", "Fiction"),
    ("Main Anmol", "Nemrah Ahmed", "Self help"),
    ("Peer-e-Kamil", "Umaira Ahmed", "Spirituality"),
    ("Secrets of Divine Love", "A.Helwa", "Spirituality"),
    ("The Pearl that Broke its Shell", "Nadia Hashimi", "Domestic Fiction"),
    ("Before the Coffee gets Cold", "Toshikazu Kawaguch", "Time Travel Fiction"),
    ("Before Your Memory Fades", "Toshikazu Kawaguch", "Time Travel Fiction")

]

cursor.executemany("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", books_data)

conn.commit()
conn.close()

print("✅ Database setup complete!")
