
from PyQt5.QtWidgets import QMainWindow

class Style(QMainWindow):
    def __init__(self):
        super().__init__()
    

    def apply_styles(self):
        self.Title_txt.setStyleSheet("background-color: rgb(191, 191, 191); color: rgb(255, 255, 255);")
        self.Title_txt.setMargin(10)
        
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
        self.Login_status.setGeometry(80, 210, 85, 13)

    def objectname_settings(self):
        self.centralwidget.setObjectName("centralwidget")
        self.Title_txt.setObjectName("Title_txt")
        self.login_btn.setObjectName("login_btn")
        self.login_place.setObjectName("login_place")
        self.password_place.setObjectName("password_place")
        self.Login_txt.setObjectName("Login_txt")
        self.Password_txt.setObjectName("Password_txt")
        self.Login_status.setObjectName("Login_status")