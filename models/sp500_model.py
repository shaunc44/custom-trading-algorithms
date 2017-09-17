import pandas as pd
import numpy as np
import pandas_datareader.data as web
# from pandas_datareader import data, web
import datetime
from datetime import date, timedelta
import time

# ==============================1 year==========================================================
def get_sp(startdate, enddate, step=1):

	all_date_list = make_date_list(startdate, enddate)
	print ("All Date List = ", all_date_list)


	#Get S&P 500 prices from Yahoo
	start_date= datetime.datetime.strptime(startdate, '%m/%d/%Y')
	end_date= datetime.datetime.strptime(enddate, '%m/%d/%Y')
	sp = web.DataReader("SPY",'google', start_date, end_date)
	adj = sp['Close']
	# sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	# adj = sp['Adj Close']
	first_price = adj.iloc[0]
	returnss = adj[::step]
	returns_list = returnss.tolist()
	# returns_list = first_price.tolist()
	sp_short_list = []

	for i in returns_list:
		short = round(i,2)
		sp_short_list.append(short)

	datee = sp.index.values
	date_list = []

	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)

	final_date_list = date_list[::step]
	# print ("Final SP Date List ", final_date_list)

	dt_list = [datetime.datetime.strptime(day, '%Y-%m-%d').date() for day in final_date_list]
	# print ("SP Date List = ", dt_list)

	sp_date_list_unix = [time.mktime(my_date.timetuple()) * 1000 for my_date in dt_list]
	# print("Sp Date List unix = ", sp_date_list_unix)

	sp_vals = fill_list(sp_date_list_unix, sp_short_list, all_date_list)
	# print("SP Vals = ", sp_vals)

	fin_list = combined_list(sp_vals, all_date_list)

	return dict(adj_list=fin_list)



def make_date_list(start_date, end_date):
	start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
	start_date = (start_date - timedelta(days=1))
	# print ("Start ", start_date)
	end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
	# print ("End ", end_date)

	num_days = (end_date - start_date).days
	# print ("Num Days ", num_days)
	date_list = [end_date - timedelta(days = x) for x in range(0, num_days)]

	date_list = date_list[::-1]
	date_list_unix = [time.mktime(my_date.timetuple()) * 1000 for my_date in date_list]
	# date_list2 = c
	return date_list_unix


def fill_list(sp_dates, sp_vals, all_dates):
	all_date_len = len(all_dates)
	sp_date_len = len(sp_dates)
	date_len_diff = all_date_len - sp_date_len

	counter = 0
	while len(sp_vals) < len(all_dates):
		if len(sp_dates) == counter:
			sp_dates.append(all_dates[counter])
			sp_vals.append(sp_vals[counter-1])
			break
		else:
			if sp_dates[counter] == all_dates[counter]:
				counter += 1
			else:
				sp_vals.insert(counter, sp_vals[counter-1])
				sp_dates.insert(counter, all_dates[counter])
	# print ("All Date Len ", all_date_len)
	# print ("SP Date Len ", sp_date_len)
	return sp_vals


def combined_list(sp_vals, all_dates):
	sp_val_len = len(sp_vals)
	# sp_val_len = 251
	# shouldn't it equal the length of values collected? or days ran?
	# print ("\nSP_Val_Len =", sp_val_len, "\n")

	final_list = []
	# for i in range(0, 2):
	for i in range(0, sp_val_len):
		print ("i: ", i)
		final_list.append([ all_dates[i], sp_vals[i] ])
	return final_list






















