import settings
import sqlite3
import tweepy
import dataset
from textblob import TextBlob
from sqlite3 import Error

db = dataset.connect(settings.CONNECTION_STRING)
result = db[settings.TABLE_NAME].all()


try:
	conn = sqlite3.connect(settings.CONNECTION_STRING)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
	#Question 3
	search_item = "polls"
	query = "SELECT * FROM election WHERE TEXT LIKE '%{0}%';".format(search_item)
    rows = cur.fetchall()
    for row in rows:
        print(row)

		#Question 4 a.)
	date_start = "2017_12_01"  #YYYY_MM_DD
	date_end = "2017_12_03"
	query = "SELECT * FROM election WHERE created BETWEEN {0} AND {1};".format(date_start, date_end)
    rows = cur.fetchall()
    for row in rows:
        print(row)

	#Question 4 b.)
	check_condition_int = 100
	query = "SELECT * FROM election WHERE user_followers >= {0};".format(check_condition_int)
    rows = cur.fetchall()
    for row in rows:
        print(row)
	
	#Question 4 c.)
	str_match_parameter = "comm"
	query = "SELECT * FROM election WHERE user_description LIKE '{0}%';".format(check_condition_int)   #For comm in starting of the string
	rows = cur.fetchall()
    for row in rows:
        print(row)
	
	#Question 5
	sort_by_field = "user_followers"
	query = "SELECT * FROM election ORDER BY {0};".format(sort_by_field)
	rows = cur.fetchall()
    for row in rows:
        print(row)	
	
	#Question 6
	group_by_field = "user_name"
	query = "SELECT {0}, COUNT(*) FROM election GROUP BY {1};".format(group_by_field, group_by_field)
	rows = cur.fetchall()
    for row in rows:
        print(row)		
	
	
except Error as e:
	print(e)

#Question 7
dataset.freeze(result, format='csv', filename=settings.CSV_NAME)