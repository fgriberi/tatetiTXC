from tateti_txc import *
from behave import *
from splinter import Browser
browser = Browser('flask', app=app)


@given("Tateti app home")
def step_impl(context):
    browser.visit('http://127.0.0.1:5000')


@then("Welcome screen message will display")
def step_impl(context):
    assert "Welcome" in browser.html, "Welcome not found"
