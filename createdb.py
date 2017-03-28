import pandas as pd
import timeit
import mysql


# conn = mysql.connect("stock_algo.db")
# cursor = conn.cursor
# df.to_sql("stock_algo", conn)

start = timeit.default_timer()

df = pd.read_csv("data/stocks_eod_prices.csv", usecols=['ticker', 'date', 'adj_close', 'adj_volume'])

#CREATE DF WITH DATES GREATER THAN 2006
df2007 = df[ (df['date']) > '2006-12-31' ]


#COLUMN HEADINGS
# print (list(df.columns.values))
#ticker date open high low close volume ex-dividend  split_ratio  adj_open  adj_high  adj_low  adj_close, adj_volume


#EARLIEST PRICE DATE
#print (df['date'].min())
#1962-01-02


#LATEST PRICE DATE
#print (df['date'].max())
#2017-03-07


#LENGTH OF FILE
# print (len(df.index)) -- 14,663,457
# print (len(df2007.index)) -- 7,029,966

#LAST TICKER SYMBOL
# print (df[-5:]) #-- last ticker ZUMZ
# print (df2007[-5:])



stop = timeit.default_timer()

print ("Seconds to run: ", (stop - start) )


#Schema goes here *********
# def createDB(conn):
# 	pass
	# conn.execute('''
	# 	DROP TABLE 'users'
	# ''')

	# conn.execute('''
	# 	DROP TABLE 'phone_numbers'
	# ''')

	# conn.execute('''
	# 	DROP TABLE 'addresses'
	# ''')

	# conn.execute('''
	# 	CREATE TABLE 'users' (
	# 	'user_id' INTEGER PRIMARY KEY AUTOINCREMENT,
	# 	'username' TEXT,
	# 	'password' TEXT,
	# 	'firstname' TEXT,
	# 	'lastname' TEXT,
	# 	'dob' TEXT,
	# 	'permission' TEXT
	# 	);
	# ''')

	# conn.execute('''
	# 	CREATE TABLE 'phone_numbers' (
	# 	'phone_id' INTEGER PRIMARY KEY AUTOINCREMENT,
	# 	'user_id' INTEGER,
	# 	'phone_type' TEXT,
	# 	'phone_number' TEXT,
	# 	FOREIGN KEY(user_id) REFERENCES users(user_id)
	# 	);
	# ''')

	# conn.execute('''
	# 	CREATE TABLE 'addresses' (
	# 	'address_id' INTEGER PRIMARY KEY AUTOINCREMENT,
	# 	'user_id' INTEGER,
	# 	'street' TEXT,
	# 	'city' TEXT,
	# 	'state' TEXT,
	# 	'zip_code' TEXT,
	# 	FOREIGN KEY(user_id) REFERENCES users(user_id)
	# 	);
	# ''')

# conn = mysql.connect('daily_prices.db')

# .cursor() allows the program to directly access the DB 
# instead of bringing the entire database into python 
# which would consume greater memory
# c = conn.cursor()
# conn.cursor()

# createDB(conn)

#saves the database currently in memory to the hard drive
# conn.commit()

#closes the file so that other users/programs can use the file
# conn.close()


