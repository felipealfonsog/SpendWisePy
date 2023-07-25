import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QFormLayout, QGroupBox, QDateEdit
from PyQt5.QtCore import Qt, QDate
from datetime import datetime

# Class to represent an expense
class Expense:
    def __init__(self, expense_type, amount, date):
        self.expense_type = expense_type
        self.amount = amount
        self.date = date

# Class for the expense tracking application
class ExpenseTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.monthly_budget = 1000  # Set the initial monthly budget
        self.expenses = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Expense Tracking App')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Input widgets
        self.expense_type_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.date_input = QDateEdit(QDate.currentDate())

        # Button to add an expense
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

        # Update the summary
        self.show_summary()

    def calculate_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def calculate_remaining_budget(self):
        return self.monthly_budget - self.calculate_total_expenses()

    def show_summary(self):
        summary_text = "----- Expense Summary -----\n"
        for expense in self.expenses:
            summary_text += f"{expense.expense_type}: {expense.amount} - Date: {expense.date}\n"
        summary_text += f"Total Expenses: {self.calculate_total_expenses()}\n"
        summary_text += f"Remaining Budget: {self.calculate_remaining_budget()}"
        self.summary_label.setText(summary_text)

# Function to show an error message
def show_error_message(message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(message)
    msg_box.exec_()

# Main function
def main():
    app = QApplication(sys.argv)
    window = ExpenseTrackerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
