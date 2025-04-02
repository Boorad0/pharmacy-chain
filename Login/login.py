from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow,QWidget
from Login.ui.style import Style
class AppLogin(QMainWindow):
    def __init__(self,stacked_widget):
        super(AppLogin,self).__init__()
        self.stacked_widget = stacked_widget
        self.stacked_widget.setWindowTitle("Аптека")
        self.stacked_widget.resize(800, 600)
        self.stacked_widget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.Title_txt = QtWidgets.QLabel(self.centralwidget)
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_place = QtWidgets.QTextEdit(self.centralwidget)
        self.password_place = QtWidgets.QTextEdit(self.centralwidget)
        self.Login_txt = QtWidgets.QLabel(self.centralwidget)
        self.Password_txt = QtWidgets.QLabel(self.centralwidget)
        self.Login_status = QtWidgets.QLabel(self.centralwidget)
        self.title_font = QtGui.QFont()
        self.login_font = self.password_font = QtGui.QFont()

        Style.setDefaultText(self)
        Style.objectname_settings(self)
        Style.geometry_settings(self)
        Style.font_settings(self)
        Style.apply_styles(self)
        
        self.authorization()  

    
    def authorization(self):
        self.login_btn.clicked.connect(self.login)

    def login(self):
        username = self.login_place.toPlainText()
        password = self.password_place.toPlainText()

        if username == "admin" and password == "1234":
            self.Login_status.setText("Успешный вход!")
            self.Login_status.setStyleSheet("color: green;")
            self.password_place.clear()
            self.stacked_widget.setCurrentIndex(1) 
            

            
            
        else:
            self.Login_status.setText("Ошибка входа!")
            self.Login_status.setStyleSheet("color: red;")
    
    
    
