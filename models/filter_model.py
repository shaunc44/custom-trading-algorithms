import flask
import pymysql.cursors
import datetime as dt
# import timeit


#Begin timer
# start = timeit.default_timer()

# conn = pymysql.connect(host='localhost',
# 	user='scox',
# 	password='scox',
# 	db='trading_algo',
# 	charset='utf8mb4'
# 	# cursorclass=pymysql.cursors.DictCursor
# 	)
# c = conn.cursor()


#This goes in the forms file
#Iterate through list of trading dates here??? to input into SQL statements
# start = "2007-01-02"
# end = "2017-03-28"
# class Date():
# 	@classmethod
# 	def add_date_range(cls, startdate, enddate):
# 		startdate = dt.datetime.strptime(startdate, '%m/%d/%Y').strftime('%Y-%m-%d')
# 		enddate = dt.datetime.strptime(enddate, '%m/%d/%Y').strftime('%Y-%m-%d')
		# print ("Type = ", type(startdate))
		# print ("Models' Startdate = ", startdate)
		# print ("Models' Enddate = ", enddate)
		# start_date = 
		# enddate =
		# current_date =
		# trading_dates = 

# d = Date()
# d.add_date_range([today,tomorrow])

# trading_dates = [] #get list of distinct trading_days from the price list based on input date range
# current_date = #need to start with start_date and iterate through list of trading_days to the enddate

#####################################################################
############################  USER CLASS  ###########################
#####################################################################

# class Users:
# 	pass

# 	@classmethod
# 	def check_login(cls, username, password):
# 		pass

# 	@classmethod
# 	def add_new_user(cls, username, password):
# 		pass


#####################################################################
###########################  FILTER CLASS  ##########################
#####################################################################


#How do i tell these filters to focus on a specific date and/or date range?
class Filter():
	def run(self):
		return self.screen()


#Takes 4.33 seconds for all filters to run
#15 minutes for 1 year
#select price.ticker from price where price.adj_close > 5 and price.date = '2017-03-28';
#takes 0.21 sec to run
class LastPriceFilter(Filter):
	def __init__(self, conn, cursor, lp_low, lp_high, rundate):
		self.conn = conn
		self.cursor = cursor
		self.lp_low = lp_low
		self.lp_high = lp_high
		self.rundate = rundate

	def screen(self): #the date should iterate over the trading dates beginning with start date
		# print ("Filter Model Rundate = ", self.rundate)
		lp_ticker_list = []
		# run_date = dt.datetime.strptime(rundate, '%m/%d/%Y').strftime('%Y-%m-%d')
		self.cursor.execute('''
			SELECT DISTINCT price.ticker_id 
			FROM price 
			WHERE price.adj_close > %s 
			AND price.adj_close < %s 
			AND price.date = %s;
		''', (self.lp_low, self.lp_high, self.rundate)) #the startdate needs to move forward one trading day until it reaches the enddate

		rows = self.cursor.fetchall() 
		for row in rows:
			lp_ticker_list.append(row[0])

		# print ("\nLast Price Ticker List = ", lp_ticker_list)
		return lp_ticker_list

# lp = LastPriceFilter(5, 9999, '2017-03-22').run()
# lp = LastPriceFilter().run()
# print (lp.run())
# print (lp)



# #SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pCURRENTRATIO) WHERE fundamental.value > 2.0 and fundamental.date > '2016-12-22' and fundamental.date < '2017-03-22';
# #takes 0.56 sec to run
# class CurrentRatioFilter(Filter):
# 	name = "current-ratio"
# 	required = False
# 	parameter_names = [""]

# 	def __init__(self, cr_low, cr_high, startdate, enddate):
# 		self.cr_low = cr_low
# 		self.cr_high = cr_high
# 		self.startdate = startdate
# 		self.enddate = enddate
# 		self.cr_ticker_list = []

# 	def screen(self):
# 		c.execute('''
# 			SELECT DISTINCT fundamental.ticker_id 
# 			FROM fundamental PARTITION (pCURRENTRATIO) 
# 			WHERE fundamental.value > %s 
# 			AND fundamental.value < %s 
# 			AND fundamental.date > %s 
# 			AND fundamental.date < %s;
# 			''', (self.cr_low, self.cr_high, self.startdate, self.enddate))

# 		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
# 		for row in rows:
# 			self.cr_ticker_list.append(row[0])

# 		return self.cr_ticker_list

# cr = CurrentRatioFilter(1, 9999, '2016-12-22', '2017-03-22').run()
# print (cr.run())



# #SELECT fundamental.ticker_id FROM fundamental PARTITION (pPE1) WHERE fundamental.value > 1.0 AND fundamental.value < 20.0 and fundamental.date > '2017-03-22';
# #takes 0.51 sec to run
class PriceEarningsFilter(Filter):
	def __init__(self, conn, cursor, pe_low, pe_high, rundate):
		self.conn = conn
		self.cursor = cursor
		self.pe_low = pe_low
		self.pe_high = pe_high
		self.rundate = rundate
		# self.pe_ticker_list = []

	def screen(self):
		pe_ticker_list = []
		#date for sql statement
		# print ("Run Date = ", self.rundate)
		run_date_fmt = dt.datetime.strptime(self.rundate, '%Y-%m-%d') 
		#convert rundate string to datetime format
		trailing_date_fmt = run_date_fmt - dt.timedelta(days=90) 
		#subtract 90 days from rundate to get trailingdate
		trailingdate_db = dt.datetime.strftime(trailing_date_fmt, '%Y-%m-%d') 
		#convert trailingdate to string
		# print ("Trailing Date = ", trailingdate_db)

		self.cursor.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pPE1) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date >= %s 
			AND fundamental.date <= %s;
			''', (self.pe_low, self.pe_high, trailingdate_db, self.rundate)
		)

		rows = self.cursor.fetchall()
		for row in rows:
			pe_ticker_list.append(row[0])
		# print ("\nPE Ticker List = ", pe_ticker_list)
		return pe_ticker_list

# pe = PriceEarningsFilter(0.1, 500.0, '2016-12-22', '2017-03-22').run()
# print (pe.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pEPS) WHERE fundamental.value > 0.5 and fundamental.date = '2017-03-22';
# #takes 1.18 sec to run
# class EarningsPerShareFilter(Filter):
# 	def __init__(self, eps_low, eps_high, startdate, enddate):
# 		self.eps_low = eps_low
# 		self.eps_high = eps_high
# 		self.startdate = startdate
# 		self.enddate = enddate
# 		self.eps_ticker_list = []

# 	def screen(self):
# 		c.execute('''
# 			SELECT DISTINCT fundamental.ticker_id 
# 			FROM fundamental PARTITION (pEPS) 
# 			WHERE fundamental.value > %s 
# 			AND fundamental.value < %s 
# 			AND fundamental.date > %s 
# 			AND fundamental.date < %s;
# 			''', (self.eps_low, self.eps_high, self.startdate, self.enddate))

# 		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
# 		for row in rows:
# 			self.eps_ticker_list.append(row[0])
# 			# print (row[0])

# 		return self.eps_ticker_list

# eps = EarningsPerShareFilter(0, 99999, '2016-12-22', '2017-03-22').run()
# print (eps.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pROE) WHERE fundamental.value > 10.0 and fundamental.date > '2016-05-22' and fundamental.date < '2016-08-22';
class ReturnOnEquityFilter(Filter):
	def __init__(self, conn, cursor, roe_low, roe_high, rundate):
		self.conn = conn
		self.cursor = cursor
		self.roe_low = roe_low
		self.roe_high = roe_high
		self.rundate = rundate

	def screen(self):
		roe_ticker_list = []
		# print ("Run Date = ", self.rundate)
		run_date_fmt = dt.datetime.strptime(self.rundate, '%Y-%m-%d') 
		#convert rundate string to datetime format
		trailing_date_fmt = run_date_fmt - dt.timedelta(days=90) 
		#subtract 90 days from rundate to get trailingdate
		trailingdate_db = dt.datetime.strftime(trailing_date_fmt, '%Y-%m-%d')

		self.cursor.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pROE) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date >= %s 
			AND fundamental.date <= %s;
			''', (self.roe_low, self.roe_high, trailingdate_db, self.rundate))

		rows = self.cursor.fetchall()
		for row in rows:
			roe_ticker_list.append(row[0])

		return roe_ticker_list

# roe = ReturnOnEquityFilter(2, 99999, '2016-12-22', '2017-03-22').run()
# print (roe.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pROIC) WHERE fundamental.value > 15.0 AND fundamental.date > '2016-05-22' AND fundamental.date < '2016-08-22';
# #takes 0.36 sec to run
# class ReturnOnInvestedCapitalFilter(Filter):
# 	def __init__(self, roic_low, roic_high, startdate, enddate):
# 		self.roic_low = roic_low
# 		self.roic_high = roic_high
# 		self.startdate = startdate
# 		self.enddate = enddate
# 		self.roic_ticker_list = []

# 	def screen(self):
# 		c.execute('''
# 			SELECT DISTINCT fundamental.ticker_id 
# 			FROM fundamental PARTITION (pROIC) 
# 			WHERE fundamental.value > %s 
# 			AND fundamental.value < %s 
# 			AND fundamental.date > %s 
# 			AND fundamental.date < %s;
# 			''', (self.roic_low, self.roic_high, self.startdate, self.enddate))

# 		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
# 		for row in rows:
# 			self.roic_ticker_list.append(row[0])
# 			# print (row[0])

# 		return self.roic_ticker_list

# roic = ReturnOnInvestedCapitalFilter(1, 9999, '2016-12-22', '2017-03-22').run()
# print (roic.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pDIVYIELD) WHERE fundamental.value > 0.5 AND fundamental.date > '2016-05-22' AND fundamental.date < '2016-08-22';
# #takes 0.61 sec to run
class DividendYieldFilter(Filter):
	def __init__(self, conn, cursor, dy_low, dy_high, rundate):
		self.conn = conn
		self.cursor = cursor
		self.dy_low = dy_low
		self.dy_high = dy_high
		self.rundate = rundate

	def screen(self):
		dy_ticker_list = []
		# print ("Run Date = ", self.rundate)
		run_date_fmt = dt.datetime.strptime(self.rundate, '%Y-%m-%d') 
		#convert rundate string to datetime format
		trailing_date_fmt = run_date_fmt - dt.timedelta(days=90) 
		#subtract 90 days from rundate to get trailingdate
		trailingdate_db = dt.datetime.strftime(trailing_date_fmt, '%Y-%m-%d') 
		#convert trailingdate to string
		# print ("Trailing Date = ", trailingdate_db)

		self.cursor.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pDIVYIELD) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date >= %s 
			AND fundamental.date <= %s;
			''', (self.dy_low, self.dy_high, trailingdate_db, self.rundate))

		rows = self.cursor.fetchall()
		for row in rows:
			dy_ticker_list.append(row[0])
		# print ("\nDiv Yield Ticker List = ", dy_ticker_list)
		return dy_ticker_list



#SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pDE) WHERE fundamental.value > 0.0 AND fundamental.value < 0.25 AND fundamental.date > '2016-05-22' AND fundamental.date < '2016-08-22';
#takes 0.92 sec to run
class DebtToEquityFilter(Filter):
	def __init__(self, conn, cursor, de_low, de_high, rundate):
		self.conn = conn
		self.cursor = cursor
		self.de_low = de_low
		self.de_high = de_high
		self.rundate = rundate

	def screen(self):
		de_ticker_list = []
		run_date_fmt = dt.datetime.strptime(self.rundate, '%Y-%m-%d') 
		#convert rundate string to datetime format
		trailing_date_fmt = run_date_fmt - dt.timedelta(days=90) 
		#subtract 90 days from rundate to get trailingdate
		trailingdate_db = dt.datetime.strftime(trailing_date_fmt, '%Y-%m-%d') 

		self.cursor.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pDE) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date >= %s 
			AND fundamental.date <= %s;
			''', (self.de_low, self.de_high, trailingdate_db, self.rundate))

		rows = self.cursor.fetchall()
		for row in rows:
			de_ticker_list.append(row[0])
		# print ("\nDiv Yield Ticker List = ", dy_ticker_list)
		return de_ticker_list

# de = DebtToEquityFilter(0, 1, '2016-12-22', '2017-03-22').run()
# print (de.run())



#convert to set so we can use intersection function
# lp = set(lp)
# # cr = set(cr)
# pe = set(pe)
# # eps = set(eps)
# # roe = set(roe)
# # roic = set(roic)
# dy = set(dy)
# de = set(de)


class CreateFilteredList:
	def __init__(self, conn, cursor, lp_low, lp_high, pe_low, pe_high, roe_low, roe_high, dy_low, dy_high, de_low, de_high, rundate):
		self.conn = conn
		self.cursor = cursor
		self.lp_low = lp_low
		self.lp_high = lp_high
		self.pe_low = pe_low
		self.pe_high = pe_high
		self.roe_low = roe_low
		self.roe_high = roe_high
		self.dy_low = dy_low
		self.dy_high = dy_high
		self.de_low = de_low
		self.de_high = de_high
		self.rundate = rundate

	def create_filtered_list(self):
		counter = 0
		master_filtered_list = []

		lp = LastPriceFilter(self.conn, self.cursor, self.lp_low, self.lp_high, self.rundate)
		lp = lp.screen()
		pe = PriceEarningsFilter(self.conn, self.cursor, self.pe_low, self.pe_high, self.rundate)
		pe = pe.screen()
		roe = ReturnOnEquityFilter(self.conn, self.cursor, self.roe_low, self.roe_high, self.rundate)
		roe = roe.screen()
		dy = DividendYieldFilter(self.conn, self.cursor, self.dy_low, self.dy_high, self.rundate)
		dy = dy.screen()
		de = DebtToEquityFilter(self.conn, self.cursor, self.de_low, self.de_high, self.rundate)
		de = de.screen()

		lp = set(lp)
		pe = set(pe)
		roe = set(roe)
		dy = set(dy)
		de = set(de)

		filtered_list = lp.intersection(
						pe.intersection(
						roe.intersection(
						dy.intersection(
						de))))
		# x = lp.intersection(cr.intersection(pe.intersection(eps.intersection(roe.intersection(roic.intersection(dy.intersection(de)))))))
		filtered_list = list(filtered_list)
		for symbol in filtered_list:
			master_filtered_list.append(symbol)
			counter += 1
			# print (i)
		# print ("\nTotal Filtered Tickers = ", str(counter))
		# print ("\nFiltered List = ", master_filtered_list)

		# Delete previous filtered table
		self.cursor.execute('''
			DELETE FROM filtered;
			'''
		)
		# Add filtered list to filtered table
		for ticker_id in master_filtered_list:
			self.cursor.execute('''
				INSERT IGNORE INTO filtered (
					date,
					ticker_id)
				VALUES (
					%s,
					%s
				);''', 
				(self.rundate, ticker_id)
			)
			self.conn.commit()
		# self.conn.close()

# filtered = CreateBuyList()
# print (filtered.create_filtered_list())


# stop = timeit.default_timer()
# print ("Seconds to run: ", (stop - start) )





# # class PriceChange52WeekFilter(Filter):
# # 	def screen(self):
# # 		c.execute('''SELECT price.ticker FROM price WHERE ((price.adj_close - old_adj_close)/old_adj_close)*100) > %s AND ((price.adj_close - old_adj_close)/old_adj_close)*100) < %s;''', (low, high))
# # 		return c.fetchall() #How do I get the adj_close from one year ago???????





