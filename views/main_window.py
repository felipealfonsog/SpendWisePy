from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from models.database import Database, Expense, SubExpense

class MainWindow(QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.setWindowTitle("SpendWisePy")
        self.setGeometry(100, 100, 800, 600)
        self.current_date = None
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.expenses_table = QTableWidget()
        self.layout.addWidget(self.expenses_table)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.load_expenses()

    def load_expenses(self):
        expenses = self.database.get_all_expenses()
        self.expenses_table.setRowCount(len(expenses))
        for row, expense in enumerate(expenses):
            self.expenses_table.setItem(row, 0, QTableWidgetItem(str(expense.expense_id)))
            self.expenses_table.setItem(row, 1, QTableWidgetItem(expense.description))
            self.expenses_table.setItem(row, 2, QTableWidgetItem(str(expense.amount)))
            self.expenses_table.setItem(row, 3, QTableWidgetItem(expense.date.strftime("%Y-%m-%d")))

    def show_total_by_date(self, selected_date):
        self.current_date = selected_date
        expenses = self.database.get_expenses_by_date(selected_date)
        total_amount = sum(expense.amount for expense in expenses)
        # Resto del código para mostrar el total por fecha.

    def show_add_expense_dialog(self):
        # Aquí puedes implementar la lógica para abrir la ventana para agregar gastos.
        # Ejemplo:
        dialog = AddExpenseDialog()
        if dialog.exec_() == QDialog.Accepted:
            expense_data = dialog.get_expense_data()
            self.database.add_expense(expense_data["description"], expense_data["amount"], expense_data["date"])
            self.load_expenses()

    def show_edit_expense_dialog(self):
        # Aquí puedes implementar la lógica para abrir la ventana para editar gastos.
        # Ejemplo:
        selected_row = self.expenses_table.currentRow()
        if selected_row >= 0:
            expense_id = int(self.expenses_table.item(selected_row, 0).text())
            expense = self.database.get_expense_by_id(expense_id)
            if expense:
                dialog = EditExpenseDialog(expense)
                if dialog.exec_() == QDialog.Accepted:
                    expense_data = dialog.get_expense_data()
                    self.database.update_expense(expense_id, expense_data["description"], expense_data["amount"], expense_data["date"])
                    self.load_expenses()

    def show_delete_expense_dialog(self):
        # Aquí puedes implementar la lógica para abrir la ventana para borrar gastos.
        # Ejemplo:
        selected_row = self.expenses_table.currentRow()
        if selected_row >= 0:
            expense_id = int(self.expenses_table.item(selected_row, 0).text())
            self.database.delete_expense(expense_id)
            self.load_expenses()

    def show_add_subexpense_dialog(self):
        # Aquí puedes implementar la lógica para abrir la ventana para agregar subgastos.
        # Ejemplo:
        selected_row = self.expenses_table.currentRow()
        if selected_row >= 0:
            expense_id = int(self.expenses_table.item(selected_row, 0).text())
            expense = self.database.get_expense_by_id(expense_id)
            if expense:
                dialog = AddSubexpenseDialog(expense)
                if dialog.exec_() == QDialog.Accepted:
                    subexpense_data = dialog.get_subexpense_data()
                    self.database.add_subexpense(expense_id, subexpense_data["description"], subexpense_data["amount"], subexpense_data["date"])
                    self.load_expenses()

    def show_edit_subexpense_dialog(self):
        # Aquí puedes implementar la lógica para abrir la ventana para editar subgastos.
        # Ejemplo:
        selected_row = self.expenses_table.currentRow()
        if selected_row >= 0:
            expense_id = int(self.expenses_table.item(selected_row, 0).text())
            subexpenses = self.database.get_subexpenses_by_expense_id(expense_id)
            if subexpenses:
                dialog = EditSubexpenseDialog(subexpenses)
                if dialog.exec_() == QDialog.Accepted:
                    selected_subexpense_id = dialog.get_selected_subexpense_id()
                    subexpense = self.database.get_subexpense_by_id(selected_subexpense_id)
                    if subexpense:
                        dialog = EditSubexpenseDataDialog(subexpense)
                        if dialog.exec_() == QDialog.Accepted:
                            subexpense_data = dialog.get_subexpense_data()
                            self.database.update_subexpense(selected_subexpense_id, subexpense_data["description"], subexpense_data["amount"], subexpense_data["date"])
                            self.load_expenses()

    def show_delete_subexpense_dialog(self):
        # Aquí puedes implementar la lógica para abrir la ventana para borrar subgastos.
        # Ejemplo:
        selected_row = self.expenses_table.currentRow()
        if selected_row >= 0:
            expense_id = int(self.expenses_table.item(selected_row, 0).text())
            subexpenses = self.database.get_subexpenses_by_expense_id(expense_id)
            if subexpenses:
                dialog = DeleteSubexpenseDialog(subexpenses)
                if dialog.exec_() == QDialog.Accepted:
                    selected_subexpense_id = dialog.get_selected_subexpense_id()
                    self.database.delete_subexpense(selected_subexpense_id)
                    self.load_expenses()


def main():
    database = Database("localhost", "root", "fafarafa", "SpendWisePy")
    app = QApplication(sys.argv)
    window = MainWindow(database)
    window.initUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
