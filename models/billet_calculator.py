# Billet

class Billet:
    totalAmount = 0

    def __init__(self, amount, late_fee, date_due, payment_date):
        self.amount = amount
        self.late_fee = late_fee
        self.date_due = date_due
        self.payment_date = payment_date

    def calculate(self):
        # calculate late fee, late payment interest
        self.totalAmount = self.amount + self.late_fee

    def get_total(self):
        return self.totalAmount
