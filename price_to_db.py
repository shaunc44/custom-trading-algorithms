import pymysql.cursors
import pandas as pd
import numpy as np
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


cursor.execute("""
	SELECT symbol, id FROM ticker;
""")

rows = cursor.fetchall()
ticker_map = pd.DataFrame.from_records(list(rows), columns=["symbol", "id"]) 
ticker_map = ticker_map.set_index("symbol")


#Fundamentals.csv file is so large that we have to break into 10000 line chunks
#Overloads 8gb memory of my MacbookAir
df_price_reader = pd.read_csv(
	"data/prices.csv",
	usecols=['ticker', 'date', 'adj_close', 'adj_volume'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)


def parse_val(val):
	if isinstance(val, np.float64):
		return 0.0 if np.isnan(val) else float(val)
	elif isinstance(val,np.int64):
		return int(val)
	else:
		return val



counter = 0

for chunk in df_price_reader:
	cursor.executemany('''
		INSERT INTO price (
		ticker_id,
		date,
		adj_close,
		adj_volume) 
		VALUES (
			%(ticker)s,
			%(date)s,
			%(adj_close)s,
			%(adj_volume)s
		);''',
		(
			[str(parse_val(row[idx])) for idx in range(1,len(row))]
			for row in chunk.itertuples()

			# (parse_row(row) for row in chunk.to_dict(orient="records"))
		)
	)
	conn.commit()


	counter += 10000
	print ("Percent Complete = ", (counter/14663457)*100, "%")

conn.close()


# counter = 0

# for chunk in df_price_reader:
# 	cursor.executemany('''
# 		INSERT INTO price (
# 		ticker_id,
# 		ticker,
# 		date,
# 		adj_close,
# 		adj_volume) 
# 		VALUES (1,%s,%s,%s,%s);''',
# 		(
# 			[str(parse_val(row[idx])) for idx in range(1,len(row))]
# 			for row in chunk.itertuples()
# 		)
# 	)
# 	conn.commit()


# 	counter += 10000
# 	print ("Percent Complete = ", (counter/14663457)*100, "%")

# conn.close()



stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )
# Seconds to run: 4928 = 82 min





# counter = 0

# for chunk in df_prices_2005:
# 	cursor.executemany('''
# 		INSERT INTO price (
# 		ticker_id,
# 		ticker,
# 		date,
# 		open,
# 		high,
# 		low,
# 		close,
# 		volume,
# 		ex_dividend,
# 		split_ratio,
# 		adj_open,
# 		adj_high,
# 		adj_low,
# 		adj_close,
# 		adj_volume) 
# 		VALUES (1,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);''',
# 		(
# 			[str(parse_val(row[idx])) for idx in range(1,len(row))]
# 			for row in chunk.itertuples()
# 		)
# 	)
# 	conn.commit()

# 	counter += 1
# 	print ("Counter = ", counter)

# conn.close()




