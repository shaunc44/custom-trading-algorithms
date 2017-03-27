import flask
import mysql
import wrapper
#use pandas in here, not createdb
#use data from Quandl, Xignite


conn = mysql.connect("stock_algo.db")
cursor = conn.cursor


class Model():

	def initialize(context):
		#bring in init params
		pass

	def make_screen(context):
		#create dynamic stock selector
		pass

	def before_trading_start(context):
		#collect securities that passed the screen
		pass

	def purchase_stocks(context):
		pass

	def sell_stocks(context):
		pass

	def calculate_return(context):
		pass


class ModelWrapper:
	pass