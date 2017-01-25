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

@then(u'Welcome screen start button will display')
def step_impl(context):
    started_button = browser.find_by_id("start_game")
    print (started_button.first.html)
    #assert "Start Game!" == started_button.text
