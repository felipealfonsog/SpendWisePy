import mysql.connector

class Database:
    def __init__(self, host, user, password, database_name):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        self.cursor = self.connection.cursor()

    def add_expense(self, expense_type, amount, date):
        query = "INSERT INTO expenses (expense_type, amount, date) VALUES (%s, %s, %s)"
        values = (expense_type, amount, date)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        expenses_data = self.cursor.fetchall()
        expenses = [Expense(expense_id=row[0], expense_type=row[1], amount=row[2], date=row[3]) for row in expenses_data]
        return expenses

    def get_expenses_by_date(self, selected_date):
        query = "SELECT * FROM expenses WHERE date = %s"
        self.cursor.execute(query, (selected_date,))
        return [Expense(*row) for row in self.cursor.fetchall()]

    def update_expense(self, expense_id, expense_type, amount, date):
        query = "UPDATE expenses SET expense_type = %s, amount = %s, date = %s WHERE id = %s"
        values = (expense_type, amount, date, expense_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_expense(self, expense_id):
        query = "DELETE FROM expenses WHERE id = %s"
        self.cursor.execute(query, (expense_id,))
        self.connection.commit()

    def get_expenses_by_date(self):
        query = "SELECT date, SUM(amount) FROM expenses GROUP BY date"
        self.cursor.execute(query)
        expenses_data = self.cursor.fetchall()
        expenses_by_date = {row[0]: row[1] for row in expenses_data}
        return expenses_by_date


class Expense:
    def __init__(self, expense_id, expense_type, amount, date):
        self.expense_id = expense_id
        self.expense_type = expense_type
        self.amount = amount
        self.date = date
