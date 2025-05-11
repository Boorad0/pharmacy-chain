
from PyQt5.QtCore import Qt

class Authorization:
    def __init__(self, qtbot, app):
        self.qtbot = qtbot
        self.app = app
        

    def correct_login(self, login, password):
        self.qtbot.keyClicks(self.app.auth_window.login_place, login)
        self.qtbot.keyClicks(self.app.auth_window.password_place, password)
        self.qtbot.mouseClick(self.app.auth_window.login_btn, Qt.LeftButton)
        self.qtbot.waitUntil(lambda: self.app.stacked_widget.currentIndex() == 1, timeout=3000)

    def incorrect_login(self, login, password):
        self.qtbot.keyClicks(self.app.auth_window.login_place, login)
        self.qtbot.keyClicks(self.app.auth_window.password_place, password)
        self.qtbot.mouseClick(self.app.auth_window.login_btn, Qt.LeftButton)
        self.qtbot.waitUntil(lambda: self.app.auth_window.label_wrong_data.text() != "", timeout=1000)
   
        

       