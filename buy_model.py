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
	def __init__(self, rsi_buy, startdate):
		self.rsi_buy = rsi_buy
		self.startdate_db = dt.datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')

	def create_purchased_list(self): #change startdate to curr date?
		purchased_list = []
		# startdate_db = dt.datetime.strptime(self.startdate, '%m/%d/%Y').strftime('%Y-%m-%d')
		c.execute('''
			SELECT filtered.ticker_id, price.date, price.adj_close
			FROM filtered 
			INNER JOIN price 
			ON filtered.ticker_id = price.ticker_id 
			WHERE price.rsi < %s 
			AND price.date = %s;
		''', (self.rsi_buy, self.startdate_db))

		rows = c.fetchall() 
		for row in rows:
			purchased_list.append(row)

		print ("\nPurchased Ticker List = ", purchased_list)
		return purchased_list



# class AddPurchasedToPortfolio:
# 	def __init__(self, results):
# 		self.results = results

# 	@classmethod
# 	def add_purchased_to_portfolio(cls, rsi_buy, startdate):
# 		purchased = CreatePurchasedList.create_purchased_list(rsi_buy, startdate)
# 		for row in purchased:
# 			# print ("Purchased Date = ", row[0])
# 			c.execute('''
# 				INSERT INTO portfolio (
# 					ticker_id,
# 					buy_date,
# 					buy_price,
# 					buy_value,
# 					shares)
# 				VALUES (
# 					%s,
# 					%s,
# 					%s,
# 					%s,
# 					%s
# 				);''', 
# 				(row[0], row[1], row[2], calc1, calc2)
# 			)
# 			conn.commit()
# 		conn.close()

		# remove_purchased_from_filtered(purchased)

	# @classmethod
	# def remove_purchased_from_filtered(cls, purchased):
	# 	print ("Purchased = ", purchased)
	# 	# purchased_to_remove = CreatePurchasedList.create_purchased_list(rsi_buy, startdate)
	# 	for ticker_id in purchased:
	# 		c.execute('''
	# 			DELETE FROM filtered
	# 			WHERE filtered.ticker_id = ?
	# 			);''',(ticker_id)





# lp = LastPriceFilter(5, 9999, '2017-03-22').run()
# print (lp.run())
# print (lp)


# filtered = FilteredStocksForTrading()
# print (filtered.create_master_list())

stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )









