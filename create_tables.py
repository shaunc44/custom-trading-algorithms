#!/usr/bin/env python3
import pymysql.cursors
import csv


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)

cursor = conn.cursor()


cursor.execute('''
DROP TABLE IF EXISTS user;
CREATE TABLE user (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
username VARCHAR(128) NOT NULL, 
password VARCHAR(128) NOT NULL
);''')


cursor.execute('''
DROP TABLE IF EXISTS price;
CREATE TABLE price (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
ticker_id INTEGER NOT NULL,
ticker VARCHAR(128) NOT NULL,
date VARCHAR(128) NOT NULL,
open FLOAT NULL,
high FLOAT NULL,
low FLOAT NULL,
close FLOAT NULL,
volume FLOAT NULL,
ex_dividend FLOAT NULL,
split_ratio FLOAT NULL,
adj_open FLOAT NULL,
adj_high FLOAT NULL,
adj_low FLOAT NULL,
adj_close FLOAT NULL,
adj_volume FLOAT NULL
);''')


cursor.execute('''
DROP TABLE IF EXISTS ticker;
CREATE TABLE ticker (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
symbol VARCHAR(128) NOT NULL
);''')


cursor.execute('''
DROP TABLE IF EXISTS fundamental;
CREATE TABLE fundamental (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
ticker_id INTEGER NOT NULL,
ticker VARCHAR(128) NOT NULL,
date VARCHAR(128) NOT NULL,
value FLOAT NULL,
indicator VARCHAR(128) NOT NULL,
dimension VARCHAR(128) NULL
);''')


cursor.execute('''
ALTER TABLE price ADD FOREIGN KEY (ticker_id) REFERENCES ticker (id);
ALTER TABLE fundamental ADD FOREIGN KEY (ticker_id) REFERENCES ticker (id);
ALTER TABLE user ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE price ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE ticker ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE fundamental ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')








# counter = 0
# with open("ticker_list3.csv") as file:
# 	for symbol in file:
# 		cursor.execute('''
# insert into prices (
# id INT AUTO_INCREMENT,
# ticker VARCHAR(128),
# date VARCHAR(128),
# open FLOAT,
# high FLOAT,
# low FLOAT,
# close FLOAT,
# volume FLOAT,
# ex_dividend FLOAT,
# split_ratio FLOAT,
# adj_open FLOAT,
# adj_high FLOAT,
# adj_low FLOAT,
# adj_close FLOAT,
# adj_volume FLOAT,
# PRIMARY KEY (id)
# );'''.)
# 		conn.commit()
# 		counter += 1
# 		print ("\nCounter = ", counter)
# 		print ("Symbol = ", symbol)
# 	conn.close()




