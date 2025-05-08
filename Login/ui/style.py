#кринге, надо переделать
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5 import QtWidgets, QtCore, QtGui
class Style(QMainWindow):
    def __init__(self):
        super().__init__()

    def label_set(self):
        self.label.setGeometry(QtCore.QRect(0, 0, 280, 1080))
        self.label.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
    def label_LoginToSystem_set(self):
        self.label_LoginToSystem.setText("Вход в систему управления базы данных")
        self.label_LoginToSystem.setGeometry(QtCore.QRect(20, 90, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_LoginToSystem.setFont(font)
        self.label_LoginToSystem.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_LoginToSystem.setMouseTracking(False)
        self.label_LoginToSystem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_LoginToSystem.setTextFormat(QtCore.Qt.AutoText)
        self.label_LoginToSystem.setWordWrap(True)
        self.label_LoginToSystem.setObjectName("label_LoginToSystem")
    def label_pharmacyChain_set(self):
        self.label_pharmacyChain.setText("Аптечная сеть")
        self.label_pharmacyChain.setGeometry(QtCore.QRect(20, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_pharmacyChain.setFont(font)
        self.label_pharmacyChain.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_pharmacyChain.setObjectName("label_pharmacyChain")
    def login_place_set(self):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.login_place.setFont(font)
        self.login_place.setGeometry(QtCore.QRect(20, 200, 241, 31))
        self.login_place.setStyleSheet("\n"
"background-color: rgb(239, 239, 239);")
        self.login_place.setFrame(False)
        self.login_place.setObjectName("login_place")
        
    def password_place_set(self):
        self.password_place.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_place.setGeometry(QtCore.QRect(20, 270, 241, 31))
        self.password_place.setStyleSheet("\n"
"background-color: rgb(239, 239, 239);")
        self.password_place.setFrame(False)
        self.password_place.setObjectName("password_place")
    def label_login_set(self):
        self.label_login.setText("Логин")
        self.label_login.setGeometry(QtCore.QRect(20, 170, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_login.setTextFormat(QtCore.Qt.AutoText)
        self.label_login.setObjectName("label_login")
    def label_password_set(self):
        self.label_password.setText("Пароль")
        self.label_password.setGeometry(QtCore.QRect(20, 240, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_password.setTextFormat(QtCore.Qt.AutoText)
        self.label_password.setObjectName("label_password")
    def login_btn_set(self):
        self.login_btn.setText("ВХОД")
        self.login_btn.setGeometry(QtCore.QRect(20, 330, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("""
    QPushButton {
        color: white;
        background-color: #000000; 
        border: none;
        
    }
    QPushButton:hover {
        background-color: #1a1a1a; 
    }
""")
        
        self.login_btn.setObjectName("login_btn")

    def label_wrong_data_set(self):
        self.label_wrong_data.setText("")
        self.label_wrong_data.setGeometry(QtCore.QRect(90, 390, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        
        self.label_wrong_data.setFont(font)
        self.label_wrong_data.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(249, 33, 33);")
        self.label_wrong_data.setTextFormat(QtCore.Qt.AutoText)
        self.label_wrong_data.setObjectName("label_wrong_data")
      