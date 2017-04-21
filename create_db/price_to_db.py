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
	# cursorclass=pymysql.cursors.DictCursor #do we need this anymore?
	)

cursor = conn.cursor()


cursor.execute("""
	SELECT symbol, id FROM ticker;
""")

rows = cursor.fetchall()
ticker_map = pd.DataFrame.from_records(list(rows), columns=["symbol", "id"]) 
ticker_map = ticker_map.set_index("symbol")
# ticker_only = ticker_map.ix[:,0]


#prices.csv file is so large that we have to break into 10000 line chunks
#Overloads 8gb memory on my MacbookAir
df_price_reader = pd.read_csv(
	"price_output_final.csv",
	usecols=['ticker', 'date', 'adj_close', 'adj_volume', 'volume_chg_pct', 'price_chg_pct', 'rsi'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)


#ORIGINAL
# def parse_val(val):
# 	if isinstance(val, np.float64):
# 		return 0.0 if np.isnan(val) else float(val)
# 	elif isinstance(val,np.int64):
# 		return int(val)
# 	else:
# 		return val


def parse_row(row):
	# print (row)
	if row["ticker"] not in ticker_map.index:
		print("New ticker added: ", row["ticker"])
		cursor.execute("""
				INSERT INTO ticker(symbol) VALUES(%s);
			""", (row["ticker"],))
		ticker_map.ix[row["ticker"]] = cursor.lastrowid

	for key in row:
		# print ("Key: ", key, "Row[key]", row[key])
		val = row[key] if key != "ticker" else ticker_map.ix[row[key]].id

		if isinstance(val, (np.float64, float)):
			row[key] = 0.0 if np.isnan(val) or np.isinf(val) else float(val)
		elif isinstance(val,np.int64):
			row[key] = int(val)
		else:
			row[key] = val
	return row


counter = 0

for chunk in df_price_reader:
	cursor.executemany("""
		INSERT INTO price (
		ticker_id,
		date,
		adj_close,
		adj_volume,
		volume_chg_pct,
		price_chg_pct,
		rsi) 
		VALUES(
			%(ticker)s,
			%(date)s,
			%(adj_close)s,
			%(adj_volume)s,
			%(volume_chg_pct)s,
			%(price_chg_pct)s,
			%(rsi)s
		);""",
		(
			# [str(parse_val(row[idx])) for idx in range(1,len(row))]
			# for row in chunk.itertuples()
			(parse_row(row) for row in chunk.to_dict(orient="records"))
		)
	)
	conn.commit()

	counter += 10000
	print ("Percent Complete = ", (counter/14663457)*100, "%")


conn.close()


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )
# Seconds to run:  9118 = 2 hrs 32 mins



#THIS IS THE OLD CODE **********************************************
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
#********************************************************************






