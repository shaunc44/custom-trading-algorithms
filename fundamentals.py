import pymysql.cursors
import pandas as pd
import numpy as np
import timeit
import csv


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


df_reader = pd.read_csv(
	"data/fundamentals.csv",
	names = ['ticker', 'date', 'value'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)

# df = pd.read_csv("data/historical_stock_prices.csv", usecols=['ticker', 'date', 'adj_close', 'adj_volume'])

#COLUMN HEADINGS
# print (list(df.columns.values))
# ['AAAP_ACCOCI_ARQ', '2016-04-29', '0.0']

# SEPARATE 1ST COLUMN INTO 3 COLUMNS
# df = pd.DataFrame(df)
# df = pd.DataFrame(df.ix[:,0:1].split('_',1).tolist(), columns = ['ticker', 'indicator', 'dimension'])
# df = pd.DataFrame(df.ticker.str.split('_',1).tolist(), columns = ['ticker', 'indicator', 'dimension'])

def parse_code(value): 
	code = value.split("_")
	if len(code) == 3: return code
	return code + [""]

for chunk in df_reader:
	chunk['ticker'], chunk['indicator'], chunk['dimension'] = zip( *chunk['ticker'].map(parse_code) )
	print (chunk)
# print (df.head())
#CREATE DF WITH DATES GREATER THAN 2006
# df2007 = df[ (df['date']) > '2006-12-31' ]


#LENGTH OF FILE
# print (len(df.index)) # 94,575,737


#LAST TICKER SYMBOL
# print (df[:5]) #-- last ticker ZUMZ
# print (df2007[-5:])



stop = timeit.default_timer()

print ("Seconds to run: ", (stop - start) )




