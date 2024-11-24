import mysql.connector
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables for database connection
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
database = os.getenv("DATABASE")

# Predefined lists of names, genders, health history, etc.
first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hank']
last_names = ['Smith', 'Doe', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Wilson']
genders = ["Male", "Female"]
ages = list(range(18, 80))  # Age range from 18 to 79
weights = [random.uniform(50, 120) for _ in range(100)]  # Random weights between 50 and 120 kg
heights = [random.uniform(150, 200) for _ in range(100)]  # Random heights between 150 cm and 200 cm
health_histories = [
    "Healthy",
    "Diabetes",
    "Hypertension",
    "Asthma",
    "Allergies",
    "Heart Disease",
    "Arthritis",
    "Obesity",
    "Depression",
    "No significant health history"
]

# Function to connect to the database
def get_db():
    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database,
    )

# Function to create the database if it doesn't exist
def create_database():
    db = mysql.connector.connect(
        user=user,
        password=password,
        host=host
    )
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    db.close()

# Function to create the health_info table if it doesn't exist
def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS health_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            gender VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            weight FLOAT NOT NULL,
            height FLOAT NOT NULL,
            health_history VARCHAR(255) NOT NULL
        )
        """
    )
    db.close()

# Function to populate the health_info table with random data
def insert_health_data():
    db = get_db()
    cursor = db.cursor()

    # Populate health_info table with random values
    for i in range(100):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        gender = random.choice(genders)
        age = random.choice(ages)
        weight = random.choice(weights)
        height = random.choice(heights)
        health_history = random.choice(health_histories)

        cursor.execute(
            "INSERT INTO health_info (first_name, last_name, gender, age, weight, height, health_history) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, gender, age, weight, height, health_history)
        )

    db.commit()
    db.close()

# Main function to create database, table, and insert data
def main():
    create_database()  # Create database if it doesn't exist
    create_table()  # Create table if it doesn't exist
    insert_health_data()  # Insert random health data into the table

if __name__ == "__main__":
    main()
