import pandas as pd
import numpy as np
import pandas_datareader.data as web
from datetime import date, timedelta
import datetime
import time


# def make_date_list(start_date, end_date):

# 	start_date = datetime.datetime.strptime(start_date, '%m/%d/%Y').date()
# 	# print ("Start ", start_date)
# 	end_date = datetime.datetime.strptime(end_date, '%m/%d/%Y').date()
# 	# print ("End ", end_date)

# 	num_days = (end_date - start_date).days
# 	# print ("Num Days ", num_days)
# 	date_list = [end_date - timedelta(days = x) for x in range(0, num_days)]

# 	date_list = date_list[::-1]

# 	date_list_unix = [time.mktime(my_date.timetuple()) * 1000 for my_date in date_list]
# 	# date_list2 = c
# 	return date_list_unix


# make_date_list('01/02/2007', '01/05/2007')



def get_sp(startdate, enddate, step=1):
	# end_date = enddate
	# start_date = startdate
	start_date= datetime.datetime.strptime(startdate, '%m/%d/%Y')
	end_date= datetime.datetime.strptime(enddate, '%m/%d/%Y')
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
	print ("Final Date List ", final_date_list)

	dt_list = [datetime.datetime.strptime(day, '%Y-%m-%d').date() for day in final_date_list]
	print ("dtList = ", dt_list)

	date_list_unix = [time.mktime(my_date.timetuple()) * 1000 for my_date in dt_list]

	# print ("DateList Unix ", date_list_unix)
	# sp_name = ['S&P500']
	# sp_final = sp_name+short_list
	# date_name = ['Dates']
	# final_date = date_name+date_list

	# print ( dict(date_list=final_date, adj_list=sp_final) )
	# return dict(adj_list=short_list)


get_sp('01/02/2007', '01/05/2007')



