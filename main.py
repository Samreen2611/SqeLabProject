from auth import register, login
from library import view_books, search_book, borrow_book, return_book
from admin import add_book, remove_book, view_users, view_transactions

while True:

    print("\n===== LIBRARY SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        user = login()

        if user:

            while True:

                print("\n===== USER MENU =====")
                print("1. View Books")
                print("2. Search Book")
                print("3. Borrow Book")
                print("4. Return Book")
                print("5. Add Book")
                print("6. Remove Book")
                print("7. View Users")
                print("8. View Transactions")
                print("9. Logout")

                c = input("Enter choice: ")

                if c == "1":
                    view_books()

                elif c == "2":
                    search_book()

                elif c == "3":
                    borrow_book(user)

                elif c == "4":
                    return_book(user)

                elif c == "5":
                    add_book()

                elif c == "6":
                    remove_book()

                elif c == "7":
                    view_users()

                elif c == "8":
                    view_transactions()

                elif c == "9":
                    print("Logging out...")
                    break   # 🔥 IMPORTANT FIX

                else:
                    print("Invalid choice!")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid option!")