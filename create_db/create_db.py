#!/usr/bin/env python3
import pymysql.cursors


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)

cursor = conn.cursor()

# cursor.execute('CREATE DATABASE bigdump;')

cursor.execute('grant all privileges on *.* to scox@localhost identified by "scox" with grant option;')

conn.commit()
conn.close()