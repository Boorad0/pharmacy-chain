from getpass import getpass
from mysql.connector import connect, Error
class BD:
    def __init__(self):
        self.status = False
    def authorization(self, login, password):
        try:
            DataBase=  connect(
            host="localhost",
            user=login,
            password=password,
            database="online_movie_rating",
            auth_plugin='mysql_native_password'
            )
            self.DataBase = DataBase
            
            self.cursor = DataBase.cursor()
            self.status = True
        except Error as e:
            self.status = False
    def read_table_data(self):
        select_movies_query = "SELECT * FROM movies LIMIT 5"
        self.cursor.execute(select_movies_query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)  