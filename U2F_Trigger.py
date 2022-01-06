import sqlite3 as sq3
from updateDataBase import *

def U2F():
	print("U2F is Triggered")


def U2FTrigger(targetAccount, days, threshold):
	updateDataBase(days)
	conn = sq3.connect("blockchain.db")
	cur = conn.cursor()
	# some SQL code, e.g. select first five entries of the table Quick
	cur.execute("SELECT COUNT(DISTINCT *) FROM Quick WHERE")
	a = cur.fetchall() #list of tuples containing all elements of the row
	conn.close()
	if a[0][0] > threshold:
		U2F()

targetAccount = '0xd3CdA913deB6f67967B99D67aCDFa1712C293601'
U2FTrigger(targetAccount, 1, 20)