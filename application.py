from PyQt5.QtCore import pyqtSignal
import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QStackedWidget,QWidget
from Login.login import AppLogin
from main.mainWindow import MainWindow
from MySQL.connect_to_db import BD


class App:
    def __init__(self):
        
        self.database= BD()

        self.stacked_widget = QStackedWidget()
        self.auth_window = AppLogin(self.stacked_widget, self.database)
        self.main_window = None

        self.stacked_widget.addWidget(self.auth_window)
        
        self.stacked_widget.setCurrentIndex(0)
        self.main_widget = QWidget()
        
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.addWidget(self.stacked_widget)

        self.main_widget.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint)
        self.main_widget.setWindowTitle("Аптека")
        self.main_widget.resize(960, 540)
        
        self.auth_window.login_signal.connect(self.create_main_window)
        if not self.is_test_mode():
            self.main_widget.show()  # Показываем окно только если не в тестовом режиме
    def is_test_mode(self):
        return hasattr(self, 'is_test') and self.is_test
    def create_main_window(self):
        if self.main_window:
            self.stacked_widget.removeWidget(self.main_window)
            self.main_window.deleteLater()
            self.main_window = None

        self.main_window = MainWindow(self.stacked_widget, self.database)
        self.main_window.logout_signal.connect(self.handle_logout)

        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.setCurrentWidget(self.main_window)
        self.stacked_widget.setMinimumSize(1440, 810)
        self.stacked_widget.setMaximumSize(1920, 1080)

    def handle_logout(self):
        # Удаляем текущее main window и возвращаемся к логину
        if self.main_window:
            self.stacked_widget.removeWidget(self.main_window)
            self.main_window.deleteLater()
            self.main_window = None

        self.stacked_widget.setCurrentWidget(self.auth_window)
        self.stacked_widget.setMinimumSize(280, 385)
        
        self.stacked_widget.resize(960, 540)

       
    
if __name__ == "__main__":
    qt_app = QtWidgets.QApplication(sys.argv)
    app = App()
    app.main_widget.show()
    sys.exit(qt_app.exec_())
