from database import load_data, save_data


BOOKS_FILE = 'books.json'
USERS_FILE = 'users.json'
TRANSACTIONS_FILE = 'transactions.json'


# Add Book

def add_book():

    books = load_data(BOOKS_FILE)

    book_id = int(input("Enter book ID: "))
    title = input("Enter title: ")
    author = input("Enter author: ")
    quantity = int(input("Enter quantity: "))

    books.append({
        'id': book_id,
        'title': title,
        'author': author,
        'quantity': quantity
    })

    save_data(BOOKS_FILE, books)
    print("Book added successfully!")


# Remove Book

def remove_book():

    books = load_data(BOOKS_FILE)

    book_id = int(input("Enter book ID to remove: "))

    for book in books:

        if book['id'] == book_id:

            books.remove(book)
            save_data(BOOKS_FILE, books)

            print("Book removed successfully!")
            return

    print("Book not found!")


# View Users

def view_users():
     users = load_data(USERS_FILE)
     print("\nRegistered Users")
     for user in users:
        print(user['username'])


# View Transactions

def view_transactions():

    transactions = load_data(TRANSACTIONS_FILE)

    print("\nTransaction Records")

    for transaction in transactions:
        print(transaction)

