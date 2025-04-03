

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
class MainWindow(QWidget):
    def __init__(self, stacked_widget,database):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Главное окно")
        self.database = database
        # Элементы главного окна
        self.label = QLabel("Добро пожаловать в главное окно!", self)
        self.back_button = QPushButton("Выйти", self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
        
        # Назад в окно авторизации
        self.print_db()
            
    def print_db(self):
        self.back_button.clicked.connect(self.jj)
    def jj(self):
        self.database.read_table_data()