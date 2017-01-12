from toque import *
from behave import *
from splinter import Browser
browser = Browser('flask',app=app)

@given(u'Game started')
def step_impl(context):
	browser.visit('http://127.0.0.1:5000')

@then(u'hint should be {hint}')
def step_impl(context, hint):
	assert hint in browser.html , browser.html

@when(u'player sends a {guess}')
def step_impl(context, guess):
	browser.fill("guess", guess)
	browser.find_by_id("submit").click()