import pymysql.cursors
import pandas as pd
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


#Iterate through ticker symbol file
#Insert symbol into ticker table
with open("data/ticker_list_fundamentals.csv") as file:
	for line in file:
		# print ("Type = ", type(ticker)," ", ticker)
		cursor.execute('INSERT INTO ticker (symbol) VALUE ("{}");'.format(line.strip()))
		conn.commit()
	conn.close()


stop = timeit.default_timer()

print ("Seconds to run: ", (stop - start) )
# Seconds to run:  1.868534772998828




# #Iterate through ticker symbol file
# #Insert symbol into ticker table
# with open("data/ticker_list_fundamentals.csv") as file:
# 	# for ticker in file:
# 	# 	# print ("Type = ", type(ticker)," ", ticker)
# 	# 	cursor.execute('''
# 	# 		INSERT INTO ticker (symbol) VALUES (?);
# 	# 	''', [ticker])
# 	)

# with open("data/ticker_list_fundamentals.csv") as file:
# 	cursor.executemany(
# 		'''
# 			INSERT INTO ticker (symbol) VALUES (?);
# 		''', 
# 		((ticker,) for ticker in file)
# 	)