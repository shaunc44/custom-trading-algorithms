import pandas as pd
import timeit
import csv


#Begin timer
start = timeit.default_timer()


#Fundamentals.csv file is so large that we have to break into 10000 line chunks
#Overloads 8gb memory of my MacbookAir
df_reader = pd.read_csv(
	"data/fundamentals.csv",
	names = ['ticker', 'date', 'value'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)


#Create function to split quandl code (AAPL_REVENUE_MRQ) into 3 columns
def parse_code(value): 
	code = value.split("_")
	if len(code) == 3: return code
	return code + [""]


#Split 1st column of csv into 3 columns (ticker, indicator, dimension)
#Convert each chunk to a unique list
counter = 0
tickers = []
for chunk in df_reader:
	chunk['ticker'], chunk['indicator'], chunk['dimension'] = zip( *chunk['ticker'].map(parse_code) )
	ticker_chunk_df = chunk['ticker'].tolist()
	ticker_chunk_list = list(set(ticker_chunk_df))
	counter += 1
	print ("Counter = ", counter)
	for i in ticker_chunk_list:
		tickers.append(i)
		tickers = list(set(tickers))
		print (tickers)


#Store unique ticker list in a csv file
pd_tickers_list = pd.DataFrame(tickers)
pd_tickers_list.to_csv("ticker_list4.csv")


stop = timeit.default_timer()

print ("Seconds to run: ", (stop - start) )
#Seconds to run:  473.1752427579995

