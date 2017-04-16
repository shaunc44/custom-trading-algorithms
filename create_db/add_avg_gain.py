import pandas as pd
import numpy as np
import timeit
import csv

#Begin timer
start = timeit.default_timer()


# df = pd.read_csv("../data/prices2.csv")
# df = pd.read_csv("price_output_copy.csv")
df = pd.read_csv("price_output_7.csv")


# THIS WORKED BUT WAS VERY SLOW !!!
counter = 0
for row in range(1, len(df)):
	if df.loc[row, 'ticker'] == df.loc[row-1, 'ticker']:
		df.loc[row, 'avg_gain'] = ((df.loc[row-1, 'avg_gain'] * 13) + df.loc[row, 'gain']) / 14
	else:
		df.loc[row, 'avg_gain'] = 0
	counter += 1
	if counter % 1000 == 0:
		print ("Percent complete = ", counter / 14663500)


# df['avg_loss'] = np.where( (df['ticker'] == df['ticker'].shift(1)), ( ( df['avg_loss'].shift(1) * 13 ) + df['loss'] ) / 14, 0 )


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




df.to_csv('price_output_8.csv', index = False)



#COLUMN HEADINGS
# print ("This is price_output_8\n")
# print (list(df.columns.values))
# print (df[:20])
#['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'ex-dividend', 'split_ratio', 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )






