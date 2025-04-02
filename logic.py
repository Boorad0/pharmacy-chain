from ui.window import Window

class AppLogic:
    def __init__(self):
        """Инициализация логики приложения."""
        self.window = Window()  # Создаем главное окно
        self.setup_logic()  # Настраиваем обработчики событий

    def setup_logic(self):
        """Настройка логики кнопок и других элементов."""
        self.window.login_btn.clicked.connect(self.login)

    def login(self):
        """Обрабатывает нажатие кнопки входа."""
        username = self.window.login_place.toPlainText()
        password = self.window.password_place.toPlainText()

        # Простая проверка (можно заменить на запрос к БД)
        if username == "admin" and password == "1234":
            self.window.Login_status.setText("Успешный вход!")
            self.window.Login_status.setStyleSheet("color: green;")
        else:
            self.window.Login_status.setText("Ошибка входа!")
            self.window.Login_status.setStyleSheet("color: red;")

    def run(self):
        """Запускает главное окно приложения."""
        self.window.show()