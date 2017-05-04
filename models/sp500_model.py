import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta

# ==============================1 year==========================================================
def get_sp(startdate, enddate, step):
	end_date = date.today()
	start_date = day
	sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	adj = sp['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returnss =returns[::step]
	returns_list = returnss.tolist()
	short_list = []
	for i in returns_list:
		short = round(i,2)
		short_list.append(short)
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	final_date_list = date_list[::step]
	# sp_name = ['S&P500']
	# sp_final = sp_name+short_list
	# date_name = ['Dates']
	# final_date = date_name+date_list

	# print ( dict(date_list=final_date, adj_list=sp_final) )
	print ( dict(date_list=date_list, adj_list=short_list) )

# get_sp(365, 1)