# MySQLServer.py

import mysql.connector

try:
    # Connect to MySQL server (no database specified)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",       # Replace with your MySQL username
        password="Marcopolo"        # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
