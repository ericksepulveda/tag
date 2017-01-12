from fourinline import *
from behave import *
from splinter import Browser
browser = Browser('flask',app=app)

@given(u'Game started')
def step_impl(context):
	browser.visit('http://127.0.0.1:5000')

@then(u'the board should be set and empty')
def step_impl(context):
  board = browser.find_by_id("board")
  assert board, browser.html
  assert len(board.find_by_text("O")) == 0, browser.html
  assert len(board.find_by_text("X")) == 0, browser.html

@then(u'it should be Player_yellow\'s turn')
def step_impl(context):
  turn = browser.find_by_id("turn")
  assert turn, browser.html
  assert turn.find_by_text("Turno actual: Amarillo"), browser.html

@when(u'player makes a move on column {col}')
def step_impl(context, col):
  browser.fill('col', col)
  browser.find_by_id('submit').click()

@then(u'there should be a yellow element in column {col}')
def step_impl(context, col):
  assert browser.find_by_id('0_' + col).first.text == 1