import pymysql.cursors
import csv
import pandas as pd
import time
import os

# secret_pw = os.system("cat pwf")

conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='bigdump',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)

# conn = pymysql.connect("stock_algo.db")
cursor = conn.cursor()
# df.to_sql("stock_algo", conn)


with open("data/stocks_eod_prices.csv", "rb") as file:
	# prices = file.read()
	for _ in file:
		print (_)
		time.sleep(1)
		# print ("All okay")
		print (_[0])
		# print (_[1])
		# print (_[2])
		# print (_[3])

		# cursor.execute('select * from dump1;')


#ticker,date,open,high,low,close,volume,ex-dividend,split_ratio,adj_open,adj_high,adj_low,adj_close,adj_volume

# ticker,date,open,high,low,close,volume,ex-dividend,split_ratio,adj_open,adj_high,adj_low,adj_close,adj_volume