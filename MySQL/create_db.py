from getpass import getpass
from mysql.connector import connect, Error

class create_db:
    def __init__(self):
        try:
            DataBase=  connect(
            host="localhost",
            user="boorado",
            password="boorado",
            
            )
            self.DataBase = DataBase
            self.cursor = DataBase.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS pharmacy")
        except Error as e:
            print(e)
    def show_db(self):
        self.cursor.execute("SHOW DATABASES")
        for db in self.cursor:
            print(db)


database = create_db()
database.show_db()