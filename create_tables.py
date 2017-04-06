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
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS user;
SET foreign_key_checks = 1;
CREATE TABLE user (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
username VARCHAR(128) NOT NULL, 
password VARCHAR(128) NOT NULL
);''')


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS price;
SET foreign_key_checks = 1;
CREATE TABLE price (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
ticker_id INTEGER NOT NULL,
ticker VARCHAR(128) NOT NULL,
date VARCHAR(128) NOT NULL,
adj_close FLOAT NULL,
adj_volume FLOAT NULL
);''')


# cursor.execute('''
# SET foreign_key_checks = 0;
# DROP TABLE IF EXISTS price;
# SET foreign_key_checks = 1;
# CREATE TABLE price (
# id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
# ticker_id INTEGER NOT NULL,
# ticker VARCHAR(128) NOT NULL,
# date VARCHAR(128) NOT NULL,
# open FLOAT NULL,
# high FLOAT NULL,
# low FLOAT NULL,
# close FLOAT NULL,
# volume FLOAT NULL,
# ex_dividend FLOAT NULL,
# split_ratio FLOAT NULL,
# adj_open FLOAT NULL,
# adj_high FLOAT NULL,
# adj_low FLOAT NULL,
# adj_close FLOAT NULL,
# adj_volume FLOAT NULL
# );''')


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS ticker;
SET foreign_key_checks = 1;
CREATE TABLE ticker (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
symbol VARCHAR(128) NOT NULL
);''')


# cursor.execute('''
# SET foreign_key_checks = 0;
# DROP TABLE IF EXISTS fundamental;
# SET foreign_key_checks = 1;
# CREATE TABLE fundamental (
# 	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
# 	ticker_id INTEGER NOT NULL,
# 	ticker VARCHAR(128) NOT NULL,
# 	date VARCHAR(128) NOT NULL,
# 	value FLOAT NULL,
# 	indicator VARCHAR(128) NOT NULL,
# 	dimension VARCHAR(128) NULL
# )
# PARTITION BY LIST(indicator) (
# 	PARTITION pCURRENTRATIO VALUES IN ('CURRENTRATIO'),
# 	PARTITION pDE VALUES IN ('DE'),
# 	PARTITION pEPS VALUES IN ('EPS'),
# 	PARTITION pDIVYIELD VALUES IN ('DIVYIELD'),
# 	PARTITION pPE1 VALUES IN ('PE1'),
# 	PARTITION pPB VALUES IN ('PB'),
# 	PARTITION pROIC VALUES IN ('ROIC'),
# 	PARTITION pROE VALUES IN ('ROE')
# );''')


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS fundamental;
SET foreign_key_checks = 1;
CREATE TABLE fundamental (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ticker_id INTEGER NOT NULL,
	ticker VARCHAR(128) NOT NULL,
	date VARCHAR(128) NOT NULL,
	value FLOAT NULL,
	indicator VARCHAR(128) NOT NULL,
	dimension VARCHAR(128) NULL
)
PARTITION BY LIST COLUMNS(indicator) (
	PARTITION pCURRENTRATIO VALUES IN('CURRENTRATIO'),
	PARTITION pDE VALUES IN('DE'),
	PARTITION pBVPS VALUES IN('BVPS'),
	PARTITION pEPS VALUES IN('EPS'),
	PARTITION pDIVYIELD VALUES IN('DIVYIELD'),
	PARTITION pPE1 VALUES IN('PE1'),
	PARTITION pPB VALUES IN('PB'),
	PARTITION pROIC VALUES IN('ROIC'),
	PARTITION pROE VALUES IN('ROE'),
	PARTITION pNETMARGIN VALUES IN('NETMARGIN'),
	PARTITION pFCF VALUES IN('FCF'),
	PARTITION pPS VALUES IN('PS'),
	PARTITION pROA VALUES IN('ROA'),
	PARTITION pTANGIBLES VALUES IN('TANGIBLES'),
	PARTITION pROS VALUES IN('ROS'),
	PARTITION pWORKINGCAPITAL VALUES IN('WORKINGCAPITAL'),
	PARTITION pMARKETCAP VALUES IN('MARKETCAP'),
	PARTITION pFCFPS VALUES IN('FCFPS')
);''')


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS fundamental;
SET foreign_key_checks = 1;
CREATE TABLE fundamental (
	ticker_id INTEGER NOT NULL,
	ticker VARCHAR(128) NOT NULL,
	date VARCHAR(128) NOT NULL,
	value FLOAT NULL,
	indicator VARCHAR(128) NOT NULL,
	dimension VARCHAR(128) NULL
)
PARTITION BY LIST COLUMNS(indicator) (
	PARTITION pCURRENTRATIO VALUES IN('CURRENTRATIO'),
	PARTITION pDE VALUES IN('DE'),
	PARTITION pBVPS VALUES IN('BVPS'),
	PARTITION pEPS VALUES IN('EPS'),
	PARTITION pDIVYIELD VALUES IN('DIVYIELD'),
	PARTITION pPE1 VALUES IN('PE1'),
	PARTITION pPB VALUES IN('PB'),
	PARTITION pROIC VALUES IN('ROIC'),
	PARTITION pROE VALUES IN('ROE'),
	PARTITION pNETMARGIN VALUES IN('NETMARGIN'),
	PARTITION pFCF VALUES IN('FCF'),
	PARTITION pPS VALUES IN('PS'),
	PARTITION pROA VALUES IN('ROA'),
	PARTITION pTANGIBLES VALUES IN('TANGIBLES'),
	PARTITION pROS VALUES IN('ROS'),
	PARTITION pWORKINGCAPITAL VALUES IN('WORKINGCAPITAL'),
	PARTITION pMARKETCAP VALUES IN('MARKETCAP'),
	PARTITION pFCFPS VALUES IN('FCFPS')
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




