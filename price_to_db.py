import pymysql.cursors
import pandas as pd
import numpy as np
import timeit
import csv


#Begin timer
start = timeit.default_timer()

#Create connection to db
conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)

cursor = conn.cursor()

#Fundamentals.csv file is so large that we have to break into 10000 line chunks
#Overloads 8gb memory of my MacbookAir


df_price_reader = pd.read_csv(
	"data/prices.csv",
	usecols=['ticker', 'date', 'adj_close', 'adj_volume'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)

# df_prices_2005 = df_price_reader[ (df_price_reader['date']) > '2004-12-31' ]

# df_price_reader = pd.read_csv(
# 	"data/prices.csv",
# 	usecols=['ticker', 'date', 'adj_close', 'adj_volume'],
# 	chunksize=10000,
# 	low_memory=True,
# 	engine='c'
# )

# df_prices_2005 = df_price_reader[ (df_price_reader['date']) > '2004-12-31' ]


def parse_val(val):
	if isinstance(val, np.float64):
		return 0.0 if np.isnan(val) else float(val)
	elif isinstance(val,np.int64):
		return int(val)
	else:
		return val

#Split 1st column of csv into 3 columns (ticker, indicator, dimension)
#Convert each chunk to a unique list
counter = 0

for chunk in df_price_reader:
	cursor.executemany('''
		INSERT INTO price (
		ticker_id,
		ticker,
		date,
		adj_close,
		adj_volume) 
		VALUES (1,%s,%s,%s,%s);''',
		(
			[str(parse_val(row[idx])) for idx in range(1,len(row))]
			for row in chunk.itertuples()
		)
	)
	conn.commit()

	counter += 1
	print ("Counter = ", counter)

conn.close()



stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )
# Seconds to run:  4928.409679741992





# counter = 0

# for chunk in df_prices_2005:
# 	cursor.executemany('''
# 		INSERT INTO price (
# 		ticker_id,
# 		ticker,
# 		date,
# 		open,
# 		high,
# 		low,
# 		close,
# 		volume,
# 		ex_dividend,
# 		split_ratio,
# 		adj_open,
# 		adj_high,
# 		adj_low,
# 		adj_close,
# 		adj_volume) 
# 		VALUES (1,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',
# 		(
# 			[str(parse_val(row[idx])) for idx in range(1,len(row))]
# 			for row in chunk.itertuples()
# 		)
# 	)
# 	conn.commit()

# 	counter += 1
# 	print ("Counter = ", counter)

# conn.close()







#Split 1st column of csv into 3 columns (ticker, indicator, dimension)
#Convert each chunk to a unique list
# counter = 0
# # tickers = []
# # counterx = 0
# for chunk in df_price_reader:

# 	# if counter % 6 == 0:
# 	# 	counterx += 1
# 	# 	print ("CounterX = ", counterx)
# 	# 	conn.close()
# 	# 	conn = pymysql.connect(host='localhost',
# 	# 		user='scox',
# 	# 		password='scox',
# 	# 		db='trading_algo',
# 	# 		charset='utf8mb4',
# 	# 		cursorclass=pymysql.cursors.DictCursor
# 	# 		)
# 	# 	cursor = conn.cursor()
# 	# else:
# 	# counter += 1
# 	# print ("Counter = ", counter)
# 	# # chunk_df = list(chunk)
# 	# # chunk_list = list(set(ticker_chunk_df))
# 	# # chunk_transposed = chunk.transpose()
# 	cursor.executemany('''
# 		INSERT INTO price (
# 		ticker_id,
# 		ticker,
# 		date,
# 		open,
# 		high,
# 		low,
# 		close,
# 		volume,
# 		ex_dividend,
# 		split_ratio,
# 		adj_open,
# 		adj_high,
# 		adj_low,
# 		adj_close,
# 		adj_volume) 
# 		VALUES (1,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',
# 		chunk.itertuples()
# 	)
# 	conn.commit()
# 	# for row in chunk.itertuples():
# 	# 	# col_transposed = chunk[col].transpose()
# 	# 	for i in range(1, 15):
# 	# 		print ("Type = ", type(float(row[i])), row[i])
# 		# print (row[1], row[2], row[3]) #this prints the specific values of column 7
# 		# print (col_transposed) #this prints values of each columns 10000 by 10000
# 		# print (chunk.ix[0])
# 		# cursor.executemany('''
# 		# 	INSERT INTO price (
# 		# 	ticker_id,
# 		# 	ticker,
# 		# 	date,
# 		# 	open,
# 		# 	high,
# 		# 	low,
# 		# 	close,
# 		# 	volume,
# 		# 	ex_dividend,
# 		# 	split_ratio,
# 		# 	adj_open,
# 		# 	adj_high,
# 		# 	adj_low,
# 		# 	adj_close,
# 		# 	adj_volume) 
# 		# 	VALUES (1,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',
# 		# 	(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
# 		# )
# 		# conn.commit()
# conn.close()




