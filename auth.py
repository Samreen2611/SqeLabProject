from database import load_data, save_data

USERS_FILE = "users.json"

def register():
    users = load_data(USERS_FILE)

    username = input("Enter username: ")
    password = input("Enter password: ")

    for u in users:
        if u["username"] == username:
            print("User already exists!")
            return

    users.append({"username": username, "password": password})
    save_data(USERS_FILE, users)

    print("Registration successful!")


def login():
    users = load_data(USERS_FILE)

    username = input("Enter username: ")
    password = input("Enter password: ")

    for u in users:
        if u["username"] == username and u["password"] == password:
            print("Login successful!")
            return username   # ✅ MUST RETURN USER

    print("Invalid credentials!")
    return None