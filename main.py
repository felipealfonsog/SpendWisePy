import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from models.database import Database

def main():
    database = Database("localhost", "root", "fafarafa", "SpendWisePy")
    app = QApplication(sys.argv)
    window = MainWindow(database)
    window.initUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
