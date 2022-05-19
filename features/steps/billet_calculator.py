from datetime import datetime
from helpers.utils import Utils

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
    context.late_fee_percent = late_fee_percent


@given('the late payment interest is {payment_interest} cents per day')
def step_impl(context, payment_interest):
    context.payment_interest = payment_interest


@when('I calculate the total value to pay')
def step_impl(context):
    raise NotImplementedError('STEP: When I calculate the total value to pay')


@then('the system informs the total value is 513.33')
def step_impl(context):
    raise NotImplementedError('STEP: Then the system informs the total value is 513.33')


@then('the total late payment days is 10')
def step_impl(context):
    raise NotImplementedError('STEP: Then the total late payment days is 10')


@then('the total of late payment interest 3.33')
def step_impl(context):
    raise NotImplementedError('STEP: Then the total of late payment interest 3.33')


@then('the total of late fee is 10 dollars')
def step_impl(context):
    raise NotImplementedError('STEP: Then the total of late fee is 10 dollars')
