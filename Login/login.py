
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow,QWidget,QLineEdit
from Login.ui.style import Style
class AppLogin(QMainWindow):
    login_signal = pyqtSignal()
    def __init__(self,stacked_widget,database):
        super(AppLogin,self).__init__()
        
        self.database = database
        self.stacked_widget = stacked_widget
        self.__create_objects()
        self.__set_styleSheet()
        self.authorization()  

    def __create_objects(self):
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_LoginToSystem = QtWidgets.QLabel(self.centralwidget)
        self.label_pharmacyChain = QtWidgets.QLabel(self.centralwidget)
        self.login_place = QtWidgets.QLineEdit(self.centralwidget)
        self.password_place = QtWidgets.QLineEdit(self.centralwidget)
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.label_wrong_data = QtWidgets.QLabel(self.centralwidget)
        
    def __set_styleSheet(self):
        self.stacked_widget.setWindowTitle("Аптека")
        self.stacked_widget.setMinimumSize(280, 385)
        
        self.centralwidget.setStyleSheet("\n"
        "background-color: rgb(49, 49, 49);")
        Style.label_set(self)
        Style.label_wrong_data_set(self)
        Style.label_LoginToSystem_set(self)
        Style.label_pharmacyChain_set(self)
        Style.login_place_set(self)
        Style.password_place_set(self)
        Style.login_btn_set(self)
        Style.label_login_set(self)
        Style.label_password_set(self)
    
    def authorization(self):
        self.login_btn.clicked.connect(self.login)
        

    def login(self):
        username = self.login_place.text()
        password = self.password_place.text()
        role = self.database.check_user_credentials(username, password)
        
    
        if role != None:
            self.login_signal.emit()
            self.password_place.clear()
            self.label_wrong_data.setText("")  
            self.stacked_widget.setCurrentIndex(1) 
           
        else:
            self.label_wrong_data.setText("Неверный логин или пароль")  
            self.password_place.clear()
    
    
