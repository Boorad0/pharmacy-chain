from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import mysql.connector
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSizePolicy, QStackedWidget,QLineEdit, QComboBox, QTableWidget,QTableWidgetItem
import time
class Product_page(QWidget):
    def __init__(self, DateBase):
        super().__init__()
        
        self.database = DateBase
        
        self.__create_objects()
        self.__add_text()
        self.__add_object_name()
        self.__load_btns()
        self.__add_to_page()
        self.__set_styleSheet()
    def __load_btns(self):
        self.table_product.itemChanged.connect(self.on_item_changed)
        self.table_product.blockSignals(True)
        self.btn_update.clicked.connect(self.load_data_from_db)
        self.btn_edit.clicked.connect(self.table_edit)
    def table_edit(self):
        
        if self.btn_edit.text() == "Сохранить":
            self.table_product.blockSignals(True)
            self.load_data_from_db(editable=False)
            self.btn_edit.setText("Редактировать")
            
        elif self.btn_edit.text() == "Редактировать":
            self.load_data_from_db(editable=True)
            self.table_product.blockSignals(False)
            self.btn_edit.setText("Сохранить")
            
    def __set_styleSheet(self):
        with open("main/products/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())
    def __create_objects(self):
        self.product_layout = QVBoxLayout(self)
        
        self.label_products = QLabel()
        self.tool_line = QHBoxLayout()
        self.editline_search=QLineEdit()
        self.btn_search = QPushButton()
        self.btn_update = QPushButton()
        self.btn_edit=QPushButton()
        self.comboBox_filter = QComboBox()
        self.table_product = QTableWidget()
    def __add_object_name(self):
        self.btn_edit.setObjectName("btn_edit")
        self.product_layout.setObjectName("product_layout")
        self.label_products.setObjectName("label_products")
        self.tool_line.setObjectName("tool_line")
        self.editline_search.setObjectName("editline_search")
        self.btn_search.setObjectName("btn_search")
        self.btn_update.setObjectName("btn_update")
        self.comboBox_filter.setObjectName("comboBox_filter")
        self.table_product.setObjectName("table_product")
    def __add_to_page(self):
        self.tool_line.addWidget(self.editline_search)
        self.tool_line.addWidget(self.btn_search)
        self.tool_line.addWidget(self.btn_update)
        self.tool_line.addWidget(self.btn_edit)
        self.tool_line.addWidget(self.comboBox_filter)

        self.product_layout.addWidget(self.label_products)
        self.product_layout.addLayout(self.tool_line)
        self.product_layout.addWidget(self.table_product)
    def __add_text(self):
        self.label_products.setText("Товары")
        self.btn_search.setText("Поиск")
        self.btn_update.setText("Обновить")
        self.btn_edit.setText("Редактировать")






    def load_data_from_db(self, editable=False):
        try:
            # Подключение к базе данных MySQL с использованием mysql.connector
            
            self.table_product.setRowCount(0)
            self.table_product.setColumnCount(0)
            
            # Выполняем запрос для получения данных
            rows = self.database.return_row()
            # Устанавливаем количество строк и столбцов в QTableWidget
            self.table_product.setRowCount(len(rows))
            self.table_product.setColumnCount(len(rows[0]))

            # Устанавливаем заголовки столбцов
            self.table_product.setHorizontalHeaderLabels(["Id", "Наименование","Производитель", "Срок годности", "Количество"])
            self.table_product.verticalHeader().setVisible(0)
            # Заполняем таблицу данными
            for row_idx, row in enumerate(rows):
                for col_idx, cell in enumerate(row):
                    item = QTableWidgetItem(str(cell))
                    
                    # Первый столбец (ID) всегда нередактируемый
                    if col_idx == 0 or not editable:
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                    self.table_product.setItem(row_idx, col_idx, item)

            # Закрываем курсор
            

        except mysql.connector.Error as err:
            print(f"Ошибка при загрузке данных: {err}")
    def on_item_changed(self, item):
        row = item.row()
        col = item.column()
        new_value = item.text()

        # Получаем значение ID из первого столбца (предполагается, что ID всегда в колонке 0)
        id_item = self.table_product.item(row, 0)
        if id_item:  # проверка на случай, если ячейка пустая
            id_value = id_item.text()
        else:
            id_value = None

        print(f"Изменено значение в строке {row + 1}, колонке {col + 1}: {new_value}")
        print(f"ID измененной строки: {id_value}")