import pandas as pd
import numpy as np
import timeit
import csv

#Begin timer
start = timeit.default_timer()


# df = pd.read_csv("../data/prices2.csv")
# df = pd.read_csv("price_output_copy.csv")
df = pd.read_csv("price_output_6.csv")


# VOLUME CHANGE
# df['volume_change'] = np.where( df['ticker'] == df['ticker'].shift(1), ((df['adj_volume'] / df['adj_volume'].shift(1)) - 1) * 100, 0 )
# df.to_csv('price_output.csv')


# PRICE CHANGE
# df['price_change'] = (( df['adj_close'] / df['adj_open'] ) - 1) * 100
# df.to_csv('price_output_2.csv')


# GAIN / LOSS
# df['gain'] = np.where( df['price_change'] > 0, df['price_change'], 0 )
# df['loss'] = np.where( df['price_change'] < 0, df['price_change'], 0 )
# df.to_csv('price_output_3.csv')r


these calcs are wrong; need to factor in avg_gain / loss
# AVG GAIN / LOSS
# df['avg_gain'] = np.where( (df['ticker'] == df['ticker'].shift(1)), ( ( df['gain'].shift(1) * 13 ) + df['gain'] ) / 14, 0 )
# df['avg_loss'] = np.where( (df['ticker'] == df['ticker'].shift(1)), ( ( df['loss'].shift(1) * 13 ) + df['loss'] ) / 14, 0 )


# TRIM CSV FILE
# keep_cols = ['ticker', 'date', 'adj_close', 'adj_volume', 'volume_change', 'price_change', 'gain', 'loss']
# new_df = df[keep_cols]
# new_df.to_csv('price_output_5.csv', index = False)


# df.to_csv('price_output_6.csv', index = False)


# df['rs'] = 
# df['rsi'] = 

# df['volume_change'] = [ (((df['adj_volume'] / df['adj_volume'].shift(-1)) - 1) * 100) if df['ticker'] == df['ticker'].shift(-1) else 0 for x in df ]

# counter = 0
# temp = ''
# for x in df:
	# print (x)
	# print (x['ticker'])
	# print print
# 	counter += 1
# if df['ticker'].any() == temp:
# if df['ticker'] == df['ticker'].shift(-1):
# 	df['price_change'] = df['adj_close'] / df['adj_close'].shift(-1)
# else:
# 	df['price_change'] = 0
# if counter % 10000 == 0:
# 	print ("Percent complete: ", counter * 10000 / 14663457)
# temp = df['ticker']


# # df['price_change'] = df['adj_close'] / df['adj_open']
# df.to_csv('price_output3.csv')



# # df['rsi'] = df['adj_close']/df['adj_close']

#COLUMN HEADINGS
print (list(df.columns.values))
print (df[-5:])
#['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'ex-dividend', 'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )






