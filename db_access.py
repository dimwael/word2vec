import os
from dotenv import load_dotenv
import bcrypt
import sqlite3

# Load environment variables
load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

def hash_password(password):
    """Hash and salt password using bcrypt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def authenticate(username):
    """Authenticate user by checking hashed password"""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result:
        hashed_password = result[0]
        return bcrypt.checkpw(username.encode(), hashed_password.encode())
    return False

def create_user(username, password):
    """Create a new user with hashed password"""
    hashed = hash_password(password)
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Create users table if not exists
    conn = sqlite3.connect("app.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)") 
    conn.close()

    # Create admin user
    create_user("admin", DB_PASSWORD)

    # Authenticate user
    username = input("Username: ")
    if authenticate(username):
        print("Authentication successful")
    else:
        print("Authentication failed")
