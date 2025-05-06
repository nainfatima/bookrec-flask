# bookrec.py
import sqlite3
from book_db import get_connection

def recommend_by_genre(selected_title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT genre FROM books WHERE LOWER(title)=?",
        (selected_title.lower(),)
    )
    row = cursor.fetchone()
    if not row:
        return []                   # was string before, now empty list
    genre = row[0]
    cursor.execute(
        "SELECT title, image FROM books WHERE genre=? AND LOWER(title)!=?",
        (genre, selected_title.lower())
    )
    recs = cursor.fetchall()       # stays a list of tuples
    conn.close()
    return recs                     # even if recs is empty, we return []
    
def recommend_by_author(selected_title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT author FROM books WHERE LOWER(title)=?",
        (selected_title.lower(),)
    )
    row = cursor.fetchone()
    if not row:
        return []
    author = row[0]
    cursor.execute(
        "SELECT title, image FROM books WHERE author=? AND LOWER(title)!=?",
        (author, selected_title.lower())
    )
    recs = cursor.fetchall()
    conn.close()
    return recs

