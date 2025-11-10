# models/database.py
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


import mysql.connector

class DatabaseModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root2',
            password='root2',
            database='SpendWisePy'
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def create_table(self):


        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            description VARCHAR(255),
            date DATE NOT NULL  -- Change this to DATE type
        )
        """
        self.cursor.execute(query)
        self.connection.commit()



    def add_expense(self, name, amount, description, date):
        query = "INSERT INTO expenses (name, amount, description, date) VALUES (%s, %s, %s, %s)"
        values = (name, amount, description, date)  # No es necesario convertir la fecha a cadena
        self.cursor.execute(query, values)
        self.connection.commit()



    def get_all_expenses(self):
        query = "SELECT * FROM expenses"
        self.cursor.execute(query)
        expenses = self.cursor.fetchall()
        return expenses

    def update_expense(self, expense_id, new_name, new_amount, new_description, new_date):
        query = "UPDATE expenses SET name = %s, amount = %s, description = %s, date = %s WHERE id = %s"
        values = (new_name, new_amount, new_description, new_date, expense_id)  # No es necesario convertir la fecha a cadena
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_expense(self, expense_id):
        query = "DELETE FROM expenses WHERE id = %s"
        values = (expense_id,)
        self.cursor.execute(query, values)
        self.connection.commit()
