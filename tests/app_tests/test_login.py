from PyQt5.QtCore import Qt
from tests.module.authorization import Authorization
from PyQt5.QtCore import Qt

def test_correct_login(app, qtbot):
    auth = Authorization(qtbot, app)
    auth.correct_login("boorado", "12345678")
    assert app.stacked_widget.currentIndex() == 1

def test_incorrect_login(app, qtbot):
    auth = Authorization(qtbot, app)
    auth.incorrect_login("wrong", "wrong")
    assert app.stacked_widget.currentIndex() == 0
    assert app.auth_window.label_wrong_data.text() == "Неверный логин или пароль"

def test_exit_btn(app, qtbot):
    auth = Authorization(qtbot, app)
    auth.correct_login("boorado", "12345678")
    assert app.stacked_widget.currentIndex() == 1
    qtbot.mouseClick(app.main_window.logout_btn, Qt.LeftButton)
    assert app.stacked_widget.currentIndex() == 0

    
    