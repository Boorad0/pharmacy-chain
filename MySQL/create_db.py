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
    def create_users_table(self):
        """
        Создаёт таблицу `users` в базе данных `pharmacy_chain`, если она не существует.
        """
        try:
            self.cursor.execute("USE pharmacy_chain")
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(50) NOT NULL
            );
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Таблица `users` успешно создана или уже существует.")
        except Error as e:
            print(f"Ошибка при создании таблицы users: {e}")
    def add_user(self, username, password, role):
        """
        Добавляет нового пользователя в таблицу users.
        :param username: имя пользователя (уникальное)
        :param password: пароль (будет захеширован SHA-256)
        :param role: роль пользователя (например, 'admin', 'manager', 'user')
        """
        try:
            self.cursor.execute("USE pharmacy_chain")

            # Хешируем пароль
            

            insert_query = """
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, %s)
            """
            self.cursor.execute(insert_query, (username, password, role))
            self.connection.commit()
            print(f"Пользователь '{username}' успешно добавлен.")
            return True
        except Error as e:
            print(f"Ошибка при добавлении пользователя: {e}")
            return False
# Использование

database = CreateDB()
database.show_db()
database.add_user("user", "12345678", "user")

