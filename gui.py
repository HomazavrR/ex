import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,  QTableWidget, QTableWidgetItem, QApplication
from bd import BD


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.bd = BD()

        self.ui = uic.loadUi("ui.ui", self)
        self.window().setWindowTitle("Урок")

        ##self.ui.load_btn.clicked.connect(self.draw_data_table)

        self.ui.delete_btn.clicked.connect(self.delete_data)

        ##self.ui.update_hall_btn.clicked.connect(self.update_hall_db)

        self.ui.add_btn.clicked.connect(self.create_data_bd)

        self.draw_data_table()

    def draw_data_table(self):
        self.table = self.ui.tableWidget
        self.table.clear()
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(["id", "name", "phone"])

        res = self.bd.read_data()

        i = 0
        for data in res:
            self.table.setRowCount(i + 1)
            j = 0
            for attribute in data:
                item = QTableWidgetItem()
                item.setText(str(attribute))
                self.table.setItem(i, j, item)
                j += 1
            i += 1

    def update_data_table(self):
        self.table = self.ui.tableWidget
        self.table.clear()
        self.draw_data_table();

    def delete_data(self):
        id = self.ID_input.text()
        if(id != ''):
            self.bd.delete_data(id)
        self.update_data_table()

    def update_data_bd(self):
        id = self.id_data_update.text()
        name = self.new_data_name.text()
        phone = self.new_data_phone.text()
        self.bd.update_data(id,name,phone)
        self.update_data_table()

    def create_data_bd(self):
        id = self.ID_input.text()
        name = self.Name_input.text()
        phone = self.Phone_input.text()
        self.bd.create_data(id, name, phone)
        self.update_data_table()


# main
qapp = QApplication(sys.argv)
window = MainWindow()
window.show()
qapp.exec()