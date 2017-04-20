import pandas as pd
import numpy as np
import timeit
import datetime as dt
import csv

#Begin timer
start = timeit.default_timer()


df = pd.read_csv("price_output_10.csv")
groups = df.groupby('ticker')


def wrap(first_avg_loss):
	prev = {
		"value": None
	}
	def calc(loss):
		if prev["value"] is not None:
			prev["value"] = ( loss + (prev["value"] * 13) ) / 14
		else:
			prev["value"] = first_avg_loss
		return prev["value"]
	return calc


my_df = None
print(dt.datetime.now())
for name, group in groups:
	avg_losses = group['loss'].rolling(window=14).mean().shift(-13)
	first_avg_loss = avg_losses.iloc[0]
	calc = wrap(first_avg_loss)
	print(name, dt.datetime.now())
	group['avg_loss'] = group['loss'].map(calc)
	group.to_csv('price_output_11.csv', index=False, header=False, mode='a')


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )

















# import pandas as pd
# import numpy as np
# import timeit
# import datetime as dt
# import csv

# #Begin timer
# start = timeit.default_timer()


# # df = pd.read_csv("price_output_7.csv")
# df = pd.read_csv("price_output_10.csv")
# groups = df.groupby('ticker')


# def wrap(initial):
# 	prev = {
# 		"value": initial
# 	}
# 	def calc(loss):
# 		prev["value"] = ( loss + (prev["value"] * 13) ) / 14
# 		return prev["value"]
# 	return calc


# # my_df = None
# print(dt.datetime.now())
# for name, group in groups:
# 	calc = wrap(0)
# 	print(name, dt.datetime.now())
# 	group['avg_loss'] = group['loss'].map(calc)
# 	group.to_csv('price_output_11.csv', index=False, header=False, mode='a')


# #COLUMN HEADINGS
# # print ("This is price_output_8\n")
# # print (list(df.columns.values))
# # # print (df[-30:])
# # print (df[:30])
# #['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'ex-dividend', 'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']


# stop = timeit.default_timer()
# print ("Seconds to run: ", (stop - start) )












# df['avg_loss'] = np.where( (df['ticker'] == df['ticker'].shift(1)), ( ( df['avg_loss'].shift(1) * 13 ) + df['loss'] ) / 14, 0 )


# THIS WORKED BUT WAS VERY SLOW !!!
# counter = 0
# for row in range(1, len(df)):
# 	if df.loc[row, 'ticker'] == df.loc[row-1, 'ticker']:
# 		df.loc[row, 'avg_gain'] = ((df.loc[row-1, 'avg_gain'] * 13) + df.loc[row, 'gain']) / 14
# 	else:
# 		df.loc[row, 'avg_gain'] = 0
# 	counter += 1
# 	if counter % 1000 == 0:
# 		print ("Percent complete = ", counter / 14663500)


# TRIM CSV FILE
# keep_cols = ['ticker', 'date', 'adj_close', 'adj_volume', 'volume_change', 'price_change', 'gain', 'loss']
# new_df = df[keep_cols]
# new_df.to_csv('price_output_5.csv', index = False)


# DELETE COLUMNS
# df = df.drop('avg_gain', 1)
# df = df.drop('avg_loss', 1)

# ASSIGN EMPTY COLUMNS TO DATAFRAME
# df['avg_gain'] = 0
# df['avg_loss'] = 0
# df.loc[0, 'avg_gain'] = 0
# df.loc[0, 'avg_loss'] = 0



