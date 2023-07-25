import mysql.connector

class Expense:
    def __init__(self, expense_id, description, amount, date):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.date = date

class SubExpense:
    def __init__(self, subexpense_id, expense_id, expense_type, amount, date):
        self.subexpense_id = subexpense_id
        self.expense_id = expense_id
        self.expense_type = expense_type
        self.amount = amount
        self.date = date


class Database:
    def __init__(self, host, user, password, database_name):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        self.cursor = self.connection.cursor()

    def add_expense(self, description, amount, date):
        query = "INSERT INTO expenses (description, amount, date) VALUES (%s, %s, %s)"
        values = (description, amount, date)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        expenses_data = self.cursor.fetchall()
        expenses = [Expense(expense_id=row[0], description=row[1], amount=row[2], date=row[3]) for row in expenses_data]
        return expenses

    # Resto del código...
