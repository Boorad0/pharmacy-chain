from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from ui.styles import apply_styles

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Аптека")
        self.resize(800, 600)
        self.setMaximumSize(QtCore.QSize(800, 600))

        self.centralwidget = QtWidgets.QWidget(self)
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

        self.setDefaultText()
        self.objectname_settings()
        self.geometry_settings()
        self.font_settings()
        apply_styles(self)

    def font_settings(self):
        self.title_font.setFamily("Arial")
        self.title_font.setPointSize(15)
        self.title_font.setBold(True)
        self.Title_txt.setFont(self.title_font)

        self.login_font.setFamily("Arial")
        self.login_font.setPointSize(10)
        self.Login_txt.setFont(self.login_font)
        self.Password_txt.setFont(self.password_font)

    def setDefaultText(self):
        self.setWindowTitle("База данных")
        self.Title_txt.setText("Вход в систему")
        self.login_btn.setText("Вход")
        self.Login_txt.setText("Логин")
        self.Password_txt.setText("Пароль")
        self.Login_status.setText("")

    def geometry_settings(self):
        self.Title_txt.setGeometry(0, 70, 801, 41)
        self.login_btn.setGeometry(190, 210, 75, 23)
        self.login_place.setGeometry(80, 130, 190, 31)
        self.password_place.setGeometry(80, 170, 190, 31)
        self.Login_txt.setGeometry(20, 140, 47, 13)
        self.Password_txt.setGeometry(20, 180, 47, 13)
        self.Login_status.setGeometry(80, 210, 47, 13)

    def objectname_settings(self):
        self.centralwidget.setObjectName("centralwidget")
        self.Title_txt.setObjectName("Title_txt")
        self.login_btn.setObjectName("login_btn")
        self.login_place.setObjectName("login_place")
        self.password_place.setObjectName("password_place")
        self.Login_txt.setObjectName("Login_txt")
        self.Password_txt.setObjectName("Password_txt")
        self.Login_status.setObjectName("Login_status")