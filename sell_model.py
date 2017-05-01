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



class SellStock:
	def __init__(self, rsi_sell, startdate):
		self.rsi_sell = rsi_sell
		self.startdate_db = dt.datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')

	def sell_stock(self): #how to change startdate to curr date?
		sell_list = []
		c.execute('''
			SELECT portfolio.ticker_id, price.date, price.adj_close
			FROM portfolio 
			INNER JOIN price 
			ON portfolio.ticker_id = price.ticker_id 
			WHERE price.rsi > %s 
			AND price.date = %s;
			''', (self.rsi_sell, self.startdate_db)
		)

		stocks_to_sell = c.fetchall() 
		print ("Stocks to Sell = ", stocks_to_sell)

		for row in stocks_to_sell:
			# print("Ticker_ID = ", row[0], "Sell_Date = ", row[1], "Sell_Price = ", row[2])
			symbol = row[0]
			c.execute('''
				UPDATE portfolio 
				SET portfolio.sell_date = %s,
					portfolio.sell_price = %s
				WHERE portfolio.ticker_id = %s AND portfolio.sell_price = 0;
				''', 
				(row[1], row[2], row[0])
			)

			c.execute('''
				UPDATE portfolio
				SET portfolio.sell_value = ((portfolio.sell_price / portfolio.buy_price) * portfolio.buy_value),
					portfolio.days_held = DATEDIFF(portfolio.sell_date, portfolio.buy_date)
				WHERE portfolio.ticker_id = %s;
				''',
				(row[0])
			)

			# portfolio.days_held = portfolio.sell_date portfolio.sell_date
			# portfolio.gain_loss = 
			conn.commit()
		conn.close()




	# def add_sell_stats(self):
	# 	c.execute('''

				


	# 		;'''
	# 	)

		# 	sell_list.append(row)
		# print ("\nSell List = ", sell_list)
		# return purchased_list









