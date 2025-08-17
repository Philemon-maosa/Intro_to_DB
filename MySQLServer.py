# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying a database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",        
        password="Marcopolo"         
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    
    if 'cursor' in locals() and cursor.is_connected() is False:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
