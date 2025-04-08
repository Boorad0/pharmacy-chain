from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSizePolicy, QStackedWidget

class MainWindow(QWidget):
    def __init__(self, stacked_widget, database):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        with open("main/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.setWindowTitle("Меню")
        self.setContentsMargins(0,0,0,0)
        btns = ["Товары", "Поставки", "Продажи","Потавщики","Сотрудники","Отчеты","UML Диаграмма","Администрирование"]
        
    
        self.create_menu_objects()
        self.set_object_name()
        
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.menu_widget.setLayout(self.menu_layout)
        self.pixmap = self.pixmap.scaled(50, 50)  
        self.label_photo.setPixmap(self.pixmap)
        self.label_username.setText("Даниил")
        self.label_menu.setText("Меню")
        self.menu_layout.addWidget(self.label_photo)
        self.menu_layout.addWidget(self.label_username)
        self.menu_layout.addWidget(self.label_line_1)
        self.menu_layout.addWidget(self.label_menu)
        self.initialization(btns)
        self.menu_layout.addWidget(self.label_line_2)
        self.initialization(["Выход"])
        self.menu_layout.addStretch()
        self.main_layout.addWidget(self.menu_widget)

        self.stack = QStackedWidget()
        self.page = QWidget()
        self.page.setContentsMargins(0,0,0,0)
        self.stack.setContentsMargins(0,0,0,0)
        self.stack.addWidget(self.page)
        self.main_layout.addWidget(self.stack)

    def create_menu_objects(self):
        self.main_layout = QHBoxLayout(self)
        self.menu_layout = QVBoxLayout(self)
        self.menu_widget = QWidget(self)
        self.label_photo = QLabel()
        self.label_username = QLabel()
        self.label_line_1 = QLabel()
        self.label_line_2 = QLabel()
        self.label_menu = QLabel()
        self.pixmap = QPixmap("photo/user-octagon-svgrepo-com.svg")

    def set_object_name(self):
        self.menu_widget.setObjectName("menu_widget")
        self.label_photo.setObjectName("label_photo")
        self.label_username.setObjectName("label_username")
        self.label_line_1.setObjectName("label_line_1")
        self.label_line_2.setObjectName("label_line_2")
        self.label_menu.setObjectName("label_menu")

    def initialization(self, btns):
        for btn in btns:
            button = MenuButton(btn)
            button.clicked.connect(self.button_clicked)  # Подключение сигнала нажатия кнопки
            self.menu_layout.addWidget(button)
    def button_clicked(self):
        button = self.sender()  # Получаем кнопку, которая вызвала сигнал
        print(f"Нажата кнопка: {button}") 
        if button.text() == "Выход":
            self.button_exit()
        
    def button_exit(self):
        self.stacked_widget.setMinimumSize(QtCore.QSize(280,385))
        self.stacked_widget.setMaximumSize(QtCore.QSize(960, 540))
        self.stacked_widget.resize(960,540)
        self.stacked_widget.setCurrentIndex(0)
        
        
class MenuButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
       
