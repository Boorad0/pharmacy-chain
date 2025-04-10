
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow,QWidget,QLineEdit
from Login.ui.style import Style
class AppLogin(QMainWindow):
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
        self.stacked_widget.resize(960, 540)
        self.stacked_widget.setMaximumSize(QtCore.QSize(960, 540))
        self.stacked_widget.setMinimumSize(QtCore.QSize(280,385))
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
        self.database.login = username
        self.database.password = password
        self.database.authorization()
        if self.database.status:
            print(self.database)
            self.password_place.clear()
            self.label_wrong_data.setText("")  
            self.stacked_widget.resize(1440, 810)
            self.stacked_widget.setCurrentIndex(1) 
            self.stacked_widget.setMinimumSize(1440,810)
            self.stacked_widget.setMaximumSize(1920,1080)
            self.stacked_widget.setGeometry(10,40,0,0)
            self.stacked_widget.showFullScreen

        else:
            self.label_wrong_data.setText("Неверный логин или пароль")  
            self.password_place.clear()
    
    
