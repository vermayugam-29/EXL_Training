import mysql.connector
from mysql.connector import Error


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='yugam123',
        database='ecommercedb'
    )


def initialize_database():
    try:
        mySQLdb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='yugam123'
        )
        cursor = mySQLdb.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS ecommercedb")
        print("Database 'ecommercedb' created.")

        mySQLdb.database = 'ecommercedb'

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                price FLOAT NOT NULL,
                stock INT NOT NULL
            )
        """)

        mySQLdb.commit()
        cursor.close()
        mySQLdb.close()

    except Error as e:
        print(f"Error: {e}")
