import pymysql.cursors
import pandas as pd
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
	# names = ['ticker', 'date', 'value'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)

#Create function to split quandl code (AAPL_REVENUE_MRQ) into 3 columns
# def parse_code(value): 
# 	code = value.split("_")
# 	if len(code) == 3: return code
# 	return code + [""]


#Split 1st column of csv into 3 columns (ticker, indicator, dimension)
#Convert each chunk to a unique list
counter = 0
# tickers = []
for chunk in df_price_reader:
	# print (chunk)
	counter += 1
	print ("Counter = ", counter)
	# chunk_df = list(chunk)
	# chunk_list = list(set(ticker_chunk_df))
	chunk_transposed = chunk.transpose()
	for row in chunk_transposed:
		print (row)
		# print (row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
		# print ("Type = ", type(ticker)," ", ticker)
		# cursor.execute('''
		# 	INSERT INTO price (
		# 	ticker,
		# 	date,
		# 	open,
		# 	high,
		# 	low,
		# 	close,
		# 	volume,
		# 	ex_dividend,
		# 	split_ratio,
		# 	adj_open,
		# 	adj_high,
		# 	adj_low,
		# 	adj_close,
		# 	adj_volume) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}");'''.format(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
		# )
	# 	conn.commit()
	# conn.close()





	# chunk['ticker'], chunk['indicator'], chunk['dimension'] = zip( *chunk['ticker'].map(parse_code) )
	# ticker_chunk_df = chunk['ticker'].tolist()
	# ticker_chunk_list = list(set(ticker_chunk_df))
	# counter += 1
	# print ("Counter = ", counter)
	# for i in ticker_chunk_list:
	# 	tickers.append(i)
	# 	tickers = list(set(tickers))
	# 	print (tickers)


#Store unique ticker list in a csv file
# pd_tickers_list = pd.DataFrame(tickers)
# pd_tickers_list.to_csv("ticker_list4.csv")



stop = timeit.default_timer()

print ("Seconds to run: ", (stop - start) )





