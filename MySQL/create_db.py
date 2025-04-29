from mysql.connector import connect, Error
from datetime import datetime
class CreateDB:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_to_mysql()

    def connect_to_mysql(self):
        try:
            self.connection = connect(
                host="localhost",
                user="boorado",
                password="12345678",
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS pharmacy")
            self.connection.database = "pharmacy_chain"
        except Error as e:
            print("Ошибка подключения или создания базы данных:", e)

    def show_db(self):
        if self.cursor:
            try:
                self.cursor.execute("SHOW DATABASES")
                for db in self.cursor:
                    print(db)
            except Error as e:
                print("Ошибка при выполнении запроса:", e)
        else:
            print("Курсор не инициализирован — соединение не установлено.")
    def create_reports_table(self):
        if self.cursor:
            try:
                create_table_query = """
                CREATE TABLE IF NOT EXISTS reports (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    manufacturer VARCHAR(255),
                    expiration_date DATE,
                    quantity INT,
                    sale_date DATETIME,
                    sold_quantity INT
                )
                """
                self.cursor.execute(create_table_query)
                self.connection.commit()
                print("Таблица 'reports' успешно создана или уже существует.")
            except Error as e:
                print("Ошибка при создании таблицы 'reports':", e)
        else:
            print("Курсор не инициализирован — соединение не установлено.")

# Использование
database = CreateDB()
database.show_db()
database.create_reports_table()
