from mysql.connector import connect, Error
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
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS pharmacy_chain")
            self.connection.database = "pharmacy_chain"
        except Error as e:
            print("Ошибка подключения или создания базы данных:", e)

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
            except Error as e:
                print("Ошибка при создании таблицы 'reports':", e)
        else:
            print("Курсор не инициализирован — соединение не установлено.")
    def create_users_table(self):
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
    def create_products_table(self):
    
        try:
            self.cursor.execute("USE pharmacy_chain")
            create_table_query = """
            CREATE TABLE IF NOT EXISTS product_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE,
                manufacturer VARCHAR(255) NOT NULL,
                expiration_date DATE, 
                quantity INT
            );
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
        except Error as e:
            print(f"Ошибка при создании таблицы product_table {e}")
    

database = CreateDB()
database.create_products_table()
database.create_reports_table()
database.create_users_table()

