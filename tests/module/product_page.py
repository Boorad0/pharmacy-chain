from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
class ProductPage:
    def __init__(self, qtbot, app):
        self.qtbot = qtbot
        self.app = app
        self.product_page = self.app.main_window.product_page
        self.table = self.product_page.table_product
        
    def add_new_product(self):
        self.qtbot.mouseClick(self.product_page.btn_add, Qt.LeftButton)
        self.product_page.add_window.isVisible()
        table = self.product_page.add_window_table
        table.setItem(0, 0, QTableWidgetItem("Тестовый товар1"))
        table.setItem(0, 1, QTableWidgetItem("Производитель Х"))
        table.setItem(0, 2, QTableWidgetItem("2025-12-31"))
        table.setItem(0, 3, QTableWidgetItem("100"))
        self.qtbot.mouseClick(self.product_page.add_window_button, Qt.LeftButton)
        self.product_page.load_data_from_db(editable=True)

        
        
    def enable_editing_mode(self):
        self.qtbot.mouseClick(self.app.main_window.product_btn, Qt.LeftButton)
        self.qtbot.mouseClick(self.product_page.btn_edit, Qt.LeftButton)
    def edit_product(self, old_name, new_name):
        

        for row in range(self.table.rowCount()):
            item = self.table.item(row, 1)
            if item and item.text() == old_name:
                self.table.setItem(row, 1, QTableWidgetItem(new_name)) 
                self.qtbot.wait(200)

                self.product_page.load_data_from_db(editable=False)
                updated_item = self.product_page.table_product.item(row, 1)
                return updated_item.text() == new_name

        return False  