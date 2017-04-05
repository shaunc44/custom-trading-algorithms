import flask
import pymysql.cursors
# import wrapper
#use pandas in here, not createdb
#use data from Quandl, Xignite


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)
c = conn.cursor()


# def test_cr():
c.callproc('sp_getTickerWithCR')
data = c.fetchall()
print (data) #returns tuples with {ticker: symbol}