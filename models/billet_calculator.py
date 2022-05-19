# Billet
from datetime import timedelta


class Billet:
    totalAmount = 0

    def __init__(self, amount, late_fee, date_due, payment_date):
        self.amount = amount
        self.late_fee = late_fee
        self.date_due = date_due
        self.payment_date = payment_date

    def calculate(self):
        # todo: calculate late fee, late payment interest
        self.totalAmount = float(self.amount) + float(self.get_late_payment_interest())

    def get_total(self):
        return self.totalAmount

    def get_late_payment_days(self):
        delta = self.payment_date - self.date_due
        return delta.days

    def get_late_payment_interest(self):
        fee = float(self.get_late_payment_days()) * 0.33 * float(self.amount)
        return fee

    def get_total_late_fee(self):
        fee = 0.02 * float(self.amount)
        return fee

