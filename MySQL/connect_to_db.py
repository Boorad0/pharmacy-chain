from getpass import getpass
from mysql.connector import connect, Error
from datetime import date
class BD:
    def __init__(self,login=None,password=None):
        self.status = False
        self.login = login
        self.password = password
        
        
    def authorization(self):
        try:
            DataBase=  connect(
            host="localhost",
            user=self.login,
            password=self.password,
            database="pharmacy_chain",
            auth_plugin='mysql_native_password'
            )
            self.DataBase = DataBase
            self.cursor = self.DataBase.cursor()
            
            self.status = True
        except Error as e:
            self.status = False
    
    def return_row(self):
        self.authorization()
        
        self.cursor.execute("SELECT * FROM product_table")
        rows = self.cursor.fetchall()
        return rows
    
    

    def add_product(self, name, manufacturer, expiration_date, quantity):
        """
        Добавляет новый продукт в таблицу product_table.
        :param name: название продукта
        :param manufacturer: производитель
        :param expiration_date: дата окончания срока годности (в формате 'YYYY-MM-DD')
        :param quantity: количество на складе
        """
        try:
            self.cursor.execute("USE pharmacy_chain")
            insert_query = """
            INSERT INTO product_table (name, manufacturer, expiration_date, quantity)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(insert_query, (name, manufacturer, expiration_date, quantity))
            self.DataBase.commit()
            print("Товар успешно добавлен.")
        except Error as e:
            print(f"Ошибка при добавлении товара: {e}")
    def print_product_row(self, row):
        """
        Удобный вывод строки из таблицы product_table.
        :param row: кортеж из SELECT-запроса (id, name, manufacturer, expiration_date, quantity)
        """
        id_, name_, manuf_, exp_date, qty = row
        if isinstance(exp_date, date):
            exp_date = exp_date.strftime("%Y-%m-%d")
        print(f"ID: {id_}, Название: {name_}, Производитель: {manuf_}, Срок годности: {exp_date}, Кол-во: {qty}")

    def search_products(self, name=None, quantity=None, manufacturer=None, expiration_date=None):
        try:
            self.cursor.execute("USE pharmacy_chain")
            query = "SELECT * FROM product_table WHERE 1=1"
            params = []

            if name is not None:
                query += " AND name LIKE %s"
                params.append(f"%{name}%")

            if quantity is not None:
                query += " AND quantity = %s"
                params.append(quantity)

            if manufacturer is not None:
                query += " AND manufacturer LIKE %s"
                params.append(f"%{manufacturer}%")

            if expiration_date is not None:
                query += " AND expiration_date = %s"
                params.append(expiration_date)

            self.cursor.execute(query, tuple(params))
            results = self.cursor.fetchall()

            if results:
                print("Найденные товары:")
                for row in results:
                    self.print_product_row(row)
            else:
                print("Совпадений не найдено.")

        except Error as e:
            print(f"Ошибка при поиске: {e}")
    def show_all_products(self):
        """
        Показывает все товары в таблице product_table.
        """
        try:
            self.cursor.execute("USE pharmacy_chain")
            self.cursor.execute("SELECT * FROM product_table")
            results = self.cursor.fetchall()

            if results:
                print("Все товары в базе данных:")
                for row in results:
                    self.print_product_row(row)
            else:
                print("Таблица пуста.")
        except Error as e:
            print(f"Ошибка при получении данных: {e}")
    def delete_product_by_id(self, product_id):
        """
        Удаляет товар по ID.
        :param product_id: ID товара, который нужно удалить
        """
        try:
            self.cursor.execute("USE pharmacy_chain")

            # Проверка, существует ли товар с таким ID
            self.cursor.execute("SELECT * FROM product_table WHERE id = %s", (product_id,))
            row = self.cursor.fetchone()
            if row:
                self.print_product_row(row)
                confirm = input("Удалить этот товар? (y/n): ").strip().lower()
                if confirm == 'y':
                    self.cursor.execute("DELETE FROM product_table WHERE id = %s", (product_id,))
                    self.DataBase.commit()
                    print("Товар удалён.")
                else:
                    print("Удаление отменено.")
            else:
                print("Товар с таким ID не найден.")
        except Error as e:
            print(f"Ошибка при удалении: {e}")
