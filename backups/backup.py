import pymysql.cursors
import csv
import pandas as pd
import time
import os
# import xlrd

# secret_pw = os.system("cat pwf")

conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='bigdump',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)

cursor = conn.cursor()

#READ PRICE FILE AND CREATE DATAFRAME
# df = pd.read_csv("data/historical_stock_prices2.csv")
# ticker_df = df['ticker'].tolist()
# ticker_set = set(ticker_df)
# ticker_list = list(ticker_set)
# print ("Tickers List: ", ticker_list)
# print ("Number of Tickers: ", len(ticker_list))
# ldf = list(df)
# sdf = set(ldf)
# xdf = list(sdf)


#CONVERT TICKER LIST TO TICKER_LIST CSV FILE
# pd_list = pd.DataFrame(ticker_list)
# pd_list.to_csv("ticker_list4.csv")


#CONVERT EXCEL TO PANDAS DF
# excel1 = pd.ExcelFile("ticker_list2.xlsx")
# ticker_df = excel1.parse("ticker_list2")
# print (ticker_df)

# ticker_df = pd.read_excel('ticker_list3.xlsx', sheetname="ticker_list3")
# print (ticker_df[1])
# ticker_df = ticker_df[1].tolist()
# ticker_set = set(ticker_df)
# ticker_list = list(ticker_set)
# print ("Tickers List: ", ticker_list)
# print ("Number of Tickers: ", len(ticker_list))

with open("ticker_list3.csv") as file:
	# file.read()
	for ticker in file:
		print (ticker)



# with open("data/historical_stock_prices2.csv") as file:
# 	# prices = file.read()
# 	for _ in file:
# 		print (_)
# 		# print (type(_))
# 		time.sleep(1)
		# print ("All okay")
		# print (_[0])
		# print (_[1])
		# print (_[2])
		# print (_[3])

		# cursor.execute('select * from dump1;')


#ticker,date,open,high,low,close,volume,ex-dividend,split_ratio,adj_open,adj_high,adj_low,adj_close,adj_volume

# ticker,date,open,high,low,close,volume,ex-dividend,split_ratio,adj_open,adj_high,adj_low,adj_close,adj_volume