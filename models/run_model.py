import pymysql.cursors
import datetime as dt
from . import filter_model
from . import buy_model
from . import sell_model
from . import current_model
from . import remove_curr_val_model





class RunLoop:
	def __init__(self, rundate, enddate, lp_low, lp_high, pe_low, pe_high, dy_low, dy_high, rsi_buy, rsi_sell):
		self.rundate = rundate
		self.enddate = enddate
		self.lp_low = lp_low
		self.lp_high = lp_high
		self.pe_low = pe_low
		self.pe_high = pe_high
		self.dy_low = dy_low
		self.dy_high = dy_high
		self.rsi_buy = rsi_buy
		self.rsi_sell =rsi_sell

	def create_cursor(self):
		if hasattr(self, "conn"):
			return self.conn.cursor()
		else:
			self.conn = pymysql.connect(host='localhost',
				user='scox',
				password='scox',
				db='trading_algo',
				charset='utf8mb4',
			# cursorclass=pymysql.cursors.DictCursor
			)
			return self.conn.cursor()

	def run_loop(self):
		cursor = self.create_cursor()

		while self.rundate <= self.enddate: 
			print ("Rundate1 = ", self.rundate)
			# Create Master Filtered Table of Stocks to Buy
			add_filtered = filter_model.CreateFilteredList(cursor, self.lp_low, self.lp_high, self.pe_low, self.pe_high, self.dy_low, self.dy_high, self.rundate)
			add_filtered.create_filtered_list()

			# Create Purchased List of Stocks
			create_purchased = buy_model.CreatePurchasedList(cursor, self.rsi_buy, self.rundate)
			purchased = create_purchased.create_purchased_list()

			# Add Purchased Stocks to Portfolio
			add_purchased = buy_model.AddPurchasedToPortfolio(cursor, purchased)
			add_purchased.add_purchased_to_portfolio()

			# Add Current Price & Value to Portfolio
			add_current = current_model.AddCurrentDataToPortfolio(cursor, self.rundate)
			add_current.add_current_data()

			# Sell Stocks
			sell_stock = sell_model.SellStock(cursor, self.rsi_sell, self.rundate)
			sell_stock.sell_stock()

			# Remove current value for stocks sold
			remove_curr_val = remove_curr_val_model.RemoveCurrentValue(cursor, self.rundate)
			remove_curr_val.remove_curr_val_for_sold()


			#convert startdate string to datetime format
			self.rundate = dt.datetime.strptime(self.rundate, '%Y-%m-%d')
			print ("Rundate2 = ", self.rundate)
			#add 1 day to startdate to get next date
			self.rundate = self.rundate + dt.timedelta(days=1)
			print ("Rundate3 = ", self.rundate)
			#convert date to string format
			self.rundate = dt.datetime.strftime(self.rundate, '%Y-%m-%d')
			print ("Rundate4 = ", self.rundate)


