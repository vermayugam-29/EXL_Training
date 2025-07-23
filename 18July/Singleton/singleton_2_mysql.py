import mysql.connector

class DBConnector:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating DBConnector object...")
            cls._instance = super(DBConnector, cls).__new__(cls)
            cls._instance.connect()
        return cls._instance

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yugam123",
            database="exl"
        )
        self.cursor = self.connection.cursor()
        print("MySQL Connection established successfully!")

    def get_cursor(self):
        return self.cursor
