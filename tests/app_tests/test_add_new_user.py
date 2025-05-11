from tests.module.authorization import Authorization
from tests.module.admin_page import AdminPage

def test_add_new_user(app, qtbot):
    auth = Authorization(qtbot, app)
    auth.correct_login("boorado", "12345678")
    admin = AdminPage(qtbot, app)
    assert app.stacked_widget.currentIndex() == 1
    admin.add_user("testuser12314", "1", "user")
    assert admin.check_user_in_table("testuser12314", "user")
    

