import flask
import pymysql.cursors
import wrapper
#use pandas in here, not createdb
#use data from Quandl, Xignite


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	# cursorclass=pymysql.cursors.DictCursor
	)
c = conn.cursor()


#Set Date range somehow (1/1/2007 to 2/28/2017)
#Iterate through list of trading dates here??? to input into SQL statements
start = "2007-01-02"
end = "2017-02-28"


#####################################################################
############################  USER CLASS  ###########################
#####################################################################

class Users():
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


#Takes 3.65 seconds for all filters to run
#15 minutes for 1 year
#select price.ticker from price where price.adj_close > 5 and price.date = '2017-03-28';
#takes 0.12 sec to run
class LastPriceFilter(Filter):
	def __init__(self, lp_low, lp_high, end_date):
		self.lp_low = lp_low
		self.lp_high = lp_high
		self.end_date = end_date

	def screen(self, tickers=None):
		# build query
		query = '''
			SELECT DISTINCT price.ticker_id 
			FROM price 
			WHERE price.adj_close > %s 
			AND price.adj_close < %s 
			AND price.date = %s
		''' #this is a string

		if tickers:
			query += " and price.ticker_id IN " + str(tickers)

		c.execute('''
			SELECT DISTINCT price.ticker_id 
			FROM price 
			WHERE price.adj_close > %s 
			AND price.adj_close < %s 
			AND price.date = %s;
		''', (self.lp_low, self.lp_high, self.end_date)) #how to deal with no high or no low?
		# print (ticker_ids)

		# c.execute('''SELECT DISTINCT ticker.symbol FROM ticker WHERE ticker.id = ticker_ids;''')
		rows = c.fetchall() #returns list of tuples ( should i run set() on this list now? )
		# for r in rows:
		# 	print (r)
		return rows


last_price = LastPriceFilter(5, 9999, '2017-03-22')
# print (last_price.run())
print (last_price.run())

#SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pCURRENTRATIO) WHERE fundamental.value > 2.0 and fundamental.date > '2016-12-22' and fundamental.date < '2017-03-22';
#takes 0.53 sec to run
# class CurrentRatioFilter(Filter):
# 	name = "current-ratio"
# 	required = False
# 	parameter_names = [""]

# 	def __init__(self, cr_high, cr_low, begin_date, end_date):
# 		self.cr_high = cr_high
# 		self.cr_low = cr_low
# 		self.begin_date = begin_date
# 		self.end_date = end_date

# 	def screen(self):
# 		c.execute('''SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pCURRENTRATIO) WHERE fundamental.value > %s AND fundamental.value < %s and fundamental.date > '2016-03-15' and fundamental.date < '2016-06-15';''', (low, high, begin_date, end_date))
# 		return c.fetchall()


# # class PriceChange52WeekFilter(Filter):
# # 	def screen(self):
# # 		c.execute('''SELECT price.ticker FROM price WHERE ((price.adj_close - old_adj_close)/old_adj_close)*100) > %s AND ((price.adj_close - old_adj_close)/old_adj_close)*100) < %s;''', (low, high))
# # 		return c.fetchall() #How do I get the adj_close from one year ago???????


# #SELECT fundamental.ticker_id FROM fundamental PARTITION (pPE1) WHERE fundamental.value > 1.0 AND fundamental.value < 20.0 and fundamental.date > '2017-03-22';
# #takes 0.38 sec to run
# #This filter returns the fewest results **********
# class PriceEarningsFilter(Filter):
# 	def __init__(self, pe_high, pe_low, begin_date, end_date):
# 		self.pe_high = pe_high
# 		self.pe_low = pe_low
# 		self.begin_date = begin_date
# 		self.end_date = end_date

# 	def screen(self):
# 		c.execute('''SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pPE1) WHERE fundamental.value > %s AND fundamental.value < %s and fundamental.date > '%s';''', (low, high, begin_date, end_date))
# 		return c.fetchall()


# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pEPS) WHERE fundamental.value > 0.5 and fundamental.date = '2017-03-22';
# #takes 1.08 sec to run
# class EarningsPerShareFilter(Filter):
# 	def __init__(self, eps_high, eps_low, begin_date, end_date):
# 		self.eps_high = eps_high
# 		self.eps_low = eps_low
# 		self.begin_date = begin_date
# 		self.end_date = end_date

# 	def screen(self):
# 		c.execute('''SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pEPS) WHERE fundamental.value > %s AND fundamental.value < %s and fundamental.date > '%s' and fundamental.date < '%s';''', (low, high, begin_date, end_date))
# 		return c.fetchall()


# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pROE) WHERE fundamental.value > 10.0 and fundamental.date > '2016-05-22' and fundamental.date < '2016-08-22';
# #takes 0.33 sec to run
# class ReturnOnEquity(Filter):
# 	def __init__(self, roe_high, roe_low, begin_date, end_date):
# 		self.roe_high = roe_high
# 		self.roe_low = roe_low
# 		self.begin_date = begin_date
# 		self.end_date = end_date

# 	def screen(self):
# 		c.execute('''SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pROE) WHERE fundamental.value > %s AND fundamental.value < %s and fundamental.date > '%s' and fundamental.date < '%s';''', (low, high, begin_date, end_date))
# 		return c.fetchall()


# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pROIC) WHERE fundamental.value > 15.0 and fundamental.date > '2016-05-22' and fundamental.date < '2016-08-22';
# #takes 0.33 sec to run
# class ReturnOnInvestedCapitalFilter(Filter):
# 	def __init__(self, roic_high, roic_low, begin_date, end_date):
# 		self.roic_high = roic_high
# 		self.roic_low = roic_low
# 		self.begin_date = begin_date
# 		self.end_date = end_date

# 	def screen(self):
# 		c.execute('''SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pROIC) WHERE fundamental.value > %s AND fundamental.value < %s and fundamental.date > '%s' and fundamental.date < '%s';''', (low, high, begin_date, end_date))
# 		return c.fetchall()


# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pDIVYIELD) WHERE fundamental.value > 0.5 and fundamental.date > '2016-05-22' and fundamental.date < '2016-08-22';
# #takes 0.36 sec to run
# class DividendYieldFilter(Filter):
# 	def __init__(self, dy_high, dy_low, begin_date, end_date):
# 		self.dy_high = dy_high
# 		self.dy_low = dy_low
# 		self.begin_date = begin_date
# 		self.end_date = end_date

# 	def screen(self):
# 		c.execute('''SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pDIVYIELD) WHERE fundamental.value > %s AND fundamental.value < %s and fundamental.date > '%s' and fundamental.date < '%s';''', (low, high, begin_date, end_date))
# 		return c.fetchall()


# #SELECT distinct fundamental.ticker_id FROM fundamental PARTITION (pDE) WHERE fundamental.value > 0.0 and fundamental.value < 0.25 and fundamental.date > '2016-05-22' and fundamental.date < '2016-08-22';
# #takes 0.49 sec to run
# class DebtToEquityFilter(Filter):
# 	def __init__(self, de_high, de_low, begin_date, end_date):
# 		self.de_high = de_high
# 		self.de_low = de_low
# 		self.begin_date = begin_date
# 		self.end_date = end_date

# 	def screen(self):
# 		c.execute('''SELECT DISTINCT fundamental.ticker_id FROM fundamental PARTITION (pDE) WHERE fundamental.value > %s AND fundamental.value < %s and fundamental.date > '%s' and fundamental.date < '?';''', (low, high, begin_date, end_date))
# 		return c.fetchall()


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







