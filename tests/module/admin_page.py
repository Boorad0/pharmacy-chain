from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt

class AdminPage:
    def __init__(self, qtbot, app):
        self.qtbot = qtbot
        self.app = app
        self.admin_page = self.app.main_window.admin_page

    def close_messagebox(self):
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QMessageBox):
                ok_button = widget.button(QMessageBox.Ok)
                if ok_button:
                    self.qtbot.mouseClick(ok_button, Qt.LeftButton)
                    self.qtbot.waitUntil(lambda: not widget.isVisible(), timeout=1000)
                    break

    def add_user(self, username, password, role):
        self.qtbot.mouseClick(self.app.main_window.admin_btn, Qt.LeftButton)
        self.qtbot.mouseClick(self.admin_page.add_user_button, Qt.LeftButton)
        dialog = self.admin_page.dialog
        self.qtbot.waitExposed(dialog)
        self.qtbot.keyClicks(dialog.username_input, username)
        self.qtbot.keyClicks(dialog.password_input, password)
        dialog.role_select.setCurrentText(role)
        self.qtbot.mouseClick(dialog.add_button, Qt.LeftButton)
        self.qtbot.waitUntil(lambda: any(isinstance(w, QMessageBox) for w in QApplication.topLevelWidgets()), timeout=2000)
        self.close_messagebox()
        self.qtbot.waitUntil(lambda: not dialog.isVisible(), timeout=2000)
        
    def check_user_in_table(self, username: str, role: str = None) -> bool:
        table = self.admin_page.table
        for row in range(table.rowCount()):
            username_item = table.item(row, 1)
            role_item = table.item(row, 2)
            if username_item and username_item.text() == username:
                if role is None or (role_item and role_item.text() == role):
                    return True
        return False
