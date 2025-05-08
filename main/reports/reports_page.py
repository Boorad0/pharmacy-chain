from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import Qt

class ReportsWindow(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.__create_objects()
        self.__add_object_name()
        self.__add_to_page()
        self.__load_buttons()
        self.__set_styleSheet()
        self.load_reports()

    def __create_objects(self):
        self.layout = QVBoxLayout()
        self.title_label = QLabel("Отчёты")
        self.refresh_button = QPushButton("Обновить")
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Название", "Производитель", "Срок годности",
            "Количество на момент продажи", "Дата продажи", "Продано"
        ])
        
    def __set_styleSheet(self):
        with open("main/reports/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.table.verticalHeader().setVisible(False)
        self.table.setSortingEnabled(True)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def __add_object_name(self):
        self.title_label.setObjectName("title_label")
        self.refresh_button.setObjectName("refresh_button")
        self.table.setObjectName("table")

    def __add_to_page(self):
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.refresh_button)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def __load_buttons(self):
        self.refresh_button.clicked.connect(self.load_reports)

    def load_reports(self):
        try:
            self.table.setRowCount(0)
            self.database.cursor.execute("USE pharmacy_chain")
            self.database.cursor.execute("SELECT name, manufacturer, expiration_date, quantity, sale_date, sold_quantity FROM reports")
            rows = self.database.cursor.fetchall()

            for row_data in rows:
                row_number = self.table.rowCount()
                self.table.insertRow(row_number)
                for col_index, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(row_number, col_index, item)
        except Exception as e:
            print(f"Ошибка при загрузке отчётов: {e}")