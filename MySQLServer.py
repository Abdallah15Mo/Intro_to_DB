#!/usr/bin/env python3
import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server (update credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

