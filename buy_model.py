import flask
import pymysql.cursors
# import wrapper
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


#####################################################################
###########################  FILTER CLASS  ##########################
#####################################################################

#How do i tell these filters to focus on a specific date and/or date range?
# class Filter:
# 	def __init__(self):
# 		pass
# 		# self buy_list = filter_model

# 	def run(self):
# 		return self.screen()

#Takes 4.33 seconds for all filters to run
#15 minutes for 1 year
#select price.ticker from price where price.adj_close > 5 and price.date = '2017-03-28';
#takes 0.21 sec to run
class CreatePurchasedList:
	# def __init__(self, lp_low, lp_high, end_date):
	# 	self.lp_low = lp_low
	# 	self.lp_high = lp_high
	# 	self.end_date = end_date
		# self.lp_ticker_list = []
	@classmethod
	def create_purchased_list(cls, rsi_buy, startdate): #change startdate to curr date?
		purchased_list = []
		startdate_db = dt.datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')

		c.execute('''
			SELECT filtered.ticker_id 
			FROM filtered 
			INNER JOIN price 
			ON filtered.ticker_id = price.ticker_id 
			WHERE price.rsi < %s 
			AND price.date = %s;
		''', (rsi_buy, startdate_db))

		rows = c.fetchall() 
		for row in rows:
			purchased_list.append(row[0])
			# print (row[0])

		print ("\nPurchased Ticker List = ", purchased_list)
		# return purchased_list

# lp = LastPriceFilter(5, 9999, '2017-03-22').run()
# print (lp.run())
# print (lp)



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pDIVYIELD) WHERE fundamental.value > 0.5 AND fundamental.date > '2016-05-22' AND fundamental.date < '2016-08-22';
# # #takes 0.61 sec to run
# class DividendYieldFilter(Filter):
# 	def __init__(self, dy_low, dy_high, begin_date, end_date):
# 		self.dy_low = dy_low
# 		self.dy_high = dy_high
# 		self.begin_date = begin_date
# 		self.end_date = end_date
# 		self.dy_ticker_list = []

# 	def screen(self):
# 		c.execute('''
# 			SELECT DISTINCT fundamental.ticker_id 
# 			FROM fundamental PARTITION (pDIVYIELD) 
# 			WHERE fundamental.value > %s 
# 			AND fundamental.value < %s 
# 			AND fundamental.date > %s 
# 			AND fundamental.date < %s;
# 			''', (self.dy_low, self.dy_high, self.begin_date, self.end_date))

# 		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
# 		for row in rows:
# 			self.dy_ticker_list.append(row[0])
# 			# print (row[0])

# 		return self.dy_ticker_list

# dy = DividendYieldFilter(0.01, 100.00, '2016-12-22', '2017-03-22').run()
# # print (dy.run())



#convert to set so we can use intersection function
# lp = set(lp)
# cr = set(cr)
# pe = set(pe)
# eps = set(eps)
# roe = set(roe)
# roic = set(roic)
# dy = set(dy)
# de = set(de)


# class FilteredStocksForTrading():
# 	def create_master_list(self):
# 		counter = 0
# 		master_list = []
# 		x = lp.intersection(cr.intersection(pe.intersection(eps.intersection(roe))))
# 		# x = lp.intersection(cr.intersection(pe.intersection(eps.intersection(roe.intersection(roic.intersection(dy.intersection(de)))))))
# 		x = list(x)
# 		for i in x:
# 			master_list.append(i)
# 			counter += 1
# 			# print (i)

# 		print ("Total Tickers = ", str(counter))
# 		return master_list


# filtered = FilteredStocksForTrading()
# print (filtered.create_master_list())

stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )



