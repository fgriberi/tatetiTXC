from rover import *
from behave import *
from splinter import Browser
browser = Browser('flask',app=app)

@given(u'Mars Rover landed')
def step_impl(context):
	browser.visit('http://127.0.0.1:5000')

@then(u'position should be {position}')
def step_impl(context,position):
	assert position in browser.html , position

