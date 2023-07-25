from PyQt5.QtWidgets import QApplication
from models.ui import SpendWiseUI
from models.database import Database

def main():
    database = Database(host='localhost', user='root', password='fafarafa', database_name='SpendWisePy')
    app = QApplication([])
    window = SpendWiseUI(database)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
