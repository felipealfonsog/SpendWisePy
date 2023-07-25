class Expense:
    def __init__(self, expense_type, amount, date, expense_id=None):
        self.id = expense_id
        self.expense_type = expense_type
        self.amount = amount
        self.date = date
