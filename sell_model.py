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
		''', (self.rsi_sell, self.startdate_db))

		rows = c.fetchall() 
		for row in rows:
			sell_list.append(row)

		print ("\nSell List = ", sell_list)
		# return purchased_list