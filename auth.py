import json
import hashlib
import os

class Auth:
    def __init__(self, user_file='data/users.json'):
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.user_file):
            return {}
        with open(self.user_file, 'r') as file:
            return json.load(file)

    def save_users(self):
        with open(self.user_file, 'w') as file:
            json.dump(self.users, file, indent=4)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if username in self.users:
            return False, "Username already exists."
        self.users[username] = self.hash_password(password)
        self.save_users()
        return True, "User registered successfully."

    def login(self, username, password):
        if username not in self.users:
            return False, "User does not exist."
        if self.users[username] != self.hash_password(password):
            return False, "Incorrect password."
        return True, "Login successful."

# Example usage
if __name__ == "__main__":
    auth = Auth()
    print(auth.register("testuser", "testpass"))
    print(auth.login("testuser", "testpass"))
