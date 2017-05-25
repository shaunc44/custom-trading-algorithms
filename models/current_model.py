import flask
import pymysql.cursors
# import timeit
import datetime as dt


#Begin timer
# start = timeit.default_timer()


class AddCurrentDataToPortfolio:
	def __init__(self, conn, cursor, rundate):
		self.conn = conn
		self.cursor = cursor
		self.rundate_db = rundate

	def add_current_data(self): #how to change rundate to curr date?
		# sell_list = []
		# print ("Current Model Rundate = ", self.rundate_db)
		self.cursor.execute('''
			SELECT portfolio.ticker_id, price.date, price.adj_close
			FROM portfolio 
			INNER JOIN price 
			ON portfolio.ticker_id = price.ticker_id 
			WHERE price.date = %s;
			''', (self.rundate_db)
		)

		current = self.cursor.fetchall()

		for row in current:
			# print ("Current = ", row)
			# Set current price for each portfolio holding
			# Set current value to zero if holding has sold
			# Set current value for each portfolio holding
			# Set high price for each holding
			self.cursor.execute('''
				UPDATE IGNORE portfolio
				SET portfolio.curr_price = %s
				WHERE (portfolio.ticker_id = %s) 
				AND (portfolio.sell_date = 0);
				UPDATE IGNORE portfolio
				SET portfolio.curr_value = 0
				WHERE portfolio.sell_date > 0;
				UPDATE IGNORE portfolio
				SET portfolio.curr_value = ((portfolio.curr_price / portfolio.buy_price) * portfolio.buy_value)
				WHERE portfolio.sell_date = 0;
				UPDATE IGNORE portfolio
				SET portfolio.hi_price = %s
				WHERE (portfolio.curr_price >= portfolio.buy_price)
				AND (portfolio.ticker_id = %s);
				''',
				(row[2], row[0], row[2], row[0])
			)
			self.conn.commit()
		# self.conn.close()







