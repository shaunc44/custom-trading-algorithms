import flask
import pymysql.cursors
import timeit



conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	)
c = conn.cursor()



class SellStock:
	def __init__(self, cursor, rsi_sell, rundate):
		self.cursor = cursor
		self.rsi_sell = rsi_sell
		self.rundate_db = rundate

	def sell_stock(self): #how to change rundate to curr date?
		sell_list = []
		c.execute('''
			SELECT portfolio.ticker_id, price.date, price.adj_close
			FROM portfolio 
			INNER JOIN price 
			ON portfolio.ticker_id = price.ticker_id 
			WHERE price.rsi > %s 
			AND price.date = %s;
			''', (self.rsi_sell, self.rundate_db)
		)
		stocks_to_sell = c.fetchall() 
		print ("Possible Stocks to Sell = ", stocks_to_sell)

		for row in stocks_to_sell:
			symbol = row[0]
			# Add sell_date and sell_price to portfolio
			c.execute('''
				UPDATE portfolio 
				SET portfolio.sell_date = %s,
					portfolio.sell_price = %s
				WHERE portfolio.ticker_id = %s AND portfolio.sell_price = 0;
				''', 
				(row[1], row[2], row[0])
			)

			# Add sell_value and days_held to portfolio
			c.execute('''
				UPDATE portfolio
				SET portfolio.sell_value = ((portfolio.sell_price / portfolio.buy_price) * portfolio.buy_value),
					portfolio.days_held = DATEDIFF(portfolio.sell_date, portfolio.buy_date)
				WHERE portfolio.ticker_id = %s AND portfolio.sell_value = 0;
				''',
				(row[0])
			)

			# Add gain_loss to portfolio
			c.execute('''
				UPDATE portfolio
				SET portfolio.gain_loss = (portfolio.sell_value - portfolio.buy_value)
				WHERE portfolio.ticker_id = %s AND portfolio.gain_loss = 0;
				''',
				(row[0])
			)

			conn.commit()
		conn.close()











