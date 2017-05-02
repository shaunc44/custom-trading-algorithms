import flask
import pymysql.cursors
import timeit
# import filter_model
import datetime as dt


#Begin timer
start = timeit.default_timer()


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	)
c = conn.cursor()



class AddCurrentDataToPortfolio:
	def __init__(self, startdate):
		# self.rsi_sell = rsi_sell
		self.startdate_db = dt.datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')

	def add_current_data(self): #how to change startdate to curr date?
		# sell_list = []
		c.execute('''
			SELECT portfolio.ticker_id, price.date, price.adj_close
			FROM portfolio 
			INNER JOIN price 
			ON portfolio.ticker_id = price.ticker_id 
			WHERE price.date = %s;
			''', (self.startdate_db)
		)

		current = c.fetchall()

		for row in current:
			print ("Current = ", row)
			c.execute('''
				UPDATE IGNORE portfolio
				SET portfolio.curr_price = %s
				WHERE (portfolio.ticker_id = %s) 
				AND (portfolio.sell_date = 0);
				UPDATE IGNORE portfolio
				SET portfolio.curr_value = ((portfolio.curr_price / portfolio.buy_price) * portfolio.buy_value)
				WHERE portfolio.sell_date = 0;
				''',
				(row[2], row[0])
			)
			conn.commit()
		conn.close()

		# Remove curr value for stocks sold
	def remove_curr_val_for_sold(self):
		c.execute('''
			UPDATE IGNORE portfolio
			SET portfolio.curr_value = 0
			WHERE portfolio.sell_date > 0;
			'''
		)
		conn.commit()
	conn.close()






