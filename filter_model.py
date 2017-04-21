import flask
import pymysql.cursors
# import wrapper
import timeit


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


#This goes in the forms file
# #Set Date range somehow (1/1/2007 to 2/28/2017)
# #Iterate through list of trading dates here??? to input into SQL statements
# # start = "2007-01-02"
# # end = "2017-03-28"
# class Date:
# 	def add_date_range(self, daterange):
# 		self.daterange = daterange
# 		print (daterange)
# 		# start_date = 
# 		# end_date =
# 		# current_date =
# 		# trading_dates = 

# d = Date()
# d.add_date_range([today,tomorrow])


#####################################################################
############################  USER CLASS  ###########################
#####################################################################

class Users:
	pass

	@classmethod
	def check_login(cls, username, password):
		pass

	@classmethod
	def add_new_user(cls, username, password):
		pass


#####################################################################
###########################  FILTER CLASS  ##########################
#####################################################################


#How do i tell these filters to focus on a specific date and/or date range?
class Filter:
	def run(self):
		return self.screen()


#Takes 4.33 seconds for all filters to run
#15 minutes for 1 year
#select price.ticker from price where price.adj_close > 5 and price.date = '2017-03-28';
#takes 0.21 sec to run
class LastPriceFilter(Filter):
	def __init__(self, lp_low, lp_high, date):
		self.lp_low = lp_low
		self.lp_high = lp_high
		self.date = date
		self.lp_ticker_list = []

	def screen(self, tickers=None):
		c.execute('''
			SELECT DISTINCT price.ticker_id 
			FROM price 
			WHERE price.adj_close > %s 
			AND price.adj_close < %s 
			AND price.date = %s;
		''', (self.lp_low, self.lp_high, self.date)) #how to deal with no high or no low?

		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
		for row in rows:
			self.lp_ticker_list.append(row[0])
			# print (row[0])

		return self.lp_ticker_list

lp = LastPriceFilter(5, 9999, '2017-03-22').run()
# print (lp.run())
# print (lp)



# #SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pCURRENTRATIO) WHERE fundamental.value > 2.0 and fundamental.date > '2016-12-22' and fundamental.date < '2017-03-22';
# #takes 0.56 sec to run
class CurrentRatioFilter(Filter):
	name = "current-ratio"
	required = False
	parameter_names = [""]

	def __init__(self, cr_low, cr_high, begin_date, end_date):
		self.cr_low = cr_low
		self.cr_high = cr_high
		self.begin_date = begin_date
		self.end_date = end_date
		self.cr_ticker_list = []

	def screen(self):
		c.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pCURRENTRATIO) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date > %s 
			AND fundamental.date < %s;
			''', (self.cr_low, self.cr_high, self.begin_date, self.end_date))

		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
		for row in rows:
			self.cr_ticker_list.append(row[0])

		return self.cr_ticker_list

cr = CurrentRatioFilter(1, 9999, '2016-12-22', '2017-03-22').run()
# print (cr.run())



# #SELECT fundamental.ticker_id FROM fundamental PARTITION (pPE1) WHERE fundamental.value > 1.0 AND fundamental.value < 20.0 and fundamental.date > '2017-03-22';
# #takes 0.51 sec to run
class PriceEarningsFilter(Filter):
	def __init__(self, pe_low, pe_high, begin_date, end_date):
		self.pe_low = pe_low
		self.pe_high = pe_high
		self.begin_date = begin_date
		self.end_date = end_date
		self.pe_ticker_list = []

	def screen(self):
		c.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pPE1) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date > %s
			AND fundamental.date < %s;
			''', (self.pe_low, self.pe_high, self.begin_date, self.end_date))

		rows = c.fetchall()
		for row in rows:
			self.pe_ticker_list.append(row[0])

		return self.pe_ticker_list

pe = PriceEarningsFilter(0.1, 500.0, '2016-12-22', '2017-03-22').run()
# print (pe.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pEPS) WHERE fundamental.value > 0.5 and fundamental.date = '2017-03-22';
# #takes 1.18 sec to run
class EarningsPerShareFilter(Filter):
	def __init__(self, eps_low, eps_high, begin_date, end_date):
		self.eps_low = eps_low
		self.eps_high = eps_high
		self.begin_date = begin_date
		self.end_date = end_date
		self.eps_ticker_list = []

	def screen(self):
		c.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pEPS) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date > %s 
			AND fundamental.date < %s;
			''', (self.eps_low, self.eps_high, self.begin_date, self.end_date))

		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
		for row in rows:
			self.eps_ticker_list.append(row[0])
			# print (row[0])

		return self.eps_ticker_list

eps = EarningsPerShareFilter(0, 99999, '2016-12-22', '2017-03-22').run()
# print (eps.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pROE) WHERE fundamental.value > 10.0 and fundamental.date > '2016-05-22' and fundamental.date < '2016-08-22';
# #takes 0.40 sec to run
class ReturnOnEquityFilter(Filter):
	def __init__(self, roe_low, roe_high, begin_date, end_date):
		self.roe_low = roe_low
		self.roe_high = roe_high
		self.begin_date = begin_date
		self.end_date = end_date
		self.roe_ticker_list = []

	def screen(self):
		c.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pROE) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date > %s 
			AND fundamental.date < %s;
			''', (self.roe_low, self.roe_high, self.begin_date, self.end_date))

		rows = c.fetchall()
		for row in rows:
			self.roe_ticker_list.append(row[0])

		return self.roe_ticker_list

roe = ReturnOnEquityFilter(2, 99999, '2016-12-22', '2017-03-22').run()
# print (roe.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pROIC) WHERE fundamental.value > 15.0 AND fundamental.date > '2016-05-22' AND fundamental.date < '2016-08-22';
# #takes 0.36 sec to run
class ReturnOnInvestedCapitalFilter(Filter):
	def __init__(self, roic_low, roic_high, begin_date, end_date):
		self.roic_low = roic_low
		self.roic_high = roic_high
		self.begin_date = begin_date
		self.end_date = end_date
		self.roic_ticker_list = []

	def screen(self):
		c.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pROIC) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date > %s 
			AND fundamental.date < %s;
			''', (self.roic_low, self.roic_high, self.begin_date, self.end_date))

		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
		for row in rows:
			self.roic_ticker_list.append(row[0])
			# print (row[0])

		return self.roic_ticker_list

roic = ReturnOnInvestedCapitalFilter(1, 9999, '2016-12-22', '2017-03-22').run()
# print (roic.run())



# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pDIVYIELD) WHERE fundamental.value > 0.5 AND fundamental.date > '2016-05-22' AND fundamental.date < '2016-08-22';
# #takes 0.61 sec to run
class DividendYieldFilter(Filter):
	def __init__(self, dy_low, dy_high, begin_date, end_date):
		self.dy_low = dy_low
		self.dy_high = dy_high
		self.begin_date = begin_date
		self.end_date = end_date
		self.dy_ticker_list = []

	def screen(self):
		c.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pDIVYIELD) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date > %s 
			AND fundamental.date < %s;
			''', (self.dy_low, self.dy_high, self.begin_date, self.end_date))

		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
		for row in rows:
			self.dy_ticker_list.append(row[0])
			# print (row[0])

		return self.dy_ticker_list

dy = DividendYieldFilter(0.01, 100.00, '2016-12-22', '2017-03-22').run()
# print (dy.run())



#SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pDE) WHERE fundamental.value > 0.0 AND fundamental.value < 0.25 AND fundamental.date > '2016-05-22' AND fundamental.date < '2016-08-22';
#takes 0.92 sec to run
class DebtToEquityFilter(Filter):
	def __init__(self, de_low, de_high, begin_date, end_date):
		self.de_low = de_low
		self.de_high = de_high
		self.begin_date = begin_date
		self.end_date = end_date
		self.de_ticker_list = []

	def screen(self):
		c.execute('''
			SELECT DISTINCT fundamental.ticker_id 
			FROM fundamental PARTITION (pDE) 
			WHERE fundamental.value > %s 
			AND fundamental.value < %s 
			AND fundamental.date > %s 
			AND fundamental.date < %s;
			''', (self.de_low, self.de_high, self.begin_date, self.end_date))

		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
		for row in rows:
			self.de_ticker_list.append(row[0])
			# print (row[0])

		return self.de_ticker_list

de = DebtToEquityFilter(0, 1, '2016-12-22', '2017-03-22').run()
# print (de.run())



#convert to set so we can use intersection function
lp = set(lp)
cr = set(cr)
pe = set(pe)
eps = set(eps)
roe = set(roe)
roic = set(roic)
dy = set(dy)
de = set(de)


class CreateBuyList():
	def create_buy_list(self):
		counter = 0
		master_list = []
		# x = lp.intersection(cr.intersection(pe.intersection(eps.intersection(roe))))
		x = lp.intersection(cr.intersection(pe.intersection(eps.intersection(roe.intersection(roic.intersection(dy.intersection(de)))))))
		x = list(x)
		for i in x:
			master_list.append(i)
			counter += 1
			# print (i)
		# print ("Total Tickers = ", str(counter))
		return master_list


# filtered = CreateBuyList()
# print (filtered.create_buy_list())


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )






# # class PriceChange52WeekFilter(Filter):
# # 	def screen(self):
# # 		c.execute('''SELECT price.ticker FROM price WHERE ((price.adj_close - old_adj_close)/old_adj_close)*100) > %s AND ((price.adj_close - old_adj_close)/old_adj_close)*100) < %s;''', (low, high))
# # 		return c.fetchall() #How do I get the adj_close from one year ago???????



# @classmethod
# 	def screen(cls, lp_hi, lp_low, cr_hi, cr_lo, ftwpc_hi, ftwpc_lo, param, param, param, param, param, param, param, param, param, param, param, param, ):
#		pass

# 	@classmethod
# 	def last_price(cls, high, low):
# 		pass

# 	@classmethod
# 	def last_price(cls, high, low):
# 		pass

# 	@classmethod
# 	def current_ratio(cls, high, low):
# 		pass

# 	@classmethod
# 	def price_change_52_wk(cls, high, low):
# 		pass

# 	@classmethod
# 	def price_to_earnings(cls, high, low):
# 		pass

# 	@classmethod
# 	def earnings_per_share(cls, high, low):
# 		pass

# 	@classmethod
# 	def return_on_equity(cls, high, low):
# 		pass

# 	@classmethod
# 	def return_on_investment(cls, high, low):
# 		pass

# 	@classmethod
# 	def div_yield(cls, high, low):
# 		pass

# 	@classmethod
# 	def debt_to_equity(cls, high, low):
# 		pass

#Pull data from fundamentals table
# class Screen:
# 	def __init__(self, *filters):
# 		self._filters = filters

	
# 	def run(self):
# 		for filter_ in self._filters:
# 			filter.screen()

# my_filter = LastPriceFilter(6,7)
# Screen(my_filter)


# #Pull data from historical prices table



# #####################################################################
# ##########################  BUY/SELL CLASS  #########################
# #####################################################################

# class BuySell():
# 	pass

# 	@classmethod
# 	def sma_50_200_crossover(cls, high, low):
# 		pass

# 	@classmethod
# 	def volume_change(cls, high, low):
# 		pass

# 	@classmethod
# 	def price_change(cls, high, low):
# 		pass

# 	@classmethod
# 	def divergence(cls, high, low):
# 		pass

# 	@classmethod
# 	def macd(cls, high, low):
# 		pass

# 	@classmethod
# 	def rsi(cls, high, low):
# 		pass

# 	@classmethod
# 	def trailing_stop_loss(cls, percent):
# 		pass






# class Model():

# 	def initialize(context):
# 		#bring in init params
# 		pass

# 	def make_screen(context):
# 		#create dynamic stock selector
# 		pass

# 	def before_trading_start(context):
# 		#collect securities that passed the screen
# 		pass

# 	def purchase_stocks(context):
# 		pass

# 	def sell_stocks(context):
# 		pass

# 	def calculate_return(context):
# 		pass







