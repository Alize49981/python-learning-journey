{
  "gmail": "encrypted_password_here",
  "facebook": "encrypted_password_here"
}

#generate encription key
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

#load key
import os
def load_key():
    if not os.path.exists("secret.key"):
        print("key not found. generating new ones...")
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    
    
    return open("secret.key", "rb").read()

#initialize encriptor
key = load_key()
fernet = Fernet(key)

#Encrypt & Decrypt Functions
def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()

#save and load password
import json
import os

FILE_NAME = "passwords.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

#add new password
def add_password(data):
    account = input("Account name: ")
    password = input("Password: ")

    encrypted = encrypt_password(password)
    data[account] = encrypted

    print("Password saved securely!")

#view password
def view_password(data):
    account = input("Enter account name: ")

    if account in data:
        decrypted = decrypt_password(data[account])
        print(f"Password for {account}: {decrypted}")
    else:
        print("Account not found.")

#show all acounts
def list_accounts(data):
    if not data:
        print("No accounts stored.")
        return

    print("\nStored accounts:")
    for account in data:
        print("-", account)

#master password
MASTER_PASSWORD = "admin123"  

def authenticate():
    password = input("Enter master password: ")
    if password == MASTER_PASSWORD:
        return True
    else:
        print("Access denied!")
        return False
    
#main program
def main():
    if not authenticate():
        return

    data = load_data()

    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Password")
        print("3. List Accounts")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password(data)
        elif choice == "2":
            view_password(data)
        elif choice == "3":
            list_accounts(data)
        elif choice == "4":
            save_data(data)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        save_data(data)

if __name__ == "__main__":
    main()