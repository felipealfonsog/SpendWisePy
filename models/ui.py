from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QTableWidget, QVBoxLayout, QPushButton, QDialog,
    QFormLayout, QLineEdit, QLabel, QDateEdit, QMessageBox, QAction, QMenu, QComboBox, QTableWidgetItem, QWidget
)
from PyQt5.QtCore import Qt, QDate
from models.database import Database, Expense

class ExpenseDialog(QDialog):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.initUI()

    def initUI(self):
        layout = QFormLayout()

        self.expense_type_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.date_input = QDateEdit(QDate.currentDate())
        self.date_input.setCalendarPopup(True)

        layout.addRow("Expense Type:", self.expense_type_input)
        layout.addRow("Amount:", self.amount_input)
        layout.addRow("Date:", self.date_input)

        buttons_layout = QVBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.add_expense)
        buttons_layout.addWidget(save_button)

        layout.addRow(buttons_layout)

        self.setLayout(layout)

    def add_expense(self):
        expense_type = self.expense_type_input.text()
        amount = self.amount_input.text()
        date = self.date_input.date().toString(Qt.ISODate)

        if expense_type and amount and date:
            if self.database.add_expense(expense_type, amount, date):
                self.show_message("Expense saved to the database successfully!")
                self.close()
            else:
                self.show_message("Failed to save the expense to the database.", "Error")
        else:
            self.show_message("Please fill in all the fields.", "Warning")

    def show_message(self, message, title="Information"):
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.exec_()


class SpendWiseUI(QMainWindow):
    def __init__(self, database):
        super().__init__()

        self.database = database

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("SpendWise")

        self.create_menus()

        self.expenses_table = QTableWidget(self)
        self.expenses_table.setColumnCount(4)
        self.expenses_table.setHorizontalHeaderLabels(["ID", "Expense Type", "Amount", "Date"])

        self.total_combobox = QComboBox()
        self.total_combobox.currentTextChanged.connect(self.show_total_by_date)

        self.load_expenses()

        layout = QVBoxLayout()
        layout.addWidget(self.expenses_table)
        layout.addWidget(self.total_combobox)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Agregar botones de edición y borrado en una barra de herramientas
        self.toolbar = self.addToolBar("Tools")
        add_action = QAction("Add Expense", self)
        add_action.triggered.connect(self.add_expense)
        self.toolbar.addAction(add_action)

        edit_action = QAction("Edit Expense", self)
        edit_action.triggered.connect(self.edit_expense)
        self.toolbar.addAction(edit_action)

        delete_action = QAction("Delete Expense", self)
        delete_action.triggered.connect(self.delete_expense)
        self.toolbar.addAction(delete_action)

    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        add_action = QAction("Add Expense", self)
        add_action.triggered.connect(self.add_expense)
        file_menu.addAction(add_action)

        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_expense)
        file_menu.addAction(delete_action)

        edit_action = QAction("Edit Expense", self)
        edit_action.triggered.connect(self.edit_expense)
        file_menu.addAction(edit_action)

    def load_expenses(self):
        self.expenses = self.database.get_all_expenses()
        self.show_expenses()
        self.update_total_combobox()

    def show_expenses(self):
        self.expenses_table.setRowCount(0)

        for row_position, expense in enumerate(self.expenses, 0):
            self.expenses_table.insertRow(row_position)
            self.expenses_table.setItem(row_position, 0, QTableWidgetItem(str(expense.expense_id)))
            self.expenses_table.setItem(row_position, 1, QTableWidgetItem(expense.expense_type))
            self.expenses_table.setItem(row_position, 2, QTableWidgetItem(str(expense.amount)))
            self.expenses_table.setItem(row_position, 3, QTableWidgetItem(str(expense.date)))

    def update_total_combobox(self):
        self.total_combobox.clear()
        dates = set(expense.date for expense in self.expenses)
        for date in sorted(dates):
            total = self.get_total_by_date(date)
            self.total_combobox.addItem(f"{date} - Total: {total:.2f}")

    def show_total_by_date(self):
        selected_text = self.total_combobox.currentText()
        total = float(selected_text.split(":")[1])
        self.total_combobox.setEditText(f"{selected_text} - Total: {total:.2f}")

    def get_total_by_date(self, selected_date):
        total = 0
        for expense in self.expenses:
            if expense.date == selected_date:
                total += expense.amount
        return total

    def add_expense(self):
        expense_dialog = ExpenseDialog(self.database)
        expense_dialog.exec_()
        self.load_expenses()

    def delete_expense(self):
        selected_row = self.expenses_table.currentRow()
        if selected_row != -1:
            expense_id = int(self.expenses_table.item(selected_row, 0).text())
            if self.show_confirmation_dialog("Are you sure you want to delete this expense?"):
                if self.database.delete_expense(expense_id):
                    self.show_message("Expense deleted successfully.", "Success")
                    self.load_expenses()
                else:
                    self.show_message("Failed to delete the expense.", "Error")
        else:
            self.show_message("Please select a row to delete.", "Warning")

    def edit_expense(self):
        selected_row = self.expenses_table.currentRow()
        if selected_row != -1:
            expense_id = int(self.expenses_table.item(selected_row, 0).text())
            expense = self.database.get_expense_by_id(expense_id)
            if expense:
                self.show_edit_dialog(expense)
        else:
            self.show_message("Please select a row to edit.", "Warning")

    def show_edit_dialog(self, expense):
        edit_dialog = ExpenseDialog(self.database)
        edit_dialog.setWindowTitle("Edit Expense")
        edit_dialog.expense_type_input.setText(expense.expense_type)
        edit_dialog.amount_input.setText(str(expense.amount))
        date = QDate.fromString(expense.date, Qt.ISODate)
        edit_dialog.date_input.setDate(date)
        edit_dialog.exec_()
        self.load_expenses()

    def show_confirmation_dialog(self, message, title="Confirmation"):
        confirmation_box = QMessageBox(self)
        confirmation_box.setIcon(QMessageBox.Question)
        confirmation_box.setText(message)
        confirmation_box.setWindowTitle(title)
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_box.setDefaultButton(QMessageBox.No)
        return confirmation_box.exec_() == QMessageBox.Yes

    def show_message(self, message, title="Information"):
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.exec_()


def main():
    app = QApplication([])
    database = Database(host='localhost', user='root', password='your_password', database_name='SpendWisePy')
    if database.connect():
        window = SpendWiseUI(database)
        window.show()
        app.exec_()
    else:
        show_error_message("Error connecting to the database. Please check your credentials.")


if __name__ == "__main__":
    main()
