from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QSpinBox, QTableWidget, QTableWidgetItem, QMessageBox,
    QLineEdit, QDialog, QHeaderView
)
from PyQt5.QtCore import Qt

class SalesWindow(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setMinimumSize(800, 500)
        self.selected_products = {}
        self.__create_objects()
        self.__add_object_name()
        self.__add_to_page()
        self.__setup_connections()
        self.__set_styleSheet()
        self.load_products()
        

    def __create_objects(self):
        self.layout = QVBoxLayout()
        self.search_layout = QHBoxLayout()
        self.title_label = QLabel("Продажи")
        self.search_line = QLineEdit()
        self.search_button = QPushButton("Поиск")
        self.update_button = QPushButton("Обновить таблицу")
        self.sell_button = QPushButton("Перейти к продаже")
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Название", "Производитель", "Срок годности", "Количество", "Добавить"])
        

    def __add_object_name(self):
        self.title_label.setObjectName("title_label")
        self.search_line.setObjectName("search_line")
        self.search_button.setObjectName("search_button")
        self.update_button.setObjectName("update_button")
        self.sell_button.setObjectName("sell_button")
        self.table.setObjectName("table")

    def __set_styleSheet(self):
        with open("main/sales/ui/style_SalesWindow.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.title_label.setAlignment(Qt.AlignCenter) 
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.search_line.setPlaceholderText("Введите название товара")
        self.table.setSortingEnabled(True)

    def __add_to_page(self):
        self.layout.addWidget(self.title_label)
        self.search_layout.addWidget(self.search_line)
        self.search_layout.addWidget(self.search_button)
        self.search_layout.addWidget(self.update_button)
        self.search_layout.addWidget(self.sell_button)
        self.layout.addLayout(self.search_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def __setup_connections(self):
        self.search_button.clicked.connect(self.search_product)
        self.update_button.clicked.connect(self.load_products)
        self.sell_button.clicked.connect(self.open_selected_products_window)

    def load_products(self):
        self.table.setRowCount(0)
        self.table.verticalHeader().setVisible(False)
        rows = self.database.return_row()

        for row_data in rows:
            self._insert_row(row_data)

    def search_product(self):
        search_text = self.search_line.text().strip()
        if not search_text:
            return

        self.table.setRowCount(0)
        rows = self.database.search_products(name=search_text)

        if not rows:
            return

        for row_data in rows:
            self._insert_row(row_data)

    def _insert_row(self, row_data):
        row_number = self.table.rowCount()
        self.table.insertRow(row_number)

        for column_number, data in enumerate(row_data):
            item = QTableWidgetItem(str(data))
            if column_number in (0, 4):  # ID и Количество по центру
                item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_number, column_number, item)

        add_button = QPushButton()
        
        add_button.clicked.connect(lambda checked, data=row_data: self.add_product(data))
        self.table.setCellWidget(row_number, 5, add_button)

    def add_product(self, row_data):
        product_id = row_data[0]
        if product_id not in self.selected_products:
            self.selected_products[product_id] = {
                "name": row_data[1],
                "manufacturer": row_data[2],
                "expiry": row_data[3],
                "quantity": row_data[4],
                "sell_quantity": 1
            }
        else:
            QMessageBox.information(self, "Информация", f"Товар '{row_data[1]}' уже добавлен.")

    def open_selected_products_window(self):
        if not self.selected_products:
            QMessageBox.warning(self, "Ошибка", "Выберите товары для продажи.")
            return

        dialog = SelectedProductsDialog(self.selected_products, self.database)
        dialog.exec_()

        self.selected_products.clear()
        self.load_products()

class SelectedProductsDialog(QDialog):
    def __init__(self, selected_products, database):
        super().__init__()
        self.selected_products = selected_products
        self.database = database
        self.setWindowTitle("Продажа выбранных товаров")
        self.__create_objects()
        self.__add_to_page()
        self.__add_object_name()
        self.__set_styleSheet()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Название", "Производитель", "Остаток", "Количество", ""])
        self.populate_table()
        self.sell_button.clicked.connect(self.sell_products)

    def __create_objects(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel("Выбранные товары")
        self.table = QTableWidget()
        self.sell_button = QPushButton("Подтвердить продажу")

    def __add_to_page(self):
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.sell_button)
        self.setLayout(self.layout)

    def __add_object_name(self):
        self.setObjectName("add_window")
        self.title_label.setObjectName("titile_label")
        self.table.setObjectName("table")
        self.sell_button.setObjectName("sell_button")

    def __set_styleSheet(self):
        with open("main/sales/ui/style_SelectedProductDialog.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.table.horizontalHeader().setStretchLastSection(True)
        self.setMinimumSize(700, 400)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def populate_table(self):
        self.table.setRowCount(0)
        for idx, (product_id, info) in enumerate(self.selected_products.items()):
            self.table.insertRow(idx)
            self.table.setItem(idx, 0, QTableWidgetItem(info["name"]))
            self.table.setItem(idx, 1, QTableWidgetItem(info["manufacturer"]))
            self.table.setItem(idx, 2, QTableWidgetItem(str(info["quantity"])))
            spinbox = QSpinBox()
            spinbox.setMinimum(1)
            spinbox.setMaximum(info["quantity"])
            spinbox.setValue(info["sell_quantity"])
            self.table.setCellWidget(idx, 3, spinbox)

            remove_button = QPushButton("Удалить")
            remove_button.setObjectName("btn_delete")
            remove_button.clicked.connect(lambda checked, row=idx: self.remove_row(row))
            self.table.setCellWidget(idx, 4, remove_button)

    def remove_row(self, row):
        product_name = self.table.item(row, 0).text()
        product_id = None
        for pid, info in self.selected_products.items():
            if info["name"] == product_name:
                product_id = pid
                break
        if product_id:
            del self.selected_products[product_id]
        self.table.removeRow(row)

    def sell_products(self):
        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text()
            for product_id, info in self.selected_products.items():
                if info["name"] == name:
                    spinbox = self.table.cellWidget(row, 3)
                    sell_quantity = spinbox.value()
                    new_quantity = info["quantity"] - sell_quantity
                    self.database.update_column_by_id(product_id=product_id, column_id=4, new_value=new_quantity)

        QMessageBox.information(self, "Успех", "Операция выполнена!")
        self.accept()
