from database import load_data, save_data

BOOKS_FILE = 'books.json'
TRANSACTIONS_FILE = 'transactions.json'


# View Books
def view_books():
    books = load_data(BOOKS_FILE)

    print("\nAvailable Books")
    print("----------------------")

    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Quantity: {book['quantity']}")
        print("----------------------")


# Search Book
def search_book():

    books = load_data(BOOKS_FILE)
    keyword = input("Enter book title: ")

    found = False

    for book in books:
        if keyword.lower() in book['title'].lower():
            print(book)
            found = True

    if not found:
        print("Book not found!")


# Borrow Book
def borrow_book(username):

    books = load_data(BOOKS_FILE)
    transactions = load_data(TRANSACTIONS_FILE)

    try:
        book_id = int(input("Enter book ID to borrow: "))
    except:
        print("Invalid input!")
        return

    for book in books:
        if book['id'] == book_id:

            if book['quantity'] > 0:

                book['quantity'] -= 1

                transactions.append({
                    'user': username,
                    'book': book['title'],
                    'status': 'Borrowed'
                })

                save_data(BOOKS_FILE, books)
                save_data(TRANSACTIONS_FILE, transactions)

                print("Book borrowed successfully!")
                return

            else:
                print("Book out of stock!")
                return

    print("Book not found!")


# Return Book
def return_book(username):

    books = load_data(BOOKS_FILE)
    transactions = load_data(TRANSACTIONS_FILE)

    try:
        book_id = int(input("Enter book ID to return: "))
    except:
        print("Invalid input!")
        return

    for book in books:
        if book['id'] == book_id:

            book['quantity'] += 1

            transactions.append({
                'user': username,
                'book': book['title'],
                'status': 'Returned'
            })
            def view_books():
                books = load_data(BOOKS_FILE)

    

    print("\nAvailable Books")
    save_data(BOOKS_FILE, books)
    save_data(TRANSACTIONS_FILE, transactions)
    print("Book returned successfully!")
    return

    print("Book not found!")