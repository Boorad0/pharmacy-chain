from getpass import getpass
from mysql.connector import connect, Error
from datetime import datetime
class BD:
    def __init__(self,login=None,password=None):
        self.column_names = ["id", "name", "manufacturer", "expiration_date", "quantity"]
        self.status = False
        self.login = login
        self.password = password
        
        
    def authorization(self):
        try:
            DataBase=  connect(
            host="localhost",
            user="boorado",#self.login=
            password="12345678",#self.password=
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
    
    
    def update_column_by_id(self, product_id, column_id, new_value):
        """
        Обновляет значение указанной колонки по ID товара.
        :param product_id: ID товара
        :param column_name: имя колонки, которую нужно изменить ('name', 'manufacturer', 'expiration_date', 'quantity')
        :param new_value: новое значение для указанной колонки
        """
        try:
            self.cursor.execute("USE pharmacy_chain")

            # Проверка, существует ли товар с таким ID
            self.cursor.execute("SELECT * FROM product_table WHERE id = %s", (product_id,))
            self.cursor.fetchone()
            query = f"UPDATE product_table SET {self.column_names[column_id]} = %s WHERE id = %s"
            self.cursor.execute(query, (new_value, product_id))
            self.DataBase.commit()

        except Error as e:
            print(f"Ошибка при обновлении данных: {e}")
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
            return True
        except Error as e:
            return False
    

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
                
                return results
            else:
                return []

        except Error as e:
            print(f"Ошибка при поиске: {e}")
    
    def delete_product_by_id(self, product_id):
        """
        Удаляет товар по ID.
        :param product_id: ID товара, который нужно удалить
        """
        try:
            self.cursor.execute("USE pharmacy_chain")
            self.cursor.execute("SELECT * FROM product_table WHERE id = %s", (product_id,))
            row = self.cursor.fetchone()
            self.cursor.execute("DELETE FROM product_table WHERE id = %s", (product_id,))
            self.DataBase.commit()
            
        except Error as e:
            print(f"Ошибка при удалении: {e}")
    def log_sale_to_reports(self, product_id, sold_quantity):
        """
        Добавляет запись о продаже в таблицу reports.
        :param product_id: ID проданного товара
        :param sold_quantity: Количество проданных единиц
        """
        try:
            self.cursor.execute("USE pharmacy_chain")

            # Получаем информацию о товаре по ID
            self.cursor.execute("SELECT name, manufacturer, expiration_date, quantity FROM product_table WHERE id = %s", (product_id,))
            result = self.cursor.fetchone()

            if not result:
                print(f"Товар с ID {product_id} не найден.")
                return False

            name, manufacturer, expiration_date, current_quantity = result

            # ➕ Проверка: не добавлять в отчёт, если товара изначально нет
            if current_quantity == 0:
                print(f"Товар '{name}' (ID {product_id}) отсутствует на складе — не добавлен в отчёт.")
                return False

            sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            insert_query = """
            INSERT INTO reports (name, manufacturer, expiration_date, quantity, sale_date, sold_quantity)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(insert_query, (
                name,
                manufacturer,
                expiration_date,
                current_quantity,
                sale_date,
                sold_quantity
            ))
            self.DataBase.commit()

            # ➕ Выводим подтверждение в консоль
            print(f"Продажа товара '{name}' (ID {product_id}) успешно добавлена в отчёт.")
            return True

        except Error as e:
            print(f"Ошибка при добавлении в отчет: {e}")
            return False
