
import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QStackedWidget,QWidget
from Login.login import AppLogin
from main.mainWindow import MainWindow
from MySQL.connect_to_db import BD


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        database= BD()
        self.stacked_widget = QStackedWidget()
        self.auth_window = AppLogin(self.stacked_widget, database)
        self.main_window = MainWindow(self.stacked_widget, database)

        self.stacked_widget.addWidget(self.auth_window)
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.setCurrentIndex(0)

        # --- создаем реальное окно
        self.main_widget = QWidget()
        
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.addWidget(self.stacked_widget)

        self.main_widget.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinMaxButtonsHint | QtCore.Qt.WindowCloseButtonHint)
        self.main_widget.setWindowTitle("Аптека")
        self.main_widget.resize(960, 540)
        self.main_widget.show()
        

       
    
if __name__ == "__main__":
    app = App(sys.argv) 
    sys.exit(app.exec_())     