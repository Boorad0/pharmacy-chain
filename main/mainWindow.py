from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSizePolicy, QStackedWidget
from main.products.product_page import Product_page
from main.sales.sales_page import SalesWindow
from main.reports.reports_page import ReportsWindow
class MainWindow(QWidget):
    def __init__(self, stacked_widget, database):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.database = database
        
        self.__create_objects()
        self.__add_object_name()
        self.__add_object_text()
        self.__add_to_page()
        self.__add_styles()

    def __add_styles(self):
        with open("main/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.setContentsMargins(0,0,0,0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.pixmap = self.pixmap.scaled(50, 50)  
        self.label_photo.setPixmap(self.pixmap)
        self.menu_layout.addStretch()
        self.product_page.setContentsMargins(0,0,0,0)
        self.stack.setContentsMargins(0,0,0,0)

    def __add_to_page(self):
        self.menu_widget.setLayout(self.menu_layout)
        self.menu_layout.addWidget(self.label_photo)
        self.menu_layout.addWidget(self.label_username)
        self.menu_layout.addWidget(self.label_line_1)
        self.menu_layout.addWidget(self.label_menu)
        self.initialization(["Товары", "Поставки", "Продажи","Поставщики","Сотрудники","Отчеты","Администрирование"])
        self.menu_layout.addWidget(self.label_line_2)
        self.initialization(["Выход"])
        self.main_layout.addWidget(self.menu_widget)
        self.stack.addWidget(self.clear_page)
        self.stack.addWidget(self.product_page)
        self.stack.addWidget(self.sales_page)
        self.stack.addWidget(self.report_page)
        self.main_layout.addWidget(self.stack)

    def __create_objects(self):
        self.main_layout = QHBoxLayout(self)
        self.menu_layout = QVBoxLayout()
        self.menu_widget = QWidget()
        self.label_photo = QLabel()
        self.label_username = QLabel()
        self.label_line_1 = QLabel()
        self.label_line_2 = QLabel()
        self.label_menu = QLabel()
        self.pixmap = QPixmap("photo/user-octagon-svgrepo-com.svg")
        self.stack = QStackedWidget()
        self.clear_page=QWidget()
        self.product_page = Product_page(self.database)
        self.sales_page = SalesWindow(self.database)
        self.report_page = ReportsWindow(self.database)

    def __add_object_name(self):
        self.menu_widget.setObjectName("menu_widget")
        self.label_photo.setObjectName("label_photo")
        self.label_username.setObjectName("label_username")
        self.label_line_1.setObjectName("label_line_1")
        self.label_line_2.setObjectName("label_line_2")
        self.label_menu.setObjectName("label_menu")

    def __add_object_text(self):
        self.label_username.setText("Даниил")
        self.label_menu.setText("Меню")

    def initialization(self, btns):
        for btn in btns:
            button = QPushButton()
            button.setText(btn)
            button.clicked.connect(self.button_clicked)  # Подключение сигнала нажатия кнопки
            self.menu_layout.addWidget(button)
            
    def button_clicked(self):
        button = self.sender()  # Получаем кнопку, которая вызвала сигнал
        
        if button.text() == "Выход":
            self.button_exit()
        if button.text() == "Товары":
            self.stack.setCurrentIndex(1)
        if button.text() == "Продажи":
            self.stack.setCurrentIndex(2)
        if button.text() == "Отчеты":
            self.stack.setCurrentIndex(3)
            
        
    def button_exit(self):
        self.stacked_widget.setMinimumSize(QtCore.QSize(280,385))
        self.stacked_widget.setMaximumSize(QtCore.QSize(960, 540))
        self.stacked_widget.resize(960,540)
        self.stacked_widget.setCurrentIndex(0)
        self.product_page.add_window.hide()
        
