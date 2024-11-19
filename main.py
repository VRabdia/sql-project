import os
from dotenv import load_dotenv
import mysql
from mysql.connector import MySQLConnection

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
database = os.getenv("DATABASE")

try:
    cnx = MySQLConnection(user=user, password=password, host=host, database=database)
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    