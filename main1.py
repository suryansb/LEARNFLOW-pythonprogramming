from cryptography.fernet import Fernet
import json
import os
import base64

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.key = self.generate_key()
        self.passwords = {}

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt(self, data):
        cipher_suite = Fernet(self.key)
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, encrypted_data):
        cipher_suite = Fernet(self.key)
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data

    def save_password(self, category, website, username, password):
        if category not in self.passwords:
            self.passwords[category] = {}

        encrypted_password = self.encrypt(password)
        encrypted_password_str = base64.urlsafe_b64encode(encrypted_password).decode('utf-8')
        self.passwords[category][website] = {'username': username, 'password': encrypted_password_str}

    def get_password(self, category, website):
        if category in self.passwords and website in self.passwords[category]:
            encrypted_password_str = self.passwords[category][website]['password']
            encrypted_password = base64.urlsafe_b64decode(encrypted_password_str.encode('utf-8'))
            decrypted_password = self.decrypt(encrypted_password)
            return decrypted_password
        else:
            return None

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            key_str = base64.urlsafe_b64encode(self.key).decode('utf-8')
            json.dump({'key': key_str, 'passwords': self.passwords}, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.key = base64.urlsafe_b64decode(data['key'])
                self.passwords = data['passwords']

# Example usage:
master_password = input("Enter your master password: ")
password_manager = PasswordManager(master_password)

while True:
    print("\nOptions:")
    print("1. Store a new password")
    print("2. Retrieve an existing password")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        category = input("Enter the category: ")
        website = input("Enter the website: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        password_manager.save_password(category, website, username, password)
        print("Password stored successfully!")

    elif choice == '2':
        category = input("Enter the category: ")
        website = input("Enter the website: ")
        retrieved_password = password_manager.get_password(category, website)
        if retrieved_password:
            print("Retrieved password:", retrieved_password)
        else:
            print("Password not found.")

    elif choice == '3':
        # Save passwords to a file before exiting
        password_manager.save_to_file('passwords.json')
        print("Exiting. Passwords saved to 'passwords.json'.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
