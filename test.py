import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
    QLabel, QStackedWidget, QSizePolicy
)
from PyQt5.QtCore import Qt


class MenuButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
            }
        """)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Красивое меню слева")
        self.setStyleSheet("background-color: #ecf0f1;")

        # Основной layout
       

        # ===== ЛЕВОЕ МЕНЮ =====
        

        

        # ===== ПРАВОЕ СОДЕРЖИМОЕ =====
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("""
            QLabel {
                font-size: 24px;
                color: #2c3e50;
                padding: 20px;
            }
        """)

        # Главная страница с несколькими кнопками
        self.page1 = QWidget()
        page1_layout = QVBoxLayout(self.page1)
        page1_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        welcome_label = QLabel("🏠 Добро пожаловать на главную страницу")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 24px;")

        action_btn1 = QPushButton("🔍 Найти что-то")
        action_btn2 = QPushButton("➕ Добавить элемент")
        action_btn3 = QPushButton("📊 Показать отчёты")

        for btn in (action_btn1, action_btn2, action_btn3):
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    padding: 10px 20px;
                    font-size: 16px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            btn.setFixedWidth(250)
            btn.setCursor(Qt.PointingHandCursor)

        page1_layout.addWidget(welcome_label)
        page1_layout.addSpacing(20)
        page1_layout.addWidget(action_btn1, alignment=Qt.AlignCenter)
        page1_layout.addWidget(action_btn2, alignment=Qt.AlignCenter)
        page1_layout.addWidget(action_btn3, alignment=Qt.AlignCenter)

        # Другие страницы
        self.page2 = QLabel("📄 Здесь будут документы")
        self.page3 = QLabel("⚙️ Настройки приложения")

        self.page2.setAlignment(Qt.AlignCenter)
        self.page3.setAlignment(Qt.AlignCenter)

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        main_layout.addWidget(self.stack)

        # Сигналы
        btn_page1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        btn_page2.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        btn_page3.clicked.connect(lambda: self.stack.setCurrentIndex(2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 500)
    window.show()
    sys.exit(app.exec_())
