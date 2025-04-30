from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSizePolicy, QStackedWidget,QLineEdit, QComboBox, QTableWidget,QTableWidgetItem,QHeaderView
class Product_page(QWidget):
    def __init__(self, DateBase):
        super().__init__()
        self.delete_items=[]
        self.database = DateBase
        
        self.__create_objects()
        self.__add_object_text()
        self.__add_object_name()
        self.__set_privilege()
        self.__load_btns()
        self.__add_to_page()
        self.__set_styleSheet()

    def __set_styleSheet(self):
        with open("main/products/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.table_product.setMinimumWidth(800)
        self.table_product.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.label_products.setAlignment(Qt.AlignCenter) 

    def __create_objects(self):
        self.product_layout = QVBoxLayout(self)
        self.add_window = QWidget()
        self.label_products = QLabel()
        self.tool_line = QHBoxLayout()
        self.editline_search=QLineEdit()
        self.btn_search = QPushButton()
        self.btn_update = QPushButton()
        self.btn_edit=QPushButton()
        self.btn_add = QPushButton()
        self.add_window_layout = QVBoxLayout()
        self.add_window_table=QTableWidget()
        self.add_window_label = QLabel()
        self.table_product = QTableWidget()
        self.add_window_button = QPushButton()
        self.add_window_error_label = QLabel()
    def __set_privilege(self):
        if self.database.role != "admin":
            self.btn_edit.hide()
    def __add_object_name(self):
        self.btn_add.setObjectName("btn_add")
        self.btn_edit.setObjectName("btn_edit")
        self.product_layout.setObjectName("product_layout")
        self.label_products.setObjectName("label_products")
        self.tool_line.setObjectName("tool_line")
        self.editline_search.setObjectName("editline_search")
        self.btn_search.setObjectName("btn_search")
        self.btn_update.setObjectName("btn_update")
        self.table_product.setObjectName("table_product")

    def __add_to_page(self):
        self.tool_line.addWidget(self.editline_search)
        self.tool_line.addWidget(self.btn_search)
        self.tool_line.addWidget(self.btn_update)
        self.tool_line.addWidget(self.btn_edit)
        self.tool_line.addWidget(self.btn_add)
        self.product_layout.addWidget(self.label_products)
        self.product_layout.addLayout(self.tool_line)
        self.product_layout.addWidget(self.table_product)
        self.btn_add.hide()
        
    def __add_object_text(self):
        self.label_products.setText("Товары")
        self.btn_search.setText("Поиск")
        self.btn_update.setText("Обновить")
        self.btn_edit.setText("Редактировать")
        self.btn_add.setText("Добавить")
        self.add_window_label.setText("Введите товар")
        self.add_window_button.setText("Добавить")
        self.add_window_error_label.setText("")

    def __load_btns(self):
        self.table_product.itemChanged.connect(self.on_item_changed)
        self.table_product.blockSignals(True)
        self.btn_update.clicked.connect(self.load_data_from_db)
        self.btn_edit.clicked.connect(self.table_edit)
        self.btn_add.clicked.connect(self.table_add)
        self.add_window_button.clicked.connect(self.add_new_row)
        self.btn_search.clicked.connect(self.search_item)

    def search_item(self):
        search_info = self.editline_search.text()
        if search_info !="":
            results = self.database.search_products(name=search_info)
            self.table_product.setRowCount(len(results))
            for row in range(len(results)):
                for item in range(0,5):
                    self.table_product.setItem(row,item, QTableWidgetItem(str(results[row][item])))
            self.table_product.viewport().update()
        
        
        
        
        
    def add_new_row(self):
        self.add_window_error_label.setText("")
        try:
            if self.database.add_product(
                self.add_window_table.item(0,0).text(),
                self.add_window_table.item(0,1).text(),
                self.add_window_table.item(0,2).text(),
                self.add_window_table.item(0,3).text()):
                    self.load_data_from_db(editable=False)
                    self.load_data_from_db(editable=True)
                    self.add_window_table.clearContents()
            else:
                self.add_window_table.clearContents()
                self.add_window_error_label.setText("Данные введены некорректно!")
        except:
            self.add_window_table.clearContents()
            self.add_window_error_label.setText("Данные введены некорректно!")
    

    def table_add(self):
        if hasattr(self, 'add_window') and self.add_window.isVisible():
            self.add_window.raise_()
            self.add_window.activateWindow()
            return
        
        
        self.add_window.resize(500, 200)
        self.add_window.setWindowTitle("Добавление товара")
        self.add_window_table.setRowCount(1)
        self.add_window_table.setColumnCount(4)
        self.add_window_table.setHorizontalHeaderLabels(["Наименование", "Производитель", "Срок годности", "Количество"])
        self.add_window_table.verticalHeader().setVisible(False)
        
        self.add_window_layout.addWidget(self.add_window_label)
        self.add_window_layout.addWidget(self.add_window_table)
        self.add_window_layout.addWidget(self.add_window_error_label)
        self.add_window_layout.addWidget(self.add_window_button)
        self.add_window.setLayout(self.add_window_layout)
        self.add_window.show()

    def table_edit(self):
        
        if self.btn_edit.text() == "Сохранить":
            self.table_product.blockSignals(True)
            self.load_data_from_db(editable=False)
            self.add_window.hide()
            self.btn_add.hide()
            
            self.btn_edit.setText("Редактировать")
            self.btn_update.show()
            
        elif self.btn_edit.text() == "Редактировать":
            self.load_data_from_db(editable=True)
            self.table_product.blockSignals(False)
            self.btn_add.show()
            
            self.btn_edit.setText("Сохранить")
            self.btn_update.hide()
    

    def load_data_from_db(self, editable=False):
        
        self.table_product.setSortingEnabled(False)
        self.table_product.setRowCount(0)
        self.table_product.setColumnCount(0)
        rows = self.database.return_row()

        if not rows:
            return

        self.table_product.setRowCount(len(rows))
        if editable:self.table_product.setColumnCount(len(rows[0])+1)
        else:self.table_product.setColumnCount(len(rows[0]))
            
        self.table_product.setHorizontalHeaderLabels(["Id", "Наименование", "Производитель", "Срок годности", "Количество", "Удалить строку"])
        self.table_product.verticalHeader().setVisible(False)

        for row_idx, row in enumerate(rows):
            for col_idx in range(len(row)):
                cell = row[col_idx]
                item = QTableWidgetItem(str(cell))

                if col_idx == 0 or not editable:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                self.table_product.setItem(row_idx, col_idx, item)

            if editable and self.table_product.columnCount() > 5:
                btn_delete = QPushButton()
                btn_delete.setObjectName("btn_delete")
                btn_delete.setText("")
                btn_delete.setContentsMargins(0, 0, 0, 0)
                btn_delete.clicked.connect(self.table_row_delete)
                    
                self.table_product.setCellWidget(row_idx, 5, btn_delete)
        self.table_product.setSortingEnabled(True)
        self.table_product.resizeColumnsToContents()

    def on_item_changed(self, item):
        row = item.row()
        col = item.column()
        new_value = item.text()
        id_value = self.table_product.item(row, 0).text()
        self.database.update_column_by_id(product_id=id_value, column_id=col, new_value=new_value)
        
    def table_row_delete(self):
        button = self.sender()
        if button:
            index = self.table_product.indexAt(button.pos())
            row = index.row()
            product_id = self.table_product.item(row, 0).text()
            self.database.delete_product_by_id(product_id)
            self.table_product.removeRow(row)
        
        