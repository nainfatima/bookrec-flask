
books = [
    {"title": "As Long as the Lemon Trees Grow", "author": "Zoulfa Katouh", "genre": "Historical Fiction"},
    {"title": "A House Without Windows", "author": "Nadia Hashimi", "genre": "Domestic Fiction"},
    {"title": "Days at the Morisaki Bookshop", "author": "Satoshi Yagisawa", "genre": "Fiction"},
    {"title": "The Stationary Shop of Tehran", "author": "Marjan Kamali", "genre": "Historical Fiction"},
    {"title": "A Thousand Splendid Suns", "author": "Khaled Hosseini", "genre": "Fiction"},
    {"title": "Main Anmol", "author": "Nemrah Ahmed", "genre": "Self help"},
    {"title": "Peer–e–Kamil", "author": "Umaira Ahmed", "genre": "Spirituality"},
    {"title": "Secrets of Divine Love", "author": "A.Helwa", "genre": "Spirituality"},
    {"title": "The Pearl that Broke its Shell", "author": "Nadia Hashimi", "genre": "Domestic Fiction"}
]


while True:
    print("\n How would you like to get recommendations?")
    print(" 1. By Genre")
    print(" 2. By Author")
    print(" 3. Exit")

   
    choice = input("Enter your choice (1/2/3): ")

 
    if choice == '1':
        print("\nAvailable Books:")
        for book in books:
            print("–", book["title"])  # show all book titles

        selected_title = input("\n🔎 Enter a book title: ")

        selected_book = None
        for book in books:
            if book["title"].lower() == selected_title.lower():
                selected_book = book
                break

        
        if not selected_book:
            print("\n Book not found. Please type the title exactly as shown.")
        else:
           
            selected_genre = selected_book["genre"]
            print(f"\n Genre: {selected_genre}")
            print("✨ Similar books in the same genre:")

            for book in books:
              
                if book["genre"] == selected_genre and book["title"] != selected_book["title"]:
                    print("  ➤", book["title"])


    elif choice == '2':
        print("\nAvailable Books:")
        for book in books:
            print("–", book["title"]) 

        selected_title = input("\n Enter a book title: ")

        selected_book = None
        for book in books:
            if book["title"].lower() == selected_title.lower():
                selected_book = book
                break

        if not selected_book:
            print("\n Book not found. Please type the title exactly as shown.")
        else:
            selected_author = selected_book["author"]
            print(f"\n Author: {selected_author}")
            print("More books by this author:")

            for book in books:
                if book["author"] == selected_author and book["title"] != selected_book["title"]:
                    print("  ➤", book["title"])

    
    elif choice == '3':
        print("\n Goodbye! Happy Reading!")
        break

    #  If user types something wrong
    else:
        print("\n⚠️ Invalid choice. Please select 1, 2, or 3.")
