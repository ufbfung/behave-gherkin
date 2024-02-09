# features/steps/test_addition.py
from behave import given, when, then
from calculator import add

@given('I have a calculator')
def step_impl(context):
    pass  # This is just to set up the context, nothing needed for our simple example

@when('I add 2 and 3')
def step_impl(context):
    context.result = add(2, 3)

@then('the result should be 5')
def step_impl(context):
    assert context.result == 5
