import pandas as pd
import timeit
import mysql


# conn = mysql.connect("stock_algo.db")
# cursor = conn.cursor
# df.to_sql("stock_algo", conn)

start = timeit.default_timer()

df = pd.read_csv("data/prices.csv", usecols=['ticker', 'date', 'adj_close', 'adj_volume'])
# df = pd.read_csv("data/historical_stock_prices.csv", usecols=['ticker', 'date', 'adj_close', 'adj_volume'])

#CREATE DF WITH DATES GREATER THAN 2006
df2007 = df[ (df['date']) > '2006-12-31' ]


#COLUMN HEADINGS
# print (list(df.columns.values))
# ticker date open high low close volume ex_dividend  split_ratio  adj_open  adj_high  adj_low  adj_close adj_volume


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


#COLUMN HEADINGS
# print (list(df.columns.values))
# ['AAAP_ACCOCI_ARQ', '2016-04-29', '0.0']


# SEPARATE 1ST COLUMN INTO 3 COLUMNS
# df = pd.DataFrame(df)
# df = pd.DataFrame(df.ix[:,0:1].split('_',1).tolist(), columns = ['ticker', 'indicator', 'dimension'])
# df = pd.DataFrame(df.ticker.str.split('_',1).tolist(), columns = ['ticker', 'indicator', 'dimension'])



stop = timeit.default_timer()

print ("Seconds to run: ", (stop - start) )


#Schema goes here *********
# def createDB(conn):
# 	pass

# conn.execute('''
# 	DROP TABLE IF EXISTS `bigdump`.`dump`;
# 	CREATE TABLE `bigdump`.`dump` (
# 		`id` INT NOT NULL AUTO_INCREMENT,
# 		`ticker` VARCHAR(128),
# 		`date` VARCHAR(128),
# 		`adj_close` FLOAT,
# 		`adj_volume` FLOAT,
# 		PRIMARY KEY (`id`)
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


