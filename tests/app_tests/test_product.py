from PyQt5.QtCore import Qt
from tests.module.authorization import Authorization
import time
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from tests.module.product_page import ProductPage
def test_add_new_product(app, qtbot):
    auth = Authorization(qtbot, app)
    auth.correct_login("boorado", "12345678")
    product = ProductPage(qtbot, app)
    product.enable_editing_mode()
    assert app.main_window.product_page.btn_edit.text() == "Сохранить"
    product.add_new_product()
    assert app.main_window.product_page.add_window_error_label.text() == ""

    assert any("Тестовый товар1" in app.main_window.product_page.table_product.item(row, 1).text()
            for row in range(app.main_window.product_page.table_product.rowCount()))
    
def test_edit_product(app, qtbot):
    auth = Authorization(qtbot, app)
    auth.correct_login("boorado", "12345678")
    product = ProductPage(qtbot, app)
    product.enable_editing_mode()
    assert app.main_window.product_page.btn_edit.text() == "Сохранить"
    product.add_new_product()
    assert product.edit_product("Тестовый товар1", "11111111111") == True, "Товар не найден или не обновлён"