import sqlite3

def get_connection():
    return sqlite3.connect("books.db")

def recommend_by_genre(selected_title):
    conn = get_connection()
    cursor = conn.cursor()

    # Find the genre of the selected book
    cursor.execute(
        "SELECT genre FROM books WHERE LOWER(title)=?",
        (selected_title.lower(),)
    )
    row = cursor.fetchone()

    if not row:
        print(" Book not found.")
    else:
        genre = row[0]
        print(f"\n📖 Genre: {genre}")
        print("✨ Similar books in the same genre:")
        cursor.execute(
            "SELECT title FROM books WHERE genre=? AND LOWER(title)!=?",
            (genre, selected_title.lower())
        )
        recs = cursor.fetchall()
        if recs:
            for rec in recs:
                print("  ➤", rec[0])
        else:
            print("  No other books in this genre.")
    conn.close()

def recommend_by_author(selected_title):
    conn = get_connection()
    cursor = conn.cursor()

    # Find the author of the selected book
    cursor.execute(
        "SELECT author FROM books WHERE LOWER(title)=?",
        (selected_title.lower(),)
    )
    row = cursor.fetchone()

    if not row:
        print(" Book not found.")
    else:
        author = row[0]
        print(f"\n✍️ Author: {author}")
        print("✨ More books by this author:")
        cursor.execute(
            "SELECT title FROM books WHERE author=? AND LOWER(title)!=?",
            (author, selected_title.lower())
        )
        recs = cursor.fetchall()
        if recs:
            for rec in recs:
                print("  ➤", rec[0])
        else:
            print("   No other books by this author.")
    conn.close()

# ------------------ MAIN LOOP -------------------
while True:
    print("\n How would you like to get recommendations?")
    print(" 1. By Genre")
    print(" 2. By Author")
    print(" 3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice in ('1','2'):
        selected_title = input("🔎 Enter a book title: ").strip()
        if choice == '1':
            recommend_by_genre(selected_title)
        else:
            recommend_by_author(selected_title)
    elif choice == '3':
        print("\n Goodbye! Happy Reading!")
        break
    else:
        print("⚠️ Invalid choice. Please choose 1, 2, or 3.")
