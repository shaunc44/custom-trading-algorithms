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


# DOES THE PURCHASED LIST RESET WITH EACH ITERATION ????

class AddPurchasedToPortfolio:
	def __init__(self, purchased):
		self.purchased = purchased

	def add_purchased_to_portfolio(self):
		for row in self.purchased:
			c.execute('''
				SELECT IF (
					(1000000 - SUM(portfolio.buy_value) + SUM(portfolio.sell_value) > 20000 OR 1000000 - SUM(portfolio.buy_value) + SUM(portfolio.sell_value) IS NULL), 
					20000, 
					1000000 - SUM(portfolio.buy_value) + SUM(portfolio.sell_value)
				)
				FROM portfolio
				;''')

			cash_avail = c.fetchone()
			# print ("Cash Avail = ", cash_avail[0])
			c.execute('''
				INSERT INTO portfolio 
				IF (
					portfolio.ticker_id IS NULL 
					OR portfolio.sell_value IS NOT NULL,
					(ticker_id,
					buy_date,
					buy_price,
					buy_value)
				VALUES (
					%s,
					%s,
					%s,
					%s
				)
				);
				DELETE FROM portfolio 
				WHERE buy_value = 0;
				''', 
				(row[0], row[1], row[2], cash_avail)
			)

			conn.commit()
		conn.close()

	# def add_purchased_value_to_portfolio(self):
	# 	# purchased = CreatePurchasedList.create_purchased_list(rsi_buy, startdate)
	# 	for row in self.purchased:
	# 		# print ("Purchased Date = ", row[0])
	# 		c.execute('''
	# 			INSERT INTO portfolio (
	# 				buy_value)
	# 			SELECT CASE WHEN (
	# 				(1000000 - SUM(porfolio.buy_value) + SUM(porfolio.sell_value)) > 20000)
	# 			THEN 
	# 				(20000)
	# 			ELSE 
	# 				(1000000 - SUM(porfolio.buy_value) + SUM(porfolio.sell_value))
	# 			;''' 
	# 			# (row[0], row[1], row[2])
	# 		)
	# 		conn.commit()
	# 	conn.close()

		# remove_purchased_from_filtered(purchased)

	# @classmethod
	# def remove_purchased_from_filtered(cls, purchased):
	# 	print ("Purchased = ", purchased)
	# 	# purchased_to_remove = CreatePurchasedList.create_purchased_list(rsi_buy, startdate)
	# 	for ticker_id in purchased:
	# 		c.execute('''
	# 			DELETE FROM filtered
	# 			WHERE filtered.ticker_id = ?
	# 			);''', (ticker_id)





# lp = LastPriceFilter(5, 9999, '2017-03-22').run()
# print (lp.run())
# print (lp)


# filtered = FilteredStocksForTrading()
# print (filtered.create_master_list())

stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )









