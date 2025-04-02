
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QStackedWidget
from Login.login import AppLogin
from main.mainWindow import MainWindow

from PyQt5.QtWidgets import QMainWindow,QWidget
class default(QMainWindow):
    def __init__(self):
        super().__init__()

class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.stacked_widget = QStackedWidget()
        self.auth_window = AppLogin(self.stacked_widget)
        self.main_window = MainWindow(self.stacked_widget)
        self.stacked_widget.addWidget(self.auth_window)
        self.stacked_widget.addWidget(self.main_window)

        self.stacked_widget.setCurrentIndex(0)  # Начинаем с окна авторизации
        self.stacked_widget.show()
        


    
if __name__ == "__main__":
    app = App(sys.argv) 
    app.auth_window.show()
    sys.exit(app.exec_())     