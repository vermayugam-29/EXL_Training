import mysql.connector
from mysql.connector import Error

def initialize_database():
    try:
        mySQlDb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "yugam123",
        )

        cursor = mySQlDb.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS exl_churn_db")
        print("✅Database exl_churn_db created")

        mySQlDb.database = 'exl_churn_db'

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            CustomerID VARCHAR(20) PRIMARY KEY,
            Gender VARCHAR(10),
            Age INT,
            Tenure INT,
            Balance FLOAT,
            NumOfProducts INT,
            HasCrCard INT,
            IsActiveMember INT,
            EstimatedSalary FLOAT,
            Churn INT
        )
        """)

        mySQlDb.commit()
        cursor.close()
        mySQlDb.close()

    except Error as e:
        print(f'Error : {e}')


def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="yugam123",
            database="exl_churn_db",
        )
    except Error as e:
        print(f"❌ Connection Error: {e}")
        return None