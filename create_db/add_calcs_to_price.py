import pandas as pd
import numpy as np
import timeit
import csv

#Begin timer
start = timeit.default_timer()


# df = pd.read_csv("../data/prices2.csv")
# df = pd.read_csv("price_output_copy.csv")
df = pd.read_csv("price_output_9.csv")


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


# RELATIVE STRENGTH
df['rs'] = df['avg_gain'] / abs(df['avg_loss'])


# DELETE COLUMNS
# df = df.drop('avg_gain', 1)
# df = df.drop('avg_loss', 1)


# AVG GAIN / LOSS
# df['avg_gain'] = df.groupby('ticker')['gain'].rolling(14).mean().reset_index(0, drop=True).fillna(method='bfill')
# df['avg_loss'] = df.groupby('ticker')['loss'].rolling(14).mean().reset_index(0, drop=True).fillna(method='bfill')


# TRIM CSV FILE
# keep_cols = ['ticker', 'date', 'adj_close', 'adj_volume', 'volume_change', 'price_change', 'gain', 'loss']
# new_df = df[keep_cols]
# new_df.to_csv('price_output_5.csv', index = False)


# ASSIGN EMPTY COLUMNS TO DATAFRAME
# df['avg_gain'] = 0
# df['avg_loss'] = 0
# df.loc[0, 'avg_gain'] = 0
# df.loc[0, 'avg_loss'] = 0




df.to_csv('price_output_10.csv', index = False)


#COLUMN HEADINGS
print ("This is price_output_9\n")
print (list(df.columns.values))
print (df[:30])
#['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'ex-dividend', 'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )






















# doesnt work bc avg_gain is part of new column
# AVG GAIN / LOSS
# df['avg_gain'] = np.where( (df['ticker'] == df['ticker'].shift(1)), ( ( df['avg_gain'].shift(1) * 13 ) + df['gain'] ) / 14, 0 )


# THIS WORKS BUT IS VERY SLOW - MAYBE TRY TO ADD CDEF TO CPYTHON FILE
# counter = 0
# prev_ticker = ''
# last_avg_gain = 0

# for row in df.itertuples():

# 	if row.ticker == prev_ticker:
# 		df.loc[row.Index, 'avg_gain'] = ( (last_avg_gain * 13) + row.gain ) / 14
# 	else:
# 		df.loc[row.Index, 'avg_gain'] = 0

# 	prev_ticker = row.ticker
# 	last_avg_gain = df.loc[row.Index, 'avg_gain']

# 	# print (row.ticker, row.gain, row.avg_gain)

# 	counter += 1
# 	# if counter == 20:
# 	# 	break
# 	if counter % 100 == 0:
# 		print ("Percent complete = ", counter / 14663500)




# counter = 0
# for row in range(1, len(df):
# 	if df.loc[row, 'ticker'] == df.loc[row-1, 'ticker']:
# 		df.loc[row, 'avg_gain'] = ((df.loc[row-1, 'avg_gain'] * 13) + df.loc[row, 'gain']) / 14
# 	else:
# 		df.loc[row, 'avg_gain'] = 0
# 	counter += 1
# 	if counter % 100 == 0:
# 		print ("Percent complete = ", counter / 14663500)


# counter = 0
# prev_tick = 0
# prev_avg_gain = 0
# for row in list(zip(df['ticker'], df['gain'], df['avg_gain'])):
# 	if row[0] == prev_tick:
# 		row[2] = ((prev_avg_gain * 13) + row[1]) / 14
# 	else:
# 		row[2] = 0
# 	prev_tick = row[0]
# 	prev_avg_gain = row[2]
# 	counter += 1
# 	if counter % 100 == 0:
# 		print ("Percent complete = ", counter / 14663500)


# counter = 0
# for row, group in grouped:
# 	# if group.loc[symbol, 'ticker'] == group.loc[symbol-1, 'ticker']:
# 	if group.loc[row-1, 'avg_gain']:
# 		group.loc[row, 'avg_gain'] = ((group.loc[row-1, 'avg_gain'] * 13) + group.loc[row, 'gain']) / 14
# 	else:
# 		group.loc[row, 'avg_gain'] = 0
# 	counter += 1
# 	if counter % 100 == 0:
# 		print ("Percent complete = ", counter / 14663500)


# THIS WORKED BUT WAS VERY SLOW !!!
# counter = 0
# for row in range(1, len(df)):
# 	if df.loc[row, 'ticker'] == df.loc[row-1, 'ticker']:
# 		df.loc[row, 'avg_gain'] = ((df.loc[row-1, 'avg_gain'] * 13) + df.loc[row, 'gain']) / 14
# 	else:
# 		df.loc[row, 'avg_gain'] = 0
# 	counter += 1
# 	if counter % 100 == 0:
# 		print ("Percent complete = ", counter / 14663500)


# df['avg_loss'] = np.where( (df['ticker'] == df['ticker'].shift(1)), ( ( df['avg_loss'].shift(1) * 13 ) + df['loss'] ) / 14, 0 )









