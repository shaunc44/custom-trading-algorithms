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
	cursorclass=pymysql.cursors.DictCursor
	)
c = conn.cursor


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
	def __init__(self, high, low, date):
		self.high = high
		self.low = low
		self.date = date

	def run(self):
		self.screen()


#select price.ticker from price where price.adj_close > 5 and price.date = '2017-03-28';
#takes 7 sec to run
class LastPriceFilter(Filter):
	def screen(self):
		c.execute('''SELECT price.ticker FROM price WHERE price.adj_close > ? AND price.adj_close < ? and price.date = '?';''', (low, high, date)) #how to deal with no high or no low?
		return c.fetchall() #returns list of tuples ( should i run set() on this list now? )


#select distinct fundamental.ticker from fundamental where fundamental.indicator = 'CURRENTRATIO' and fundamental.value > 2.0 and date > '2017-01-01';
#takes 56 sec to run ????
class CurrentRatioFilter(Filter):
	def screen(self):
		c.execute('''SELECT DISTINCT fundamental.ticker FROM fundamental WHERE fundamental.indicator = 'CURRENTRATIO' AND fundamental.value > ? AND fundamental.value < ?;''', (low, high))
		return c.fetchall()


class PriceChange52WeekFilter(Filter):
	def screen(self):
		c.execute('''SELECT price.ticker FROM price WHERE ((price.adj_close - old_adj_close)/old_adj_close)*100) > ? AND ((price.adj_close - old_adj_close)/old_adj_close)*100) < ?;''', (low, high))
		return c.fetchall() #How do I get the adj_close from one year ago???????


class PriceEarningsFilter(Filter):
	def screen(self):
		c.execute('''SELECT fundamental.ticker FROM fundamental WHERE fundamental.indicator = 'PE1' AND fundamental.value > ? AND fundamental.value < ?;''', (low, high))
		return c.fetchall()


class EarningsPerShareFilter(Filter):
	def screen(self):
		c.execute('''SELECT fundamental.ticker FROM fundamental WHERE fundamental.indicator = 'EPS' AND fundamental.value > ? AND fundamental.value < ?;''', (low, high))
		return c.fetchall()


class ReturnOnEquity(Filter):
	def screen(self):
		c.execute('''SELECT fundamental.ticker FROM fundamental WHERE fundamental.indicator = 'ROE' AND fundamental.value > ? AND fundamental.value < ?;''', (low, high))
		return c.fetchall()


class ReturnOnInvestedCapitalFilter(Filter):
	def screen(self):
		c.execute('''SELECT fundamental.ticker FROM fundamental WHERE fundamental.indicator = 'ROIC' AND fundamental.value > ? AND fundamental.value < ?;''', (low, high))
		return c.fetchall()


class DividendYieldFilter(Filter):
	def screen(self):
		c.execute('''SELECT fundamental.ticker FROM fundamental WHERE fundamental.indicator = 'DIVYIELD' AND fundamental.value > ? AND fundamental.value < ?;''', (low, high))
		return c.fetchall()


class DebtToEquityFilter(Filter):
	def screen(self):
		c.execute('''SELECT fundamental.ticker FROM fundamental WHERE fundamental.indicator = 'DE' AND vfundamental.alue > ? AND fundamental.value < ?;''', (low, high))
		return c.fetchall()


# @classmethod
# 	def screen(cls, lp_hi, lp_low, cr_hi, cr_lo, ftwpc_hi, ftwpc_lo, param, param, param, param, param, param, param, param, param, param, param, param, ):
		

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
class Screen:
	def __init__(self, *filters):
		self._filters = filters

	
	def run(self):
		for filter_ in self._filters:
			filter.screen()

my_filter = LastPriceFilter(6,7)
Screen(my_filter)


#Pull data from historical prices table



#####################################################################
##########################  BUY/SELL CLASS  #########################
#####################################################################

class BuySell():
	pass

	@classmethod
	def sma_50_200_crossover(cls, high, low):
		pass

	@classmethod
	def volume_change(cls, high, low):
		pass

	@classmethod
	def price_change(cls, high, low):
		pass

	@classmethod
	def divergence(cls, high, low):
		pass

	@classmethod
	def macd(cls, high, low):
		pass

	@classmethod
	def rsi(cls, high, low):
		pass

	@classmethod
	def trailing_stop_loss(cls, percent):
		pass






class Model():

	def initialize(context):
		#bring in init params
		pass

	def make_screen(context):
		#create dynamic stock selector
		pass

	def before_trading_start(context):
		#collect securities that passed the screen
		pass

	def purchase_stocks(context):
		pass

	def sell_stocks(context):
		pass

	def calculate_return(context):
		pass







