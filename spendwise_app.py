import sys
#print(sys.path)

import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QGroupBox, QDateEdit
from PyQt5.QtCore import Qt, QDate

# Adjust the Python path to include the parent directory of the models folder
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

# Import the Expense class using a relative import
from models.expense import Expense


# Import the Database class from the database.py file
from database import Database

class SpendWisePy(QMainWindow):
    # Rest of the code remains the same


    def __init__(self):
        super().__init__()

        self.expenses = []
        self.initUI()

        # Initialize the database
        self.database = Database(host='localhost',   # Replace with your MySQL host
                                 user='root',   # Replace with your MySQL user
                                 password='fafarafa',  # Replace with your MySQL password
                                 database_name='SpendWisePy')  # Replace with your database name
        self.database.connect()

    def initUI(self):
        self.setWindowTitle('SpendWisePy - Expense Tracker')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Widgets for input
        self.expense_type_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.date_input = QDateEdit(QDate.currentDate())

        # Button to add expense
        add_button = QPushButton('Add Expense')
        add_button.clicked.connect(self.add_expense)

        # Group box for input widgets
        form_group_box = QGroupBox('Add Expense')
        layout = QFormLayout()
        layout.addRow('Expense Type:', self.expense_type_input)
        layout.addRow('Amount:', self.amount_input)
        layout.addRow('Date:', self.date_input)
        layout.addRow(add_button)
        form_group_box.setLayout(layout)

        # Label to show expense summary
        self.summary_label = QLabel()

        # Add widgets to the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(form_group_box)
        main_layout.addWidget(self.summary_label)
        self.central_widget.setLayout(main_layout)

    def add_expense(self):
        expense_type = self.expense_type_input.text()
        amount = float(self.amount_input.text())
        date = self.date_input.date().toString(Qt.ISODate)
        expense = Expense(expense_type, amount, date)
        self.expenses.append(expense)

        # Save the expense to the MySQL database
        self.database.save_expense(expense_type, amount, date)

        # Update the summary
        self.show_summary()

    def calculate_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def show_summary(self):
        summary_text = "----- Expense Summary -----\n"
        for expense in self.expenses:
            summary_text += f"{expense.expense_type}: {expense.amount} - Date: {expense.date}\n"
        summary_text += f"Total Expenses: {self.calculate_total_expenses()}"
        self.summary_label.setText(summary_text)

# Rest of the code remains the same

# Function to show an error message
def show_error_message(message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(message)
    msg_box.exec_()

# Main function
def main():
    app = QApplication(sys.argv)
    window = SpendWisePy()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
