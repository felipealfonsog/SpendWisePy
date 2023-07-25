import mysql.connector

class Database:
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database_name
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database successfully!")
        except mysql.connector.Error as error:
            print("Error connecting to MySQL database:", error)

    def save_expense(self, expense_type, amount, date):
        try:
            insert_query = "INSERT INTO expenses (expense_type, amount, date) VALUES (%s, %s, %s)"
            data = (expense_type, amount, date)
            self.cursor.execute(insert_query, data)
            self.connection.commit()
            print("Expense saved to the database successfully!")
        except mysql.connector.Error as error:
            print("Error saving expense to the database:", error)

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL database connection closed.")
