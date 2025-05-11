from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QHeaderView, QHBoxLayout, QDialog,
    QLineEdit, QComboBox, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

class AddUserDialog(QDialog):
    user_added = pyqtSignal()
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.__create_objects()
        self.__add_to_page()
        self.__set_styleSheet()
        self.__load_btns()

    def __create_objects(self):
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.role_select = QComboBox()
        self.role_select.addItems(["admin", "user"])
        self.form_layout = QFormLayout()
        self.form_layout.addRow("Имя пользователя:", self.username_input)
        self.form_layout.addRow("Пароль:", self.password_input)
        self.form_layout.addRow("Права:", self.role_select)
        self.add_button = QPushButton("Добавить")
        self.layout = QVBoxLayout()

    def __add_to_page(self):
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.add_button)
        self.setLayout(self.layout)

    def __load_btns(self):
        self.add_button.clicked.connect(self.add_user)

    def __set_styleSheet(self):
        self.setWindowTitle("Добавить пользователя")
        self.password_input.setEchoMode(QLineEdit.Password)
        with open("main/admin/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())

    def add_user(self):
        name = self.username_input.text()
        password = self.password_input.text()
        role = self.role_select.currentText()

        if not name or not password:
            box = QMessageBox(self)
            box.setIcon(QMessageBox.Warning)
            box.setWindowTitle("Ошибка")
            box.setText("Заполните все поля.")
            box.setStandardButtons(QMessageBox.Ok)
            box.show()
            return

        if self.database.add_user(name, password, role):
            box = QMessageBox(self)
            box.setIcon(QMessageBox.Information)
            box.setWindowTitle("Успех")
            box.setText("Пользователь добавлен.")
            box.setStandardButtons(QMessageBox.Ok)
            box.show()
            self.user_added.emit()
            self.close()
        else:
            box = QMessageBox(self)
            box.setIcon(QMessageBox.Critical)
            box.setWindowTitle("Ошибка")
            box.setText("Не удалось добавить пользователя.")
            box.setStandardButtons(QMessageBox.Ok)
            box.show()

        

class AdminWindow(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.__create_objects()
        self.__add_object_name()
        self.__set_styleSheet()
        self.__add_to_page()
        self.__load_btns()
        self.load_users()

    def __set_styleSheet(self):
        self.title_label.setAlignment(Qt.AlignCenter)
        with open("main/admin/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())
    def __load_btns(self):
        self.refresh_button.clicked.connect(self.load_users)
        self.add_user_button.clicked.connect(self.show_add_user_dialog)

    def __add_to_page(self):
        self.dialog.user_added.connect(self.load_users)
        self.button_layout.addWidget(self.refresh_button)
        self.button_layout.addWidget(self.add_user_button)
        self.layout.addWidget(self.title_label)
        self.layout.addLayout(self.button_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def __add_object_name(self):
        self.title_label.setObjectName("title_label")
    def __create_objects(self):
        self.dialog = AddUserDialog(self.database)
        self.layout = QVBoxLayout()
        self.title_label = QLabel("Управление пользователями")
        self.refresh_button = QPushButton("Обновить")
        self.add_user_button = QPushButton("Добавить пользователя")
        self.button_layout = QHBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Имя", "Роль", "Удалить"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)

    def load_users(self):
        self.table.setRowCount(0)
        users = self.database.get_all_users()
        for row_index, user in enumerate(users):
            self.table.insertRow(row_index)
            for col_index, value in enumerate(user):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row_index, col_index, item)

            delete_button = QPushButton()
            delete_button.clicked.connect(lambda _, uid=user[0]: self.delete_user(uid))
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.addWidget(delete_button)
            button_layout.setAlignment(Qt.AlignCenter)
            button_layout.setContentsMargins(0, 0, 0, 0)

            self.table.setCellWidget(row_index, 3, button_widget)

    def delete_user(self, user_id):
        confirm = QMessageBox.question(self, "Подтвердите", f"Удалить пользователя ID {user_id}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.database.delete_user_by_id(user_id)
            self.load_users()

    def show_add_user_dialog(self):
        self.dialog.show()
        self.dialog.raise_()  
        self.dialog.activateWindow()