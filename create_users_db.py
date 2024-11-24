import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Function to connect to the database
def get_db():
    return mysql.connector.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
    )


# Function to create the database if it doesn't exist
def create_database():
    db = mysql.connector.connect(
        user=os.getenv("USER"), password=os.getenv("PASSWORD"), host=os.getenv("HOST")
    )
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DATABASE')}")
    db.close()


# Function to create the users table
def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            role VARCHAR(255) NOT NULL
        )
        """
    )
    db.close()


# Function to insert a user into the database
def insert_user(username, password, role):
    # Hash the password using bcrypt
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Insert user into the database
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users_info (username, password_hash, role) VALUES (%s, %s, %s)",  # Updated table name to users_info
        (username, password_hash, role),
    )
    db.commit()
    db.close()
    print(f"User {username} added successfully!")


# Main function to create database, table, and add a user
def main():
    create_database()  # Create database if it doesn't exist
    create_table()  # Create table if it doesn't exist

    # Input user data
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (e.g., admin, user): ")

    # Insert user into the database
    insert_user(username, password, role)


if __name__ == "__main__":
    main()
