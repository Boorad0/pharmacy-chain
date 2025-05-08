from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QHeaderView, QHBoxLayout, QDialog,
    QLineEdit, QComboBox, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt

class AddUserDialog(QDialog):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setWindowTitle("Добавить пользователя")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.role_select = QComboBox()
        self.role_select.addItems(["admin", "user"])

        form_layout = QFormLayout()
        form_layout.addRow("Имя пользователя:", self.username_input)
        form_layout.addRow("Пароль:", self.password_input)
        form_layout.addRow("Права:", self.role_select)

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_user)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.add_button)
        self.setLayout(layout)
        with open("main/admin/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())

    def add_user(self):
        name = self.username_input.text()
        password = self.password_input.text()
        role = self.role_select.currentText()

        if not name or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")
            return

        if self.database.add_user(name, password, role):
            QMessageBox.information(self, "Успех", "Пользователь добавлен.")
            self.accept()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось добавить пользователя.")


class AdminWindow(QWidget):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setWindowTitle("Администрирование")
        self.setMinimumSize(700, 400)

        self.layout = QVBoxLayout()
        self.title_label = QLabel("Управление пользователями")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.refresh_button = QPushButton("Обновить")
        self.add_user_button = QPushButton("Добавить пользователя")
        self.refresh_button.clicked.connect(self.load_users)
        self.add_user_button.clicked.connect(self.show_add_user_dialog)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.add_user_button)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Имя", "Роль", "Удалить"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)

        self.layout.addWidget(self.title_label)
        self.layout.addLayout(button_layout)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.title_label.setObjectName("title_label")
        with open("main/admin/ui/style.qss", "r") as file:
            self.setStyleSheet(file.read())
        self.load_users()

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
        self.dialog = AddUserDialog(self.database)
        if self.dialog.exec_():
            self.load_users()