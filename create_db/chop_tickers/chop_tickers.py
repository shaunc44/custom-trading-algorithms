import csv
import pandas as pd


df = pd.read_csv(
	"../price_output_7.csv",
	usecols=['ticker', 'date', 'adj_close', 'adj_volume', 'gain', 'loss', 'volume_change', 'price_change'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)


groups = df.groupby('ticker')

for name, group in groups:
	with open('{}.csv'.format(name), a) as f:
		writer = csv.writer(f)
		writer.writerow(group)
		print (name)