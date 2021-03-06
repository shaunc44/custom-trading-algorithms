import pandas as pd
import numpy as np
import timeit
import csv

#Begin timer
start = timeit.default_timer()



df = pd.read_csv("price_output_final.csv")


# DELETE COLUMNS
# df = df.drop('gain', 1)
# df = df.drop('loss', 1)
# df = df.drop('avg_gain', 1)
# df = df.drop('avg_loss', 1)
# df = df.drop('price_chg_abs', 1)
# df = df.drop('rs', 1)

# ADD HEADERS TO DATAFRAME
# df = pd.read_csv("price_output_9.csv")
# df.columns = ['ticker', 'date', 'adj_close', 'adj_volume', 'volume_chg_pct', 'price_chg_pct', 'price_chg_abs', 'gain', 'loss', 'avg_gain', 'avg_loss']
# df.columns = ['ticker', 'date', 'adj_close', 'adj_volume', 'volume_chg_pct', 'price_chg_pct', 'rsi']


# REPLACE ALL INF WITH NANS
df2 = df.replace( [np.inf, -np.inf], 0 )


# REPLACE ALL INF WITH NANS
# df3 = df2.replace( np.nan, 0 )


# VOLUME CHANGE
# df['volume_change'] = np.where( df['ticker'] == df['ticker'].shift(1), ((df['adj_volume'] / df['adj_volume'].shift(1)) - 1) * 100, 0 )
# df.to_csv('price_output.csv')


# PRICE CHANGE
# df['price_chg_pct'] = np.where( df['ticker'] == df['ticker'].shift(1), ((df['adj_close'] / df['adj_close'].shift(1)) - 1) * 100, 0 )
# df['price_chg_abs'] = np.where( df['ticker'] == df['ticker'].shift(1), (df['adj_close'] - df['adj_close'].shift(1)), 0 )


# GAIN / LOSS
# df['gain'] = np.where( df['price_chg_abs'] > 0, df['price_chg_abs'], 0 )
# df['loss'] = np.where( df['price_chg_abs'] < 0, df['price_chg_abs'], 0 )


# RELATIVE STRENGTH
# df['rs'] = df['avg_gain'] / abs(df['avg_loss'])


# RELATIVE STRENGTH INDICATOR
# df['rsi'] = 100 - ( 100 / ( 1 + df['rs'] ) )


# AVG GAIN / LOSS
# df['avg_gain'] = df.groupby('ticker')['gain'].rolling(14).mean().reset_index(0, drop=True).fillna(method='bfill')
# df['avg_loss'] = df.groupby('ticker')['loss'].rolling(14).mean().reset_index(0, drop=True).fillna(method='bfill')


# RSI AVG GAIN / LOSS
# df['rsi_avg_gain'] = np.where( df['ticker'] == df['ticker'].shift(1), ( ((df['avg_gain'].shift(1) * 13) + df['gain']) / 14 ), 0 )
# df['rsi_avg_loss'] = np.where( df['ticker'] == df['ticker'].shift(1), ( ((df['avg_loss'].shift(1) * 13) + df['loss']) / 14 ), 0 )


# TRIM CSV FILE
# keep_cols = ['ticker', 'date', 'adj_close', 'adj_volume', 'volume_change', 'price_chg_pct', 'price_chg_abs', 'gain', 'loss']
# new_df = df[keep_cols]
# new_df.to_csv('price_output_8.csv', index = False)


# ASSIGN EMPTY COLUMNS TO DATAFRAME
# df['avg_gain'] = 0
# df['avg_loss'] = 0
# df.loc[0, 'avg_gain'] = 0
# df.loc[0, 'avg_loss'] = 0


# df.to_csv('price_output_final2.csv', index = False)


#COLUMN HEADINGS
# print ("This is price_output_8\n")
print (list(df.columns.values))
# print (df[:20])
print (df[-30:])



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






#CYTHON EXAMPLE
# import pandas as pd
# #import numpy as np
# #import timeit
# import csv
# import os


# #start = timeit.default_timer()


# df = pd.read_csv("../price_output_7.csv")

# cdef int counter
# cdef str prev_ticker
# cdef double last_avg_gain

# counter = 0
# prev_ticker = 'sampleticker'
# last_avg_gain = 0

# for row in df.itertuples():
# 	if row.ticker == prev_ticker:
# 		df.loc[row.Index, 'avg_gain'] = ( (last_avg_gain * 13) + row.gain ) / 14
# 	else:
# 		df.loc[row.Index, 'avg_gain'] = 0
# 	prev_ticker = row.ticker
# 	last_avg_gain = df.loc[row.Index, 'avg_gain']
# 	print (last_avg_gain)
# 	counter += 1
# 	print ("Counter = ", counter)
	#with open("out1.csv", a, newline='') as f:
	#	writer = csv.writer(f)

	#os.system('')


#df.to_csv('price_output_8.csv', index = False)


#stop = timeit.default_timer()
#print ("Seconds to run: ", (stop - start) )





