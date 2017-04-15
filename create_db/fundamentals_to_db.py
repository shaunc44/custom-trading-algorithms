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
	# cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()


cursor.execute("""
	SELECT symbol, id FROM ticker;
""")

rows = cursor.fetchall()
ticker_map = pd.DataFrame.from_records(list(rows), columns=["symbol", "id"]) 
ticker_map = ticker_map.set_index("symbol")


#fundamentals.csv file is so large that we have to break into 10000 line chunks
#Overloads 8gb memory on my MacbookAir
df_fundamental_reader = pd.read_csv(
	"data/fundamentals.csv",
	names=['ticker', 'date', 'value'],
	chunksize=10000,
	low_memory=True,
	engine='c'
)

#COLUMN HEADINGS
# print (list(df.columns.values))
# ['AAAP_ACCOCI_ARQ', '2016-04-29', '0.0']

def parse_code(value): 
	code = value.split("_")
	if len(code) == 3: return code
	return code + [""]


def parse_row(row):
	for key in row:
		val = row[key] if key != "ticker" else ticker_map.ix[row[key]].id
		if isinstance(val, np.float64):
			row[key] = 0.0 if np.isnan(val) else float(val)
		elif isinstance(val,np.int64):
			row[key] = int(val)
		else: 
			row[key] = val
	return row


counter = 0

for chunk in df_fundamental_reader:
	chunk['ticker'], chunk['indicator'], chunk['dimension'] = zip( *chunk['ticker'].map(parse_code) )
	# print (chunk)
	# print (type(chunk['value']), chunk['value'])

	cursor.executemany('''
		INSERT INTO fundamental (
		ticker_id,
		date,
		value,
		indicator,
		dimension) 
		VALUES (
			%(ticker)s,
			%(date)s,
			%(value)s,
			%(indicator)s,
			%(dimension)s
		);''',
		(parse_row(row) for row in chunk.to_dict(orient="records"))
	)
	conn.commit()

	counter += 10000
	print ("Percent Complete = ", (counter/94575000)*100, "%")

conn.close()


stop = timeit.default_timer()
print ("Seconds to run: ", (stop - start) )
#Seconds to run: 49124 = 13 hrs 39 min












