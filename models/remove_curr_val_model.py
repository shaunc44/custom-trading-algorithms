import flask
import pymysql.cursors
import datetime as dt



conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	)
c = conn.cursor()



class RemoveCurrentValue:
	def __init__(self, cursor, rundate):
		self.cursor = cursor
		self.rundate_db = rundate

	# Remove curr value for stocks sold
	def remove_curr_val_for_sold(self):
		c.execute('''
			UPDATE IGNORE portfolio
			SET portfolio.curr_value = 0
			WHERE (portfolio.sell_date > 0);''')
		conn.commit()
		conn.close()