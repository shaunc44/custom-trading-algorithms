import flask
import pymysql.cursors



class RemoveCurrentValue:
	def __init__(self, conn, cursor, rundate):
		self.conn = conn
		self.cursor = cursor
		self.rundate_db = rundate

	# Remove curr value for stocks sold
	def remove_curr_val_for_sold(self):
		self.cursor.execute('''
			UPDATE IGNORE portfolio
			SET portfolio.curr_value = 0
			WHERE (portfolio.sell_date > 0);''')
		self.conn.commit()