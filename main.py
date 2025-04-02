import sys
from PyQt5.QtWidgets import QApplication
from logic import AppLogic

def application():
    app = QApplication(sys.argv)
    logic = AppLogic()  # Создаем объект логики, который запускает окно
    logic.run()  # Запускаем приложение
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()