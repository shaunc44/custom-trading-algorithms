import flask
import pymysql.cursors
import timeit
import filter_model
import datetime as dt


#Begin timer
start = timeit.default_timer()


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	# cursorclass=pymysql.cursors.DictCursor
	)
c = conn.cursor()


class CreatePurchasedList:

	@classmethod
	def create_purchased_list(cls, rsi_buy, startdate): #change startdate to curr date?
		purchased_list = []
		startdate_db = dt.datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')

		c.execute('''
			SELECT price.date, filtered.ticker_id, price.adj_close
			FROM filtered 
			INNER JOIN price 
			ON filtered.ticker_id = price.ticker_id 
			WHERE price.rsi < %s 
			AND price.date = %s;
		''', (rsi_buy, startdate_db))

		rows = c.fetchall() 
		for row in rows:
			purchased_list.append(row)
			# print (row[0])

		print ("\nPurchased Ticker List = ", purchased_list)
		# return purchased_list


class AddPurchasedToPortfolio:

	@classmethod
	def add_purchased_to_portfolio(cls):
		pass


# lp = LastPriceFilter(5, 9999, '2017-03-22').run()
# print (lp.run())
# print (lp)


# filtered = FilteredStocksForTrading()
# print (filtered.create_master_list())

stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )



