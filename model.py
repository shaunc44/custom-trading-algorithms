import flask
import pymysql.cursors
import wrapper
#use pandas in here, not createdb
#use data from Quandl, Xignite


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='bigdump',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)
cursor = conn.cursor


class Users():
	pass




#Pull data from fundamentals csv
class Screening():
	pass




#Pull data from historical prices csv
class BuySell():
	pass






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







