#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def getUseHomePage():
	sql = "select pageID , userName from BlogUser order by pageID ASC limit 10 "
	try:
	    con = MySQLdb.connect("brian1" , "brian","general","csdn")
	    cur = con.cursor()
	    try:
		cur.execute(sql)
		results = cur.fetchall()
		fname = []
		for row in results:
			fname.append(row[1])
		homePages = map(lambda x: "http://my.csdn.net/"+x , fname)
	        print homePages
		return homePages
	    except:
	        print "execute select failed. \n" 
	finally:
	    if con:
		con.close()

