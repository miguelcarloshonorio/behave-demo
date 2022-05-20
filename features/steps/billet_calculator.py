from datetime import datetime
from helpers.utils import Utils
from hamcrest import assert_that, equal_to, greater_than, none, is_not
from models.billet_calculator import Billet

from behave import then, given, when

_ignore_step_entry = "-"


@given('billet with value {amount} dollars')
def step_impl(context, amount):
    context.amount = amount


@given('the date due is {date_due}')
def step_impl(context, date_due):
    context.date_due = Utils.CovertToTime(date_due)


@given('the payment date is {payment_date}')
def step_impl(context, payment_date):
    context.payment_date = Utils.CovertToTime(payment_date)


@given('the late fee is {late_fee_percent} percent')
def step_impl(context, late_fee_percent):
    context.late_fee_percent = float(late_fee_percent)


@given('the late payment interest is {payment_interest} cents per day')
def step_impl(context, payment_interest):
    context.payment_interest = payment_interest


@when('I calculate the total value to pay')
def step_impl(context):
    billet = Billet(context.amount, context.late_fee_percent, context.date_due, context.payment_date)
    billet.calculate()
    context.billet = billet


@then('the system informs the total value is {total_amount}')
def step_impl(context, total_amount):
    assert_that((total_amount, context.billet.get_total()), "currency average")


@then('the total late payment days is {late_payment_days}')
def step_impl(context, late_payment_days):
    assert_that((late_payment_days, context.billet.get_late_payment_days()), "late_payment_days")


@then('the total of late payment interest {late_payment_interest}')
def step_impl(context, late_payment_interest):
    assert_that((late_payment_interest, context.billet.get_late_payment_interest()), "late_payment_interest")


@then('the total of late fee is {total_late_fee} dollars')
def step_impl(context, total_late_fee):
    assert_that((total_late_fee, context.billet.get_total_late_fee()), "total_late_fee")

