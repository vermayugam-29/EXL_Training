import mysql.connector
from mysql.connector import Error

def initialize_database():
    try:
        mySQLdb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='yugam123'
        )
        cursor = mySQLdb.cursor()


        cursor.execute("CREATE DATABASE IF NOT EXISTS shopdb")
        print("✅ Database 'shopdb' checked/created.")


        mySQLdb.database = 'shopdb'


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price FLOAT NOT NULL,
                quantity INT NOT NULL
            )
        """)

        mySQLdb.commit()
        cursor.close()
        mySQLdb.close()

    except Error as e:
        print(f"❌ Error: {e}")
