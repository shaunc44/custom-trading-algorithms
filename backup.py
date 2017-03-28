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

cursor = conn.cursor()


df = pd.read_csv("data/historical_stock_prices2.csv")
ticker_df = df['ticker'].tolist()
ticker_set = set(ticker_df)
ticker_list = list(ticker_set)
# print ("Tickers List: ", ticker_list)
# print ("Number of Tickers: ", len(ticker_list))
# ldf = list(df)
# sdf = set(ldf)
# xdf = list(sdf)

for symbol in ticker_list:
	os.system("'{}' >> set_symbols.csv".format(symbol))
	print (symbol)
# 	cursor.execute('''
# create table {} (
# `id` INT AUTO_INCREMENT,
# `date` VARCHAR(128),
# `open`  FLOAT,
# `high` FLOAT,
# `low` FLOAT,
# `close` FLOAT,
# `volume` FLOAT,
# `ex-dividend` FLOAT,
# `split_ratio` FLOAT,
# `adj_open` FLOAT,
# `adj_high` FLOAT,
# `adj_low` FLOAT,
# `adj_close` FLOAT,
# `adj_volume` FLOAT,
# PRIMARY KEY (`id`)
# );'''.format(symbol)
# 	)

# for symbol in ticker_list:
# 	cursor.execute('''
# DROP TABLE IF EXISTS `bigdump`.`{}`;
# create table {} (
# `id` INT AUTO_INCREMENT,
# `date` VARCHAR(128),
# `open`  FLOAT,
# `high` FLOAT,
# `low` FLOAT,
# `close` FLOAT,
# `volume` FLOAT,
# `ex-dividend` FLOAT,
# `split_ratio` FLOAT,
# `adj_open` FLOAT,
# `adj_high` FLOAT,
# `adj_low` FLOAT,
# `adj_close` FLOAT,
# `adj_volume` FLOAT,
# PRIMARY KEY (`id`)
# );'''.format(symbol)
# 	)

# for _ in xdf:
# 	print (type(_))


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