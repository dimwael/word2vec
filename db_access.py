import os
from getpass import getpass
import bcrypt
import sqlite3
from sqlite3 import OperationalError

def authenticate(username):
    query = "SELECT password FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        return bcrypt.checkpw(getpass("Enter password: ").encode(), result[0])
    else:
        return False

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password BYTEA)")
except OperationalError as e:
    print(f"Error creating table: {e}")
    
if __name__ == "__main__":
    username = input("Enter username: ")
    if authenticate(username):
        print("Authentication successful")
    else:
        print("Invalid username or password")
