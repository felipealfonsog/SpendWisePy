'''


▒█▀▀▀█ █▀▀█ █▀▀ █▀▀▄ █▀▀▄ ▒█░░▒█ ░▀░ █▀▀ █▀▀ ▒█▀▀█ █░░█ 
░▀▀▀▄▄ █░░█ █▀▀ █░░█ █░░█ ▒█▒█▒█ ▀█▀ ▀▀█ █▀▀ ▒█▄▄█ █▄▄█ 
▒█▄▄▄█ █▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▒█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▒█░░░ ▄▄▄█


*************************************************
SpendWisePy Expense Tracker Application
*************************************************
*  Simple: An expense tracking application to create and manage expenses.
*************************************************
* Developed and engineered by:
* Felipe Alfonso Gonzalez <f.alfonso@res-ear.ch>
* Computer Science Engineer
* Chile
*************************************************
* Prerequisites:
* - Python 3: Make sure you have Python 3 installed on your system.
* - PyQt5: Install PyQt5 library for the graphical user interface.
*   You can install it using pip: pip install pyqt5
* - Database model: The application uses a custom database model.
*   Make sure to include the appropriate model or adapt it for your needs.
*************************************************
* How to run the SpendWisePy application:
*
* 1. Clone the SpendWisePy repository from GitHub.
*
* 2. Navigate to the project directory:
*    cd SpendWisePy
*
* 3. Run the main application script:
*    python spendwiseapp.py
*
* 4. The SpendWisePy application will launch, allowing you to:
*    - Add expenses with name, amount, description, and date.
*    - Update and delete existing expenses.
*    - Filter expenses based on a specific date range.
*
* 5. To exit the application, close the main window.
*
*************************************************
* Important Notes:
* - The application has been tested on Linux and macOS.
* - For Windows, additional configurations may be required.
* - Make sure to fulfill the prerequisites before running the application.
* - The database model may need to be adjusted to match your database setup.
* - For more information, please refer to the project documentation.
*************************************************
'''



from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, QDateEdit, QCalendarWidget, QMessageBox
from PyQt5.QtCore import Qt, QDate

# Importar solo la clase datetime directamente
import datetime

from models.database import DatabaseModel

from decimal import Decimal, InvalidOperation  # Import the Decimal class and InvalidOperation


class SpendWiseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SpendWisePy')
        self.setGeometry(100, 100, 800, 500)

        self.init_ui()

        self.database_model = DatabaseModel()
        self.database_model.create_table()

        self.filter_date = None  # Initialize filter_date attribute
       
        self.refresh_expenses()  

       
 

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel('SpendWisePy')
        self.layout.addWidget(self.label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Expense Name')
        self.layout.addWidget(self.name_input)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText('Amount')
        self.layout.addWidget(self.amount_input)

        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText('Description')
        self.layout.addWidget(self.description_input)

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)  
        self.date_input.setDate(QDate.currentDate())  
        self.layout.addWidget(self.date_input)

        self.add_button = QPushButton('Add Expense')
        self.add_button.clicked.connect(self.add_expense)
        self.layout.addWidget(self.add_button)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Amount', 'Description', 'Date'])
        # After creating the table widget, set the row height:
        self.table.verticalHeader().setDefaultSectionSize(25)

        self.layout.addWidget(self.table)

        self.total_label = QLabel()
        self.layout.addWidget(self.total_label)

        self.update_button = QPushButton('Update Expense')
        self.update_button.clicked.connect(self.update_expense)
        self.layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Delete Expense')
        self.delete_button.clicked.connect(self.delete_expense)
        self.layout.addWidget(self.delete_button)

        self.start_date_input = QDateEdit()
        self.start_date_input.setCalendarPopup(True)
        self.layout.addWidget(self.start_date_input)
        
        self.start_date_input.setDate(QDate.currentDate())  # Use QDate.currentDate() to set the current date

        
        self.reset_filter_button = QPushButton('Reset Filter')
        self.reset_filter_button.clicked.connect(self.reset_filter)
        self.layout.addWidget(self.reset_filter_button)



   #     self.end_date_input = QDateEdit()
   #     self.end_date_input.setCalendarPopup(True)

        # Add a filter button to apply the date range filter
        
        self.filter_button = QPushButton('Filter')
        self.filter_button.clicked.connect(self.filter_expenses)
        self.layout.addWidget(self.filter_button)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)




    def add_expense(self):
        name = self.name_input.text()
        amount = self.amount_input.text()
        description = self.description_input.text()
        date = self.date_input.date().toPyDate()

        try:
            amount = float(amount)
            self.database_model.add_expense(name, amount, description, date)
            self.refresh_expenses() 
            self.clear_inputs()
        except ValueError:
            print("Invalid amount format.")
        except Exception as e:
            print("Error:", e)
        
     
        total_amount = self.refresh_expenses()
        self.total_label.setText(f'Total: {total_amount:.2f}')


    def update_expense(self):
        row = self.table.currentRow()
        if row == -1:
            return

        expense_id = int(self.table.item(row, 0).text())
        name = self.table.item(row, 1).text()
        amount_text = self.table.item(row, 2).text()
        description = self.table.item(row, 3).text()
        date_text = self.table.item(row, 4).text()

        try:
            amount = Decimal(amount_text) 
        except InvalidOperation:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Invalid amount format.")
            return

        # Update the expense in the database
        self.database_model.update_expense(expense_id, name, amount, description, date_text)

        # Refresh the expenses table and update the total amount
        total_amount = self.refresh_expenses()

        # Update the total label with the new total amount
        self.total_label.setText(f'Total: {total_amount:.2f}')

                
    def delete_expense(self):
        row = self.table.currentRow()
        if row >= 0:
            item = self.table.item(row, 0)
            if item is not None:  # Check if the item at the current row exists
                expense_id = int(item.text())
                try:
                    self.database_model.delete_expense(expense_id)
                    self.refresh_expenses()
                    self.clear_inputs()
                except Exception as e:
                    print("Error:", e)
            else:
                print("Select an expense to delete.")
        else:
            print("Select an expense to delete.")
        total_amount = self.refresh_expenses()
        self.total_label.setText(f'Total: {total_amount:.2f}')



    def filter_expenses(self):
        self.filter_date = self.start_date_input.date().toPyDate()
        self.refresh_expenses()
        
        total_amount = self.refresh_expenses()
        self.total_label.setText(f'Total: {total_amount:.2f}')


    def reset_filter(self):
        self.filter_date = None
        self.start_date_input.setDate(datetime.date.today())  # Reset the start date input
        self.refresh_expenses()  # Refresh the expenses table with the updated filter

        
    def refresh_expenses(self):
        self.table.clearContents()
        expenses = self.database_model.get_all_expenses()

        self.table.setRowCount(len(expenses))
        total_amount = 0.0

        for row, expense in enumerate(expenses):
            expense_date = expense[4]  # The date is already a datetime.date object

            # If there is a filter date, only show expenses with matching date
            if self.filter_date and expense_date != self.filter_date:
                continue

            self.table.setItem(row, 0, QTableWidgetItem(str(expense[0])))
            self.table.setItem(row, 1, QTableWidgetItem(expense[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(expense[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(expense[3])))  # Convert the date to a string
            self.table.setItem(row, 4, QTableWidgetItem(str(expense[4])))
            total_amount += float(expense[2])  # Convert decimal to float

        self.total_label.setText(f'Total: {total_amount:.2f}')
        return total_amount  # Return the total_amount value


    def clear_inputs(self):
        self.name_input.clear()
        self.amount_input.clear()
        self.description_input.clear()
        self.date_input.setDate(datetime.date.today())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpendWiseApp()
    window.show()
    sys.exit(app.exec_())