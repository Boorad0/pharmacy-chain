from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QStackedWidget
class MainWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Главное окно")

        # Элементы главного окна
        self.label = QLabel("Добро пожаловать в главное окно!", self)
        self.back_button = QPushButton("Выйти", self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

        # Назад в окно авторизации
        self.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))