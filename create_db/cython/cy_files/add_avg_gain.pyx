import pandas as pd
import numpy as np
import timeit
import csv


start = timeit.default_timer()


df = pd.read_csv("../price_output_7.csv")


counter = 0
prev_ticker = ''
last_avg_gain = 0

for row in df.itertuples():
	if row.ticker == prev_ticker:
		df.loc[row.Index, 'avg_gain'] = ( (last_avg_gain * 13) + row.gain ) / 14
	else:
		df.loc[row.Index, 'avg_gain'] = 0
	prev_ticker = row.ticker
	last_avg_gain = df.loc[row.Index, 'avg_gain']
	counter += 1
	if counter % 100 == 0:
		print ("Percent complete = ", counter / 14663500)


df.to_csv('price_output_8.csv', index = False)


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )