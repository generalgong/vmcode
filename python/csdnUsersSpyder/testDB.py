#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
try:
    con = MySQLdb.connect("brian1" , "brian","general","csdn")
    cur = con.cursor()
    sql = "INSERT INTO BlogUser(pageID, pageMD5,pageUrl, userName, follows ,befollowed , followNum ,befollowedNum)   VALUES (2, 'qqqq' ,'url' ,'name','all;follow','befollowed',4,5)"
    try:
        cur.execute(sql)
        con.commit()
    except:
        con.rollback()
finally:
    if con:
        con.close()

