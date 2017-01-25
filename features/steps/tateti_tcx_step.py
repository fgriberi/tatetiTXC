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


@when(u'User start game')
def step_impl(context):
    start_game_btn = browser.find_by_id("start_game")[0]
    start_game_btn.click()


@then(u'game is started')
def step_impl(context):
    assert "Game Started!" in browser.html


@given(u'User start game')
def step_impl(context):
    start_game_btn = browser.find_by_id("start_game")[0]
    start_game_btn.click()


@when(u'User click button {x} {y}')
def step_impl(context, x, y):
    button_id = "first_button_" + str(x) + "_" + str(y)
    first_button = browser.find_by_id(button_id)[0]
    first_button.click()


@then(u'button {x} {y} change state')
def step_impl(context, x, y):
    button_id = "first_button_" + str(x) + "_" + str(y)
    class_css_btn = browser.find_by_id(button_id)[0]
    assert "X" in class_css_btn.value
